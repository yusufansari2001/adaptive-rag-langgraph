import requests
import streamlit as st


API_URL = "http://localhost:8000/ask"


st.set_page_config(
    page_title="Adaptive RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Adaptive RAG Assistant")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    if not question.strip():
        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Thinking..."
        ):

            response = requests.post(
                API_URL,
                json={
                    "question": question
                }
            )

            if response.status_code == 200:

                answer = response.json()[
                    "answer"
                ]

                st.success(
                    "Answer"
                )

                st.write(
                    answer
                )

            else:

                st.error(
                    "Failed to get response from API."
                )