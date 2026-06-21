import uuid
import requests
import streamlit as st


ASK_API_URL = "http://localhost:8000/ask"
UPLOAD_API_URL = "http://localhost:8000/upload"


st.set_page_config(
    page_title="Adaptive RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Adaptive RAG Assistant")


# ==================================
# Session Initialization
# ==================================

if "session_id" not in st.session_state:
    st.session_state.session_id = str(
        uuid.uuid4()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==================================
# Sidebar Upload
# ==================================

with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if st.button("Upload PDF"):

        if uploaded_file is None:

            st.warning(
                "Please select a PDF."
            )

        else:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                UPLOAD_API_URL,
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    f"Uploaded successfully. "
                    f"Chunks: {result['chunks']}"
                )

            else:

                st.error(
                    "Upload failed."
                )


# ==================================
# Display Chat History
# ==================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# ==================================
# Chat Input
# ==================================

question = st.chat_input(
    "Ask a question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            response = requests.post(
                ASK_API_URL,
                json={
                    "question": question,
                    "session_id": st.session_state.session_id
                }
            )

            if response.status_code == 200:

                answer = response.json()[
                    "answer"
                ]
                st.session_state.session_id = response.json().get(
                    "session_id",
                    st.session_state.session_id
                )

                st.markdown(
                    answer
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            else:

                st.error(
                    "Failed to get response."
                )
