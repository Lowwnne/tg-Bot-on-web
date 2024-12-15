# https://api.telegram.org/bot6531110683:AAFX7L-n1andA4uZqYhYDAC6RG4aWxNQWF4/getUpdates?offset=-1
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6531110683:AAFX7L-n1andA4uZqYhYDAC6RG4aWxNQWF4'
TEXT = 'Ну типо ты мне написал, я ответил'
MAX_COUNTER = 100

def tg_base_request(API_URL, BOT_TOKEN, TEXT, MAX_COUNTER):
    import requests
    import time

    offset = -2
    chat_id: int
    counter = 0

    while counter < MAX_COUNTER:
        print('attempt=', counter)

        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')


        time.sleep(1)
        counter += 1


if __name__ == '__main__':
    tg_base_request(API_URL, BOT_TOKEN, TEXT, MAX_COUNTER)