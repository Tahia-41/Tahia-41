import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
Alexa = pyttsx3.init()
voices = Alexa.getProperty('voices')
Alexa.setProperty('voice', voices[1].id)



def talk(text):
    Alexa.say(text)
    Alexa.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
    except:
        return 'none'
    return command

def run_brain():
    command = listen().lower()
    if 'alexa' in command:
        command = command.replace('alexa', '')
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 1)
            talk(info)
        elif "goodbye" in command:
            talk("GoodBye. Keep exploring more exciting things.")
            exit()
        elif command != 'none':
            talk('I did not get it but I am going to search it for you')
            pywhatkit.search(command)

talk("hello sir I am Alexa, your desktop assistant. Tell me how may I help you")
while True:
    run_brain()