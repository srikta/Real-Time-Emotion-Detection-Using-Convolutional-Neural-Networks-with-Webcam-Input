import cv2

# Start the webcam feed
cap = cv2.VideoCapture(0)

# Set a resolution you want to test (e.g., 1920x1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Get the actual resolution set by the camera
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Actual Camera Resolution: {int(width)}x{int(height)}")

# Release the camera and close windows
cap.release()
