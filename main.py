try:
    import cv2
    import speech_recognition as sr
    import pyttsx3
    import requests

    # Camera stream setup
    url = "http://user:1234@192.168.1.116/mjpg/1/video.mjpg?camera=1&timestamp=1753839334186"
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("❌ Could not open camera stream.")
    else:
        print("📷 Camera stream opened successfully.")

    # Text-to-speech setup
    tts = pyttsx3.init()
    tts.setProperty('rate', 150)
    tts.setProperty('volume', 1.0)

    def glados_speak(text):
        print("GLaDOS:", text)
        tts.say(text)
        tts.runAndWait()

    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = r.listen(source)
            return r.recognize_google(audio)

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

    while True:
        # Show camera if available
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow("GLaDOS Camera View", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # Listen and respond
        try:
            user_input = listen()
            if "exit" in user_input.lower():
                glados_speak("You can't escape the test that easily.")
                break
            reply = ask_ollama(user_input)
            glados_speak(reply)
        except Exception as mic_err:
            glados_speak("Microphone error. I blame the humans.")
            print("⚠️ Microphone error:", mic_err)

    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print("❌ ERROR:", e)
    input("Press Enter to close...")
