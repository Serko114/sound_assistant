import queue
import sounddevice as sd  # pip install sounddevice это доступ к микрофону
import vosk  # pip install vosk распознаватель речи
import json
import words
import voice
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression

# python -m sounddevice выдает все устройства ввода/вывода звука

q = queue.Queue()
model = vosk.Model('vosk_model_small_ru')

device = sd.default.device  # = 1, 3     # <--- по умолчанию
# или -> sd.default.device = 1, 3, python -m sounddevice просмотр
# ! первое число - это микрофон, второе - динамики
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
# print(device, samplerate) -> выход: [1, 3] 44100 - каналы вход/выход и частота дискретизации
# print(device, samplerate)


def callback(indata, frames, time, status):
    '''
    Добавляет в очередь семплы из потока.
    вызывается каждый раз при наполнении blocksize
    в sd.RawInputStream'''

    q.put(bytes(indata))


with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                       channels=1, callback=callback):

    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Result())
            # data = json.loads(rec.Result())['text']
            # recognize(data, vectorizer, clf)
        else:
            print(rec.PartialResult())
