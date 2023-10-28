import cv2
import numpy as np
import mediapipe as mp
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
mphand = mp.solutions.hands
hand = mphand.Hands(False,4,1,0.8,0.5)
mpdraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volran = volume.GetVolumeRange()
minvol = volran[0]
maxvol = volran[1]
vol = 0

while cap.isOpened():
    succ,frame = cap.read()
    imgres = cv2.resize(frame,(1280,720))
    img = cv2.cvtColor(imgres,cv2.COLOR_BGR2RGB)
    result = hand.process(img)
    lmlist = []

    imgres = cv2.flip(imgres, 1)
    if result.multi_hand_landmarks:
        for hands in result.multi_hand_landmarks:
            for id,lm in enumerate(hands.landmark):
                h,w,c = imgres.shape
                cx , cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                
            mpdraw.draw_landmarks(imgres,hands,mphand.HAND_CONNECTIONS)
            
    

    cv2.rectangle(imgres,(640,100),(740,550),(91,64,28),cv2.FILLED)
    

    

    if len(lmlist)>=12:
        x1,y1 = lmlist[8][1],lmlist[8][2]
        x2,y2 = lmlist[12][1],lmlist[12][2]
        length = np.hypot(x2-x1,y2-y1)
        if length<100 and 540<x1<640 and 100<y1<550:
            cv2.rectangle(imgres,(640,100),(740,550),(208,58,13),cv2.FILLED)
            vol = np.interp(y1,[120,500],[minvol,maxvol])
        
            volume.SetMasterVolumeLevel(vol, None)

    
    
    cv2.imshow("vid",imgres)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()