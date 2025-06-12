import pyttsx3 as p
import speech_recognition as sr
#import randfacts
from weather import *
import datetime
#from jokes import *
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
todat_date = datetime.datetime.now()
def speak(text):
    engine.say(text)
    engine.runAndWait()
r = sr.Recognizer()
speak("Hello, I am your personal voice assistant. the temperature is "+str(temp())+"degrees celcius and the weather is "+str(des()))
speak("today is "+todat_date.strftime("%d")+" of "+todat_date.strftime("%B")+" and its currently "+todat_date.strftime("%I")+" "+todat_date.strftime("%M")+" "+todat_date.strftime("%p"))
speak("How are you on this fine Day")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am also having a good day")
speak("what can I do for you today")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    from seleniumweb import infow
    assist = infow()
    assist.getinfo(infor)
elif "play" and "video" in text2:
    speak("Which video do you want me to play?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    from ut_script import music
    assist = music()
    assist.play(vid)
elif "news" in text2:
    from news import *
    arr = news()
    speak("sure sir")
    for i in range(len(arr)):
        speak(arr[i])
        print(arr[i])
'''elif "fact" or "facts" in text2:
    speak("Sure")
    x = randfacts.getFact()
    print(x)
    speak("Did you know that "+x)
elif "temperature" or "weather" in text2:
    t = temp()
    print(t)
    speak("The temperature is "+str(t)+" degrees celsius")
    w = des()
    print(w)
    speak("The weather is "+str(w))'''

