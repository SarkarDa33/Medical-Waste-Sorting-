from cvzone.ClassificationModule import Classifier
import cv2
from vpython import *
from time import sleep
cap = cv2.VideoCapture(0)
Classifier = Classifier('Resources/keras_model.h5', 'Resources/labels.txt')
myOrb = sphere(color= color.black, radius= 1)
while True:
    _, img = cap.read()
    prediction, indexVal = Classifier.getPrediction(img)
    print(prediction, indexVal)
    if (indexVal == 0):
        myOrb.color = vector(0, 0, 1)
    if (indexVal == 4):
        myOrb.color = vector(0, 0, 1)
    if (indexVal == 1):
        myOrb.color = vector(1, 0, 0)
    if (indexVal == 3):
        myOrb.color = vector(1, 0, 0)
    if (indexVal == 2):
        myOrb.color = vector(0, 0, 0)
    if (indexVal == 5):
        myOrb.color = vector(0, 0, 0)
    sleep(1)

    cv2.imshow("LIVE CLASSIFIER", img)
    cv2.waitKey(1)

