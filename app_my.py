import queue
import sounddevice as sd  # pip install sounddevice это доступ к микрофону
import vosk  # pip install vosk распознаватель речи
import json
import words
# import voice
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
from skills import *

# python -m sounddevice выдает все устройства ввода/вывода звука

q = queue.Queue()
model = vosk.Model('vosk_model_small_ru')

device = sd.default.device = 1, 3     # <--- по умолчанию
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


# samplerate = 44100, частота дискретизации (в секунду)
# blocksize - количество сэмплов, которе будет передаваться на обработку
# device
# dtype
# channels
# callback

def recognize(data, vectorizer, clf):
    '''
    Анализ распознанной речи
    '''
    # data придет в форме словаря {'text' ".......какие-то слова_через_пробел_текст.............."}
    # проверяем есть ли имя бота в data, если нет, то return
    # .intersection( проверяет пересечение 2-х списков (круги Эйлера)
    trg = words.TRIGGERS.intersection(data.split())
    # если trg, то возвращается пустой кортеж set(), а если присутствует, то со значением: {'кристи'}
    if not trg:
        print('not trg')
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    # получаем вектор полученного текста
    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    print(answer)
    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    speaker(answer.replace(func_name, ''))

    # запуск функции из skills
    exec(func_name + '()')


def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''

    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    # print(vectors.toarray()) # смотрим закодированный текст
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))
    del words.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                # print(rec.Result())
                # json.loads(rec.Result())['text'] возвращается str в которой слова, разделенные пробелами
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            # else:
            #     print(rec.PartialResult())


if __name__ == '__main__':
    main()
