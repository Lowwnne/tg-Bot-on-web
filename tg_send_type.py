API_URL: str
BOT_TOKEN: str
MAX_COUNTER = 100
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

def send_message(text: str, chat_id: str, token: str) -> None:
    from requests import get
    global BOT_TOKEN
    return get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

def send_photo(photo: str, chat_id: str, token: str):
    from requests import get
    return get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={photo}')