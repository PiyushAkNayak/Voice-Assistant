import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
    with open("Alarmtext.txt", "r") as file:
        alarm_time = file.read().strip()
except FileNotFoundError:
    speak("Sorry, the alarm file is not found.")
    exit()
except Exception as e:
    speak(f"An error occurred: {str(e)}")
    exit()

try:
    alarm_time_obj = datetime.datetime.strptime(alarm_time, "%I:%M %p")
    alarm_time = alarm_time_obj.strftime("%H:%M")
except ValueError:
    speak("Invalid time format in the alarm file.")
    exit()

try:
    with open("Alarmtext.txt", "w") as file:
        file.write("")
except Exception as e:
    speak(f"Error clearing the alarm file: {str(e)}")
    exit()

def ring(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak("Alarm ringing, sir")
            os.startfile("music.mp3")
            break

ring(alarm_time)