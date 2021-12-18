# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import cv2
import numpy as np
import pyautogui
import argparse
import imutils
import time
import dlib

def mouseControl():
        ##########################
    wCam, hCam = 640, 480
    frameR = 200  # Frame Reduction # 100
    smoothening = 7  # 7

    pTime = 0
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    #########################
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    # ap.add_argument("-p", "--shape-predictor", required=True,
    # 	help="path to facial landmark predictor")
    ap.add_argument("-r", "--picamera", type=int, default=-1,
                    help="whether or not the Raspberry Pi camera should be used")
    args = vars(ap.parse_args())

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # initialize the video stream and allow the cammera sensor to warmup
    print("[INFO] camera sensor warming up...")
    # vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    time.sleep(2.0)

    # PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe
    pyautogui.FAILSAFE = False

    # get screen dimensions
    wScr, hScr = pyautogui.size()
    time.sleep(1.0)
    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream, resize it to
        # have a maximum width of 400 pixels, and convert it to
        # grayscale
        ret,frame = cap.read()
        # cv2.imshow("", frame)
        # frame = imutils.resize(frame, width=wCam, height=hCam)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ############
        # detect faces in the grayscale frame
        faces = detector(gray, 0)
        # loop over the face detections
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array

        for face in faces:
            # rects[0] first detected face cause 'detector' detect all faces in a frame
            shape = predictor(gray, face)
            shape = face_utils.shape_to_np(shape)

            # get nose coordinates
            nose_x = shape[30][0]
            nose_y = shape[30][1]

            # Convert Coordinates
            x3 = np.interp(nose_x, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(nose_y, (frameR, hCam - frameR), (0, hScr))

            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move Mouse
            pyautogui._mouseMoveDrag("move", wScr - clocX, clocY, 0, 0, 0)
            cv2.putText(frame, "X: {:.2f}".format(wScr - clocX), (20, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.putText(frame, "Y: {:.2f}".format(clocY), (20, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            cv2.circle(frame, (nose_x, nose_y), 3, (255, 0, 0), cv2.FILLED)
            plocX, plocY = clocX, clocY

            # Frame Rate
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, "Frame: {}".format(str(int(fps))),
                        (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display
        # cv2.imshow("Image", frame)
        # key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        # if key == ord("q"):
        #     break

    # do a bit of cleanup
    # cv2.destroyAllWindows()
    


if __name__ == "__main__":
    mouseControl()


