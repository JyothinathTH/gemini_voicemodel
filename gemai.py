import speech_recognition as sr
import pyttsx3 as ptx
import google.generativeai as genai

genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')
recognizer = sr.Recognizer()
engine = ptx.init()

#setting female voice. If you want a male voice, disable line 11 and line 12
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("Speak something...")
        audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"You said: {text}")
        response = model.generate_content(text)

        # Convert text to speech
        rs = response.text
        rs = rs.replace('*', '') 
        rs = rs.lower()
        engine.say(rs)
        print(response.text)
        engine.runAndWait()
    except sr.UnknownValueError:
        engine.say("Can't Hear")
        print("Could not understand audio")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say("Something error has occurred")
        print(f"Error: {e}")
        engine.runAndWait()
