#модули
import requests
import json
import os
import time

#главная функция
def text_to_speech(text):
    #по eden ai
    headers = {"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOWNjY2UyNTYtODhlYS00NmFiLThkNTAtOWMyODhmYjI1ZjQ3IiwidHlwZSI6ImFwaV90b2tlbiJ9.3Or_e6Fs_HKumsFM_x8PJnb_OQTY93JJUBZq3tfMZ5Q"}
    url = "https://api.edenai.run/v2/audio/text_to_speech"
    payload = {
        'providers': 'google',
        'language': 'ru-RU',
        'option': 'MALE',
        'google': 'ru-RU-Wavenet-B',
        'text': f'{text}'
    }
    #получение json файла с res
    responce = requests.post(url, json=payload, headers=headers)
    result = json.loads(responce.text)
    unx_time = int(time.time())

    with open(f'{unx_time}.json', 'w') as file:
        json.dump(result,file,indent=4,ensure_ascii=False)

    #автоматизация процесса (скачивание файла со звуком вместо ссылки)
    audio_url = result.get('google').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)

def main():
    text_to_speech(text=input())
if __name__=='__main__':
    main()