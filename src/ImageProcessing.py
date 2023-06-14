import cv2
import pytesseract

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera, or specify the camera index

while True:
    # Capture frame-by-frame from the camera
    ret, frame = camera.read()

    # Convert the captured frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR using Tesseract
    serial_number = pytesseract.image_to_string(gray)

    # Print the recognized serial number
    print("Serial Number:", serial_number)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
