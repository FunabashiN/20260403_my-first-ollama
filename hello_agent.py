# hello_agent.py
# LangChainの練習前の、python動作確認用コード

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    message = greet("funa")
    print(message)