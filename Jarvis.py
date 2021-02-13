import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)
s = pyttsx3.init()
s.say('Hello Yash, I am jarvis, your personal assistant. What can I do for you')
s.runAndWait()

def talk(text):
     engine.say(text)
     print(text)
     engine.runAndWait()

def take_command():
  try:
      with sr.Microphone() as source:
           print('listening...')
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if 'jarvis' in command:
               command = command.replace('jarvis','')
               print(command)

  except:
      pass



def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing...'+ song)
        print('playing...'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current Time is '+ time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        fact = 'none'
        thing = command.replace('what is', '')
        fact = wikipedia.summary(thing,5)
        print(fact)
        talk(fact)
    elif 'are you single' in command:
        talk('I am in a relationship with faraday')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    else:
        talk('Pardon me, I cannot understand what you said, please come again')

while True:
    run_jarvis()