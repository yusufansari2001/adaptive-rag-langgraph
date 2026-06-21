from langchain_core.messages import AIMessage, BaseMessage, HumanMessage


def message_content_to_text(content) -> str:
    """
    Convert LangChain message content into readable plain text.
    """

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []

        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(str(item.get("text", item)))
            else:
                parts.append(str(item))

        return " ".join(parts)

    return str(content)


def get_messages(state) -> list[BaseMessage]:
    return state.get("messages", [])


def get_latest_human_message(state) -> HumanMessage:
    for message in reversed(get_messages(state)):
        if isinstance(message, HumanMessage):
            return message

    raise ValueError("No human message found in graph state.")


def get_latest_question(state) -> str:
    message = get_latest_human_message(state)

    return message_content_to_text(message.content).strip()


def get_latest_ai_answer(state) -> str:
    for message in reversed(get_messages(state)):
        if isinstance(message, AIMessage):
            return message_content_to_text(message.content).strip()

    return ""


def format_chat_history(
    state,
    max_messages: int = 8,
    include_latest_user_message: bool = False
) -> str:
    messages = get_messages(state)

    if not include_latest_user_message:
        messages = messages[:-1]

    messages = messages[-max_messages:]

    history_lines = []

    for message in messages:
        if isinstance(message, HumanMessage):
            role = "Human"
        elif isinstance(message, AIMessage):
            role = "Assistant"
        else:
            continue

        content = message_content_to_text(message.content).strip()

        if content:
            history_lines.append(f"{role}: {content}")

    if not history_lines:
        return "No previous conversation."

    return "\n".join(history_lines)
