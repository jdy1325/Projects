# Python Project; Facial Regcognition Program
# This program will open a camera feed and detect whether a face is present or if there isn't one present
# Jack Young, Anndrea Chester, and Andrew Skipworth
# 3/18/24

import cv2
import os
import numpy as np

# Document required for opening of Opencv Library
cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_feed = cv2.VideoCapture(0)

# Loop for box around the face that enter the screen
while True:
    # Capture frame-by-frame
    ret, frames = video_feed.read()

    gray_scale = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)  # Sets grayscale

    faces = faceCascade.detectMultiScale(
        gray_scale,
        # Prerequisites for the boxes around faces
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draws a rectangle around recognized faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Colors the frames green

    # Displays resulting frame
    cv2.imshow('Video', frames)

    # Exits the camera and program whenever "q" is entered
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Loop for keeping the frames for the Live Feed
while True:

    ret, image = cap.read()
    image = cv2.flip(image, -1)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray_scale,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        frame_gray = gray[y:y + h, x:x + w]
        frame_color = img[y:y + h, x:x + w]
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff

    if k == 27:  # press 'ESC' to quit
        break

# Closes the feed
video_feed.release()
cv2.destroyAllWindows()