# agent.py
# テスト可能な関数としてまとめる

def greet(name: str) -> str:
    """名前を受け取って挨拶を返す"""
    if not name:
        raise ValueError("Please Enter Your Name")
    return f"Hello, {name}! Let's get started with agent development."

def format_prompt(user_input: str, system: str = "") -> dict:
    """LangChain用のメッセージ形式に変換する"""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": user_input})
    return messages
