import replicate
import os
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()

# Получаем токен
api_token = os.getenv("REPLICATE_API_TOKEN")
assert api_token, "API token не найден. Убедись, что в .env файл есть REPLICATE_API_TOKEN."

# Устанавливаем токен
replicate.Client(api_token=api_token)

# Задаем модель
model = replicate.models.get("lucataco/magnet")
version = model.versions.get("e8e2ecd4a1dabb58924aa8300b668290cafae166dd36baf65dad9875877de50e")

# Ввод: описание сцены
prompt = "a cat skateboarding in Tokyo at night"

# Запуск
output = version.predict(prompt=prompt)

# Вывод результата
print("Output video URL:", output)
