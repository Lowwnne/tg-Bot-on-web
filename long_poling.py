import time
import requests

BOT_TOKEN = '6531110683:AAFX7L-n1andA4uZqYhYDAC6RG4aWxNQWF4'

offset = -2
updates: dict
timeout = 10

while True:
    start_time = time.time()
    updates = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']

            print('Работаем...')

    print(f'Время апдейта: {int(time.time() - start_time)}')