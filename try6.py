import cv2
import numpy as np
import mediapipe as mp
import pyautogui as pg
from time import sleep

def count(lst):
    cnt = 0
    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:    
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh: 
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh: 
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh: 
        cnt += 1

    if (lst.landmark[5].y*100 - lst.landmark[4].y*100) > thresh:
        cnt += 1

    return cnt

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
mphand = mp.solutions.hands
hand = mphand.Hands(False,2,1,0.8,0.5)
mpdraw = mp.solutions.drawing_utils

while cap.isOpened():
    succ,frame = cap.read()
    imgres = cv2.resize(frame,(1280,720))
    imgres = cv2.flip(imgres, 1)
    img = cv2.cvtColor(imgres,cv2.COLOR_BGR2RGB)
    result = hand.process(img)
    lmlist1 = []
    lmlist2 = []

    if result.multi_hand_landmarks and len(result.multi_hand_landmarks) == 2:
        landmarks_for_left_hand = result.multi_hand_landmarks[0]
        landmarks_for_right_hand = result.multi_hand_landmarks[1]
        h,w,c = img.shape
        startX = 0
        for id1, lm1 in enumerate(landmarks_for_left_hand.landmark):
            
            cx1 , cy1= int(lm1.x*w),int(lm1.y*h)
            lmlist1.append([id1,cx1,cy1])

        for id2, lm2 in enumerate(landmarks_for_right_hand.landmark):
            cx2 , cy2= int(lm2.x*w),int(lm2.y*h)
            lmlist2.append([id2,cx2,cy2])

        
        
        mpdraw.draw_landmarks(imgres, landmarks_for_left_hand, mphand.HAND_CONNECTIONS)
        mpdraw.draw_landmarks(imgres, landmarks_for_right_hand, mphand.HAND_CONNECTIONS)

    if lmlist1 and lmlist2:
        cnt1 = count(landmarks_for_left_hand)
        cnt2 = count(landmarks_for_right_hand)

        if cnt1 == 1:
            pg.press("w")
            sleep(0.2)
        if cnt1 == 2:
            pg.press("s")
            sleep(0.2)
        if cnt1 == 3:
            pg.press("e")
            sleep(0.2)
        if cnt1 == 4:
            pg.press("d")
            sleep(0.2)

        if cnt2 == 1:
            pg.press("z")
            sleep(0.2)
        if cnt2 == 2:
            pg.press("x")
            sleep(0.2)
        if cnt2 == 3:
            pg.press("c")
            sleep(0.2)
        if cnt2 == 4:
            pg.press("v")
            sleep(0.2)
    
    
    cv2.imshow("vid",imgres)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
