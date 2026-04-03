# load_env.py
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Ollama設定を取得
ollama_url = os.getenv("OLLAMA_BASE_URL")
ollama_model = os.getenv("OLLAMA_MODEL")

print(f"Ollama URL: {ollama_url}")
print(f"Ollama Model: {ollama_model}")

# APIキーは最初の5文字だけ表示（セキュリティの基本）
openai_key = os.getenv("OPENAI_API_KEY", "未設定")
print(f"OpenAI key: {openai_key[:8]}...")
