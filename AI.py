import json
from g4f.client import Client
from gtts import gTTS
from playsound3 import playsound
lang = input('Выберете язык(ru или en): ')
print('AI начал свою работу...')

client = Client()
while True:
    test = input('Вы: ')
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"{test}"}],
    web_search=True
    )
    print('AI: ' + response.choices[0].message.content)
    tts = gTTS(f'{response.choices[0].message.content}', lang=f'{lang}')
    tts.save('text.mp3')
    playsound('text.mp3')