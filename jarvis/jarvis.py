import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import wolframalpha
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',168)
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',25)
    server.ehlo()
    server.starttls()
    server.login('UR_ID_@gmail.com','ur_password')
    server.sendmail('UR_ID_@gmail.com',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=5 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Aternoon!")
    
    else:
        speak("Good Evening!")

    speak("this is your.. Assistant,how may i help you?")

def takeCommand(): 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n ")


    except Exception as e:
        # print(e)    
        print("say that again")
        speak("say that again")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while(True):
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipdia')
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('opening youtube..')
            urL='https://www.youtube.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'google' in query:
            speak('opening google..')
            urL='https://www.google.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'microsoft' in query:
            speak('opening microsoft..')
            urL='https://www.microsoft.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif '18 plus' in query:
            speak('opening porn..')
            url = 'www.tiava.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new(url)

        elif 'stack overflow' in query:
            speak('opening stack overflow..')
            urL='https://www.stackoverflow.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
            
        elif 'facebook' in query:
            speak('opening facebook..')
            urL='https://www.facebook.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'instagram' in query:
            speak('opening instagram..')
            urL='https://www.instagram.com'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'telegram' in query:
            speak('opening telegram..')
            urL='https://webk.telegram.org/'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'olx' in query:
            speak('opening olx..')
            urL='https://www.olx.com/'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'flipkart' in query:
            speak('opening flipkart..')
            urL='https://www.flipkart.com/'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'amazon' in query:
            speak('opening amazon..')
            urL='https://www.amazon.com/'
            chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'music' in query:
            music_dir='C:\\Users\\safora\\Desktop\\html\\music'
            songs=os.listdir(music_dir)
            print(songs)
            randNo=random.randint(0,8)
            os.startfile(os.path.join(music_dir,songs[randNo]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir,the time is {strtime}")

        elif 'code' in query:
            speak('opening v s code editor..')
            codepath='C:\\Users\\safora\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)
        
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me zeera")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by god.")

        elif "who am i" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to omer. further It's a secret")
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif 'exit' in query:
            speak('bye,see u later')
            exit()

        elif 'what is' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif'send email' in query:
            try:
                speak('what should i say?')
                content=takeCommand()
                to='recv_ID_@gmail.com'
                sendEmail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)    
                speak('sorry boss ,i am unable to send this mail')


# https://www.geeksforgeeks.org/voice-assistant-using-python/