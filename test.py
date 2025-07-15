# import sys
import pyttsx3
from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
# import words
print(1+1)
# print(sys.path)
# sys.path.append('C:\\ProgramData\\anaconda3\\pkgs')
# print(sys.path)
# from sklearn.feature_extraction.text import CountVectorizer
# print(get_python_lib())

# vectorizer = CountVectorizer()
# # print(list(words.data_set.keys()))
# vectors = vectorizer.fit_transform(list(words.data_set.keys()))
# vectorizer.get_feature_names_out()
# # for i in vectors:
# #     print(i)
# # print(vectors.toarray())
# data = 'кристи я не знаю что происходит'
# print(words.TRIGGERS.intersection(data.split()))


# engine = pyttsx3.init('dummy')     # инициализация движка

# # зададим свойства
# engine.setProperty('rate', 150)     # скорость речи
# engine.setProperty('volume', 0.9)   # громкость (0-1)

# engine.say("I can speak!")      # запись фразы в очередь
# engine.say("Я могу говорить!")  # запись фразы в очередь

# # очистка очереди и воспроизведение текста
# engine.runAndWait()

# engine = pyttsx3.init()
# engine.say("добрый день сэр")
# engine.runAndWait()

# class _TTS:
#     engine = None
#     rate = None

#     def __init__(self):
#         self.engine = pyttsx3.init()

#     def start(self, text_):
#         # Вот сюда пихай адрес голоса, в кавычках.
#         self.engine.setProperty(
#             'voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
#         self.engine.say(text_)
#         self.engine.runAndWait()


# # и вызываем:

# tts = _TTS()
# tts.start("добрый день сэр!")
# del tts

# # ---------------------------------------------------------------------
# engine = pyttsx3.init()

# for voice in engine.getProperty('voices'):
#     print(voice)
# # ---------------------------------------------------------------------

# engine = pyttsx3.init()
# ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
# engine.setProperty('voice', ru_voice_id)
# engine.say('привет')

# engine.runAndWait()

engine = pyttsx3.init()
ru_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0'
engine.setProperty('voice', ru_voice_id)
engine.setProperty('rate', 150)
engine.say("Уж нет пути вокруг зияет бездна, ты сам того хотел небезвоздмездно смелее странник здесь или нигде погибнешь ты подумав о беде")
engine.runAndWait()
