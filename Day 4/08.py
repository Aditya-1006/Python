
import wikipedia
import pyttsx3
import cowsay


msg = input("Enter your message: ")

result = wikipedia.summary(msg , sentences=2)

cowsay.tux(result)

engine=pyttsx3.init()

rate = engine.getProperty('rate')                     
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)   

engine.say(result)
engine.runAndWait()




