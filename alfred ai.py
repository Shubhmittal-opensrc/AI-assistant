import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
         speak("Good Evening")
    speak("hi , i am your personal assistant, how may i help you sir")

def takecommand(): #it is just using microphone and converting that phrase into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1 #seconds of non speaking audio before the phrase is completed so that it does not quit at the pause
        audio = r.listen(source)
    try: #we use this when we feel that the possibility of error is high
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please......")
        return "None" #if problem occurs none string occurs
    return query

if __name__ == '__main__':
    wishMe()
    query = takecommand().lower()#converting voice into lower language so that we can perform logical operations

    if 'wikipedia' in query:
        speak('searching Wikipedia.........')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query , sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")

    elif'play music' in query:
        music_dir = 'D:\\Songs'
        songs = os.listdir(music_dir)
        print (songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
       strTime = datetime.datetime.now().strftime("%H:%M:%S")
       speak(f"sir, the time is {strTime}")

