import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import datetime

r=sr.Recognizer()

with sr.Microphone()as source:
     print('Say Something!')
     audio = r.adjust_for_ambient_noise(source)
     audio=r.listen(source)
     print('Done!')
try:
    ftext=r.recognize_google(audio)
    print ('Google thinks you said: \n' + ftext)
except Exception as e:
    print(e)

tts=gTTS(text=ftext ,lang='en')
tts.save("123.mp3")
playsound('123.mp3')
