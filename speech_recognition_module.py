import speech_recognition as sr
from googletrans import Translator


class MultilingualSpeechRecognition:
    def __init__(self):
        print("[INFO] Initializing Multilingual Speech Recognition...")
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.translator = Translator()  # Google Translator for language translation

    def listen_and_translate(self):
        print("[INFO] Adjusting microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("[INFO] Listening for speech. Speak into the microphone...")

            while True:
                try:
                    print("[INFO] Say something...")
                    audio = self.recognizer.listen(source)  # Listen for input
                    detected_text = self.recognizer.recognize_google(audio)  # Recognize speech

                    # Detect language of the input text
                    detected_language = self.translator.detect(detected_text).lang
                    print(f"[DETECTED LANGUAGE]: {detected_language}")
                    print(f"[USER SAID]: {detected_text}")

                    # Translate input to English
                    translated_text = self.translator.translate(detected_text, src=detected_language, dest="en").text
                    print(f"[TRANSLATED TO ENGLISH]: {translated_text}")

                    return translated_text  # Return the translated text

                except sr.UnknownValueError:
                    print("[WARNING] Could not understand the audio. Please try again.")
                except sr.RequestError as e:
                    print(f"[ERROR] Speech recognition service failed: {e}")
                    break
