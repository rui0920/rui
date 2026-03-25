import pathlib
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()


def main():
    # Define workspace path relative to this script
    current_dir = pathlib.Path(__file__).parent
    workspace_path = current_dir / "workspace"

    # Read persona and user preference files
    soul_file = workspace_path / "SOUL.md"
    user_file = workspace_path / "USER.md"

    if not soul_file.exists() or not user_file.exists():
        print(f"Error: Missing {soul_file} or {user_file}")
        return

    soul_content = soul_file.read_text(encoding="utf-8")
    user_content = user_file.read_text(encoding="utf-8")

    llm = ChatOpenAI(
        model="gemma3:27b",
        base_url="http://203.71.78.31:8000/v1",
        api_key="sk-12345678",
        temperature=0.0,
    )

    # Combine file contents into a system prompt
    system_prompt = f"""【系統角色 / System Role】
{soul_content}

【使用者偏好 / User Preferences】
{user_content}
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content="自我介紹  "),
    ]

    for chunk in llm.stream(messages):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    main()

