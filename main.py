# https://api.telegram.org/bot<bot token>/getUpdates?offset=-1
from tg_send_type import send_message, send_photo

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = open('token.txt').readline()
MAX_COUNTER = 100
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'

def tg_cat_request(API_URL, BOT_TOKEN, MAX_COUNTER):
    import requests
    import time

    offset = -2
    chat_id: int
    counter = 0
    cat_response: requests.Response

    while counter < MAX_COUNTER:
        print('attempt=', counter)

        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                message_text = result['message']['text']
                if message_text == 'котика на базу':
                    cat_response = requests.get(API_CATS_URL)
                    if cat_response.status_code == 200:
                        cat_link = cat_response.json()[0]['url']
                        send_photo(cat_link, chat_id, BOT_TOKEN)
                    else:
                        send_message('Сегодня без котиков (', chat_id, BOT_TOKEN)
                elif message_text == 'сосал?':
                    send_message('Пфф. Конечно!', chat_id, BOT_TOKEN)


        time.sleep(1)
        counter += 1


if __name__ == '__main__':
    tg_cat_request(API_URL, BOT_TOKEN, MAX_COUNTER)
