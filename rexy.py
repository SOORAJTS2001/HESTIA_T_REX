from itertools import count
import cv2 as cv
from cv2 import FONT_HERSHEY_COMPLEX
import cvzone as cvz
from cv2 import VideoCapture
import mediapipe as mp
import PositionModule as pm
from cvzone.HandTrackingModule import HandDetector
import random,math
tick = cv.imread("tick.png", cv.IMREAD_UNCHANGED)#this is the tick for the correct frame
imgtick = cv.resize(tick, (50, 50), None, 0.3, 0.3)
cross = cv.imread("crs.png", cv.IMREAD_UNCHANGED)#this is the cross for the wrong frame
imgcross = cv.resize(cross, (50, 50), None, 0.3, 0.3)
count = 0
cap = cv.VideoCapture(0)#records video from the camera
handlength =0
hands = []
detector = pm.poseDetector()
hand_detector = HandDetector(detectionCon=0.8, maxHands=1)
imagespos = random.randint(0,2)
while True:
    success, img = cap.read()
    img = cv.flip(img,1)#it is to flip the image
    hands = hand_detector.findHands(img, draw=True,flipType=False)#detects the hand
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if hands: #if there is a hand
        pass
        # if(hands[0]):
        #     print(hands[0])
    if lmList:
        #img pos is the position coordinates of the image as a dictionary with key as name of the image,
        # print(lmList[16])
        # print("angle",angle)
        if lmList[14][1] in range(150,180) and lmList[14][2] in range(300,340):
            img = cvz.overlayPNG(img, imgtick, [400,0])
            angle = detector.findAngle(img, 12, 14, 16, draw=False)
            if(angle<90):
                pass
                # print("up")
            elif(angle>90):
                pass
                # print("down")
            x = abs(lmList[16][1]-171)#this is the x coordinate of the refernce
            y = abs(lmList[16][2]-329)#this is the y coordinate of the reference
            x = x**2
            y = y**2
            d = math.sqrt(x+y)
            # print(d)
            if(d>216):
                val = 0.001548627925746558*(d**2)+(0.09397699757869586*d)-1.3640032284102335
                print("to the left",val)
                # print("to the left")
            elif (d<216):
                val = 0.0011659567527420355*(d**2)-(1.1019051125650066*d)+255.52348954088453
                print("to the right",val)
            else:
                print("not moving")     
        else:
            img = cvz.overlayPNG(img, imgcross, [400,0])#overlays the image
        cv.circle(img, (171, 329), 15, (255, 255, 0), cv.FILLED)
        cv.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 255, 0), cv.FILLED)
        cv.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 255, 0), cv.FILLED)
        cv.circle(img, (lmList[16][1], lmList[16][2]), 15, (0, 255, 0), cv.FILLED)

    # print(angle)
    # fpsReader = cvz.FPS()
    # print(hb,wb)
    # cv.namedWindow("Image", cv.WND_PROP_FULLSCREEN)
    # cv.setWindowProperty("Image", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    # _, imgResult = fpsReader.update(imgResult)
    cv.imshow("Image", img)
    cv.waitKey(1)