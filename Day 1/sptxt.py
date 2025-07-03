message = input("Enter Your Message: ")

import pyttsx3
engine = pyttsx3.init()
engine.say(message)
engine.runAndWait()