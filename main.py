import replicate
import os
from dotenv import load_dotenv

# Загрузим .env файл
load_dotenv()

# Получим токен
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Установим токен
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Вызов модели
output = replicate.run(
    "lucataco/magnet:e8e2ecd4a1dabb58924aa8300b668290cafae166dd36baf65dad9875877de50e",
    input={
        "prompt": "a melodic lo-fi beat with soft drums and a jazzy vibe"
    }
)

print("🎵 Output:", output)
