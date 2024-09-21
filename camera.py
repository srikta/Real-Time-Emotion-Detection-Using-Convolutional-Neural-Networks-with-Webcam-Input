import cv2

# Start the webcam feed
cap = cv2.VideoCapture(0)  # 0 refers to the default camera

# Get the default resolution of the camera
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Default Camera Resolution: {int(width)}x{int(height)}")

# Release the camera and close windows
cap.release()
