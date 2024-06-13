import requests

from config.settings import TELEGRAM_BOT_API_KEY

telegram_token = TELEGRAM_BOT_API_KEY
send_message_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'


def send_message(telegram_id, message):
    requests.post(url=send_message_url,
                  data={"chat_id": telegram_id, "text": message})
