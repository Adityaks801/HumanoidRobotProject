import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'

import openai
import pyttsx3
import cv2
from object_detection import detect_objects
from gesture_recognition import recognize_gesture
from speech_recognition import MultilingualSpeechRecognition
from response_generation import ResponseGeneration


def speak_response(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()


def main():
    openai_api_key = 'your_openai_api_key_here'  # Set your OpenAI API key
    response_generator = ResponseGeneration(openai_api_key)
    speech_recognition = MultilingualSpeechRecognition()

    # For object detection and gesture recognition, using a webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Listen and Translate Speech
        translated_text = speech_recognition.listen_and_translate()
        print(f"User asked: {translated_text}")

        if translated_text.lower() in ["quit", "exit", "stop"]:
            print("[INFO] Exiting...")
            break

        # Get AI Response (using GPT-3)
        response = response_generator.generate_response(translated_text)
        print(f"AI Response: {response}")

        # Speak the AI response
        speak_response(response)

        # For Object Detection and Gesture Recognition
        ret, frame = cap.read()

        if not ret:
            print("[ERROR] Failed to grab frame")
            break

        # Perform Object Detection
        detected_frame = detect_objects(frame)
        cv2.imshow("Object Detection", detected_frame)

        # Perform Gesture Recognition
        gesture_frame = recognize_gesture(frame)
        cv2.imshow("Gesture Recognition", gesture_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
