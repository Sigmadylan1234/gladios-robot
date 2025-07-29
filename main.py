import speech_recognition as sr
import pyttsx3
import requests

# GLaDOS voice setup
tts = pyttsx3.init()
tts.setProperty('rate', 150)
tts.setProperty('volume', 1.0)

# Speak aloud
def glados_speak(text):
    print("GLaDOS:", text)
    tts.say(text)
    tts.runAndWait()

# Listen for voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return ""

# Ask the local Ollama AI
def ask_ollama(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": f"You are GLaDOS from Portal. Respond with dark humor and sarcasm.\nUser: {prompt}"
    }, stream=True)

    result = ""
    for line in response.iter_lines():
        if line:
            data = eval(line.decode('utf-8'))
            result += data.get("response", "")
    return result.strip()

# Main loop
while True:
    user_input = listen()
    if not user_input:
        continue
    if "exit" in user_input.lower():
        glados_speak("You can't escape the test that easily.")
        break
    reply = ask_ollama(user_input)
    glados_speak(reply)
