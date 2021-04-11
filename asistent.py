import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import bot as bt
import os

listener = sr.Recognizer()
engine = pyttsx3.init()

def voiceSpeak(text):
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('voice', voices[19].id)
    engine.setProperty('rate',180)
    engine.say(text)
    engine.runAndWait()

def listenMicro():

    try:
        with sr.Microphone()as source:
            print('Escuchando...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.record(source,duration=3)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            return "{}".format(rec)
    except Exception as e:
        print(e)

w = [
    'hola',
    'música rock',
    'detén música',
    'desconectar'
    ]

def command_automatice (rec):

    if rec is None:
        print('Esperando orden')

    elif w[0] in rec:
        voiceSpeak('Hola progamador')
        voiceSpeak('Que deseas realizar')

    elif w[1] in rec:
        voiceSpeak('Iniciando musica rock')
        voiceSpeak('Feliz haking')
        os.system('xfce4-terminal -e rock-hacking2.sh')

    elif w[2] in rec:
        voiceSpeak('Deteniendo musica')
        os.system('killall mpv')

    elif w[3] in rec:
        voiceSpeak('Desconectando asistente virtual')
        quit()

    elif 'reproduce' in rec:
        rec = rec.replace('reproduce', '')
        voiceSpeak(f'Reproduciendo a {rec}')
        pywhatkit.playonyt(rec)
        return

    elif 'hora es' in rec:
        hora_actual = datetime.datetime.now().strftime('%H:%M %p')
        voiceSpeak(f'Son las {hora_actual}')

    elif 'busca' in rec:
        rec = rec.replace('busca', '')

        wikipedia.set_lang("es")
        info = wikipedia.summary(rec, sentences=1)
        voiceSpeak(info)
        print(rec)

    else :
        for i in w:
            if i != w:
                voiceSpeak('ha dicho' + str(rec))
                voiceSpeak('Aun no me han programado para eso')
                return

