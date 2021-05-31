from chat import bot_name, get_response
from common import *

import speech_recognition as sr
import pyttsx3, time

r = sr.Recognizer()

def TextToSpeech(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def VoiceChat():
    print(greeting)
    while True:
        with sr.Microphone() as source:
            try:
                print(you, end="")
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                sentence = r.recognize_google(audio)
                print(sentence)
                
                if sentence == "quit":
                    response = "Thank you for visiting! I hope to see you again!"
                    print(f'{bot_name}: {response}\n')
                    TextToSpeech(response)
                    break

                response = get_response(sentence)
                print(f'{bot_name}: {response}\n')
                TextToSpeech(response)
                    
            except Exception as e:
                print(e)