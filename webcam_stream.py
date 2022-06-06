import cv2
import requests

API_URL = "http://localhost/stream_receiver.php"

# initilize camera
capture = cv2.VideoCapture(0)

try:
    while True:
        # capture frame
        ret, frame = capture.read()

        cv2.imwrite("files/webcam.jpg", frame)

        files = {'frame': ('frame.png', open('files/webcam.jpg', 'rb'))}

        requests.post(API_URL, files=files)

        # display frame
        cv2.imshow("Parking Camera", frame)

except:
    print("Ocorreu um erro.")

finally:
    capture.release()
    print("Execução terminada.")

