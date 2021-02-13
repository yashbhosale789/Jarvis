import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import pywhatkit
import wikipedia
import smtplib
import sys
import pyautogui
import webbrowser
import pyjokes
import time
from news_module import read_news

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        print(f"User Said: {command}")

    except Exception as e:
        speak('Pardon me, I cannot understand what you said. Please come again.')
        return 'none'
    return command

def tellday():
    day = datetime.datetime.today().weekday() + 1
    day_dict = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in day_dict.keys():
        day_of_the_week =day_dict[day]
        print(day_of_the_week)
        speak('The day is ' + day_of_the_week)

def wish():
    time = int(datetime.datetime.now().hour)

    if time>=5 and time<=12:
       speak('Good Morning')
    elif time>=12 and time<=18:
        speak('Good Afternoon')
    else:
        speak("Good Night")

    speak('I am Jarvis, your personal assistant. How can I help you?')

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

def run_jarvis():
    while True:
        command = takecommand().lower()
        if 'open' in command:
            if 'notepad' in command:
                path = "C:\\WINDOWS\\system32\\notepad.exe"
                speak('opening notepad')
                os.startfile(path)
            elif 'command prompt' in command:
                speak('opening command prompt ')
                os.system("start cmd")
            elif 'cmd' in command:
                speak('opening cmd')
                os.system("start cmd")
            elif 'control panel' in command:
                speak('opening control panel')
                os.system("start control panel")
            elif 'chrome' in command:
                path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                speak('opening chrome')
                webbrowser.get(path)
            elif 'whatsapp' in command:
                path = "C:\\Users\\Yash\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                speak('opening whatsapp')
                os.system(path)
            elif 'teams' in command:
                path = "C:\\Users\\Yash\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
                speak('opening teams')
                os.system(path)
            elif 'camera' in command:
                path = cv2.VideoCapture(0)
                while True:
                    ret, img = path.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                path.release()
                cv2.destroyAllWindows()
            elif 'google' in command:
                speak('opening google')
                webbrowser.open("www.google.com")
                continue
            elif 'geek for geeks' in command:
                speak('opening geek for geeks')
                webbrowser.open("www.geekforgeeks.com")
                continue
            elif 'youtube' in command:
                speak('opening youtube')
                webbrowser.open("www.youtube.com")
                continue
            elif 'google drive' in command:
                speak('opening google drive')
                webbrowser.open("www.drive.google.com")
                continue
            elif 'gmail' in command:
                speak('opening gmail')
                webbrowser.open("www.mail.google.com")
                continue
            elif 'google meet' in command:
                speak('opening google meet')
                webbrowser.open("www.meet.google.com")
                continue
            elif 'google duo' in command:
                speak("opening duo")
                webbrowser.open("www.duo.google.com")
                continue
            elif 'instagram' in command:
                speak('opening instagram')
                webbrowser.open("www.instagram.com")
                continue
            elif 'whatsapp web' in command:
                speak('oening wjhatsapp web')
                webbrowser.open_new_tab("www.web.whatsapp.com")
                continue
            elif 'twitter' in command:
                speak('opeong twitter')
                webbrowser.open("www.twitter.com")
                continue
            elif 'facebook' in command:
                speak('opening facebook')
                webbrowser.open("www.facebook.com")
                continue


        elif 'close' in command:
            if 'notepad' in command:
                speak('closing notepad')
                os.system("taskkill /f /im notepad.exe")
            elif 'command prompt' in command:
                speak('closing command prompt')
                os.system("close sommand prompt")
            elif 'cmd' in command:
                speak('closing cmd')
                os.system("close command prompt")

        elif 'play' in command:
            if 'songs' in command:
                if 'english' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\ENG FAV"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing'+ song)
                    os.startfile(os.path.join(music, rd))
                elif 'downloaded' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Downloaded"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif 'arijit singh' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Arijit Singh"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif 'armaan malik' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Armaan Malik"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif 'favourite' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Favourite"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif "jubin" in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Jubin Nautiyal"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' +  song)
                    os.startfile(os.path.join(music, rd))
                elif "prithvi" in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Pruthvi"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif 'sanam' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Sanam"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))
                elif 'shirley' in command:
                    song = command.replace('play', '')
                    music = "D:\Music\Shirley Setia"
                    songs = os.listdir(music)
                    rd = random.choice(songs)
                    speak('playing' + song)
                    os.startfile(os.path.join(music, rd))

            else:
                song = command.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)

        elif 'ip adress' in command:
            ip = get("https//api.ipify.org").text
            speak(f'your ip adress is {ip}')

        elif 'wikipedia' in command:
            speak('searching in wikipedia')
            person = command.replace('wikipedia', '')
            info = wikipedia.summary(person, 1)
            speak('according to wikipedia ' + info)

        elif 'whatsapp message' in command:
            pywhatkit.sendwhatmsg('+91 8904421907', 'Hello bro.  "this is an auto generated message"', 14, 40)

        elif 'facebook message' in command:
            pyautogui.typewrite('Hello')
            pyautogui.press('enter')

        elif 'email' in command:
            try:
                speak('what should i say')
                content = takecommand().lower()
                to = "yashbhosale1176@gmail.com"
                send_email(to, content)
                speak('Email has been sent')

            except Exception as e:
                print(e)
                speak('sorry, email was not sent')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            speak('current time is' + time)
            print(time)

        elif 'joke' in command:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'switch the window' in command:
            time = 'none'
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'day' in command:
            tellday()

        elif 'what is your name' in command:
            speak('I am Jarvis, your personal assistant')

        elif 'relationship' in command:
            speak('i am in a relationship')

        elif 'single' in command:
            speak('no, i am committed')

        elif 'girlfriend'in command:
            speak('my girlfriend is my girlfriend, she is none of your girlfriends')

        elif 'no thanks' in command:
            speak('thank you for using me. have a great day.')
            print('Thank you for using me. Have a great day.')
            sys.exit()

        elif 'set alarm' in command:
            nn = int(datetime.datetime.now().hour)
            if nn:=22 :
                music = "D:\\Music\\ENG FAV\\All_of_Me_-_John_Legend_(Lyrics)(256k).mp3"
                song = os.listdr(music)
                os.startfile(os.path.join(music,song))

       #elif 'tell me news' in command:
            #speak('please wait, fetching news for you')
            #read_news()

        speak('Do you need anything else?')





if __name__ == "__main__":
    speak('Hello Sir')
    wish()
    takecommand()
    run_jarvis()
