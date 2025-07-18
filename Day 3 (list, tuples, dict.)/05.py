import cowsay

message=input("Enter your Message: ")
cowsay.meow(message)

import pyttsx3

engine=pyttsx3.init()
engine.say(message)
engine.runAndWait()