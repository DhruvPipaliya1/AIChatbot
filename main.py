import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import subprocess
import os
import time

recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "open project" in c.lower():
        speak("Starting your Laravel project")

        # ✅ Start Apache and MySQL using XAMPP batch files
        subprocess.Popen(r"C:\xampp\apache_start.bat")
        subprocess.Popen(r"C:\xampp\mysql_start.bat")
        speak("Starting Apache and MySQL...")

        time.sleep(5)  # wait for servers to start

        # ✅ Run php artisan serve in your Laravel project directory
        project_path = r"C:\Users\HP\Downloads\Flex_Home_v2.55.2_Nulled\Flex Home v2.55.2 Nulled\codecanyon-25197385-flex-home-laravel-real-estate-multilingual-system"  # Change this
        command = f'start cmd /K "cd /d {project_path} && php artisan serve"'
        os.system(command)

        speak("Opening your Laravel project in browser")
        time.sleep(5)
        webbrowser.open("http://localhost:8000")

if __name__ == "__main__":
    speak("Intializing jarvis....")
    while True:
        r = sr.Recognizer()
        

        print("Recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listning....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("jarvis active..")
                    audio = r.listen(source)
                    command =  r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

