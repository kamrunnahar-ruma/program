# Computer Vision - CV
import cv2

# Create a VideoCapture object for the default camera (usually 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Display the frame in a window named "output"
    cv2.imshow("output", frame)
    
    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(10) == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
