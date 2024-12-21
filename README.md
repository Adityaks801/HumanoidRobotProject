Multilingual Speech Recognition, Object Detection, and Gesture Recognition System


This project combines multilingual speech recognition, object detection using YOLOv5, and gesture recognition with MediaPipe into a cohesive AI-powered system. Additionally, it uses OpenAI's GPT-3 to generate intelligent responses based on user inputs and outputs responses audibly.
Features

Multilingual Speech Recognition:

Detects and recognizes speech in multiple languages.
Automatically translates speech into English for processing.
Generates and speaks back AI-powered responses.

Object Detection:

Real-time detection of objects using the YOLOv5 model.
Visualizes detected objects with bounding boxes and labels.

Gesture Recognition:

Detects and tracks hand gestures using MediaPipe.
Visualizes hand landmarks and provides gesture-based interactions.

AI-Powered Responses:

Uses OpenAI GPT-3 to interpret queries and generate contextual responses.
Responds audibly to user questions and commands.

GPU Support:

Optimized to leverage GPU for real-time performance in object detection and AI response generation.


System Requirements

Python 3.9
GPU-enabled system (optional but recommended)
Libraries: torch, opencv-python, mediapipe, speechrecognition, googletrans, pyttsx3, openai


Setup Instructions
1. Create Python 3.9 Virtual Environment
bash\

python -m venv project_env
project_env\Scripts\activate     # For Windows

3. Install Dependencies
Install the required libraries:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  # For GPU support
pip install opencv-python mediapipe speechrecognition googletrans==4.0.0-rc1 pyttsx3 openai

3. Set Up YOLOv5
Clone YOLOv5 repository:git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

5. Configure OpenAI API
Set your OpenAI API key as an environment variable:

bash
Copy code
export OPENAI_API_KEY='your_openai_api_key'  # For Linux/Mac
set OPENAI_API_KEY=your_openai_api_key       # For Windows
5. Run the Project



Usage
Start the system by running main.py.
Speak into the microphone for speech recognition.
Switch between object detection and gesture recognition using keyboard inputs.
Receive AI-powered audible responses to your queries.


Troubleshooting
Webcam Issues: Ensure your webcam is connected and accessible. Update OpenCV if the issue persists.
GPU Support: Verify CUDA installation and use compatible PyTorch versions for GPU acceleration.
Speech Recognition Failures: Check your microphone settings and ensure a stable internet connection for Google Speech Recognition.
Future Enhancements
Improved natural language understanding for complex queries.
Integration of gesture-based command execution.
Further optimization for real-time performance.
Acknowledgments
This project utilizes:

YOLOv5 by Ultralytics
MediaPipe
OpenAI API
