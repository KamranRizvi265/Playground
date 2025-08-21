import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How may I assist you today?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in" )
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None

    return query

def main():
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    wishMe()
    query = listen()

    try:
        if 'search' in query.lower():
            speak("Searching Wikipedia...")
            query = query.replace("search", "")
            summary = wikipedia.summary(query, sentences=2)
            print(summary)
            speak(summary)

        elif 'open youtube' in query.lower():
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query.lower():
            webbrowser.open("https://www.google.com")

        elif 'open stack overflow' in query.lower():
            webbrowser.open("https://stackoverflow.com")

        elif 'open github' in query.lower():
            webbrowser.open("https://github.com")
            
    except Exception as e:
        print("An error occurred:", e)
        speak("I am sorry, I could not process your request.")

if __name__ == "__main__":
    main()
    