import os
import webbrowser
import sys
import subprocess
import pyttsx3  # pip install pyttsx3
import voice

try:
    import requests  # pip install requests
except:
    pass


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://dzen.ru/?ysclid=md1do2xkkj292795156', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    os.system('shutdown -s')
    # print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
    https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
    try:
        params = {'q': 'London', 'units': 'metric',
                  'lang': 'ru', 'appid': 'ключ к API'}
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(
            f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker(
            'Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass


# -----------------------блок озвучки (дублируем данные в файле voices.py)-----------------------------------
engine = pyttsx3.init()
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', ru_voice_id)  # скорость речи

# engine = pyttsx3.init('dummy')
# voice = engine.getProperty('voices')
engine.setProperty('rate', 180)  # скорость речи
# # зададим свойства
# engine.setProperty('rate', 150)     # скорость речи
# engine.setProperty('volume', 0.9)   # громкость (0-1)


def speaker(text):
    '''Озвучка текста'''
    print(f'тееееееееееееееееееееееекст: {text}')
    engine.say(text)
    engine.runAndWait()
