import requests

from config.settings import TELEGRAM_URL, TG_BOT_TOKEN


def send_tg_message(chat_id, message):
    """Отправляет напоминаение о привычки в чат."""
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.get(f"{TELEGRAM_URL}{TG_BOT_TOKEN}/sendMessage", params=params)
