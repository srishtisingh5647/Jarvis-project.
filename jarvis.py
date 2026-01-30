import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import pyaudio


#pip install pocketsphinx

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        if song in musicLibrary.music:
            say(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            say(f"Sorry, song not found")

    else:
        # Let openAI handle the request
        pass


if __name__ == '__main__':
    print('PyCharm')
    say("Initializing Jarvis...")
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
    r=sr.Recognizer()

    print('Recognizing...')
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source, timeout=2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            say("Ya")
            #Listen for command
            with sr.Microphone() as source:
                print('Jarvis Active...')
