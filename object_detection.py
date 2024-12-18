import torch
import cv2

def detect_objects(frame):
    # Load YOLOv5 model (change to "yolov5s" for smaller models)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    # Perform object detection
    results = model(frame)

    # Draw bounding boxes and labels on the frame
    results.render()  # Adds bounding boxes to the frame

    return results.imgs[0]  # Return the image with detected objects

# Usage Example:
# image = cv2.imread('test_image.jpg')
# detected_image = detect_objects(image)
# cv2.imshow('Detected Image', detected_image)
