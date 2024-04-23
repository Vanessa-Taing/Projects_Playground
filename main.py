#import openai
#from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser
from transformers import pipeline
#from transformers import AutoModelForCausalLM, AutoTokenizer

#openai.api_key=api_data
#completion=openai.Completion()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello. How Are You? ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("Mojo Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query

def Reply(question):
    text_generator = pipeline("text-generation", model="gpt2")
    generated_text = text_generator(question, max_length=200, num_return_sequences=1)[0]['generated_text']
    return generated_text.strip()

if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print("Jarvis: ", ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            break


