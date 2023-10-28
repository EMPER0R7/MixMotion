import cv2
import numpy as np
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
mphand = mp.solutions.hands
hand = mphand.Hands(False,2,1,0.8,0.5)
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
    imgres = cv2.flip(imgres, 1)
    img = cv2.cvtColor(imgres,cv2.COLOR_BGR2RGB)
    result = hand.process(img)
    lmlist = []

    cv2.rectangle(imgres,(980,200),(1140,520),(91,64,28),cv2.FILLED)
    
    if result.multi_hand_landmarks:
        for landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            for id,lm in enumerate(landmarks.landmark):
                h,w,c = imgres.shape
                cx , cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
            
            mpdraw.draw_landmarks(imgres,landmarks,mphand.HAND_CONNECTIONS)

            # Classifying left and right hands
            classification = handedness.classification[0].label

            if classification == "Left":
                landmarks_for_left_hand = landmarks
            elif classification == "Right":
                landmarks_for_right_hand = landmarks
            
            # Enter in screen with left hand (imp)

            # Get the coordinates of specific landmarks (e.g., thumb, index, and wrist)
            thumb_base = landmarks_for_left_hand.landmark[mphand.HandLandmark.THUMB_MCP]
            thumb_mid = landmarks_for_left_hand.landmark[mphand.HandLandmark.THUMB_IP]
            thumb_tip = landmarks_for_left_hand.landmark[mphand.HandLandmark.THUMB_TIP]
            ring_tip = landmarks_for_left_hand.landmark[mphand.HandLandmark.RING_FINGER_TIP]
            ring_mid = landmarks_for_left_hand.landmark[mphand.HandLandmark.RING_FINGER_DIP]
            middle_finger = landmarks_for_left_hand.landmark[mphand.HandLandmark.MIDDLE_FINGER_TIP]
            index_finger = landmarks_for_left_hand.landmark[mphand.HandLandmark.INDEX_FINGER_TIP]
            ring_finger = landmarks_for_left_hand.landmark[mphand.HandLandmark.RING_FINGER_TIP]
            pinky_finger = landmarks_for_left_hand.landmark[mphand.HandLandmark.PINKY_TIP]
            pinky_base = landmarks_for_left_hand.landmark[mphand.HandLandmark.PINKY_MCP]
            pinky_mid = landmarks_for_left_hand.landmark[mphand.HandLandmark.PINKY_PIP]


            # Calc dist bw different fingers to recognize finger gestures  
            max_distance = 0.04
            dist_midTh = abs((middle_finger.y-thumb_base.y)**2 + (middle_finger.x-thumb_base.x)**2)
            dist_thInd = abs((ring_finger.y-thumb_tip.y)**2 + (ring_finger.x-thumb_tip.x)**2)
            dist_thRing = abs((ring_mid.y-thumb_mid.y)**2 + (ring_mid.x-thumb_mid.x)**2)
            dist_indMid = abs((index_finger.y-middle_finger.y)**2 + (index_finger.x-middle_finger.x)**2)
            dist_ringMid = abs((ring_finger.y-middle_finger.y)**2 + (ring_finger.x-middle_finger.x)**2)
            dist_ringPinky = abs((ring_finger.y-pinky_finger.y)**2 + (ring_finger.x-pinky_finger.x)**2)
            dist_pinkbasePinkpip = abs((pinky_base.y-pinky_mid.y)**2 + (pinky_base.x-pinky_mid.x)**2)

            # cv2.rectangle(imgres,(800,100),(900,550),(91,64,28),cv2.FILLED)
            # cv2.rectangle(imgres,(960,100),(1060,550),(91,64,28),cv2.FILLED)
            # cv2.rectangle(imgres,(1120,100),(1220,550),(91,64,28),cv2.FILLED)

            

            # To manipulate volume
            # if len(lmlist)>=12:
            #     x1,y1 = lmlist[8][1],lmlist[8][2]
            #     x2,y2 = lmlist[12][1],lmlist[12][2]
            #     length = np.hypot(x2-x1,y2-y1)
            #     if length<100 and 540<x1<640 and 100<y1<550:
            #         cv2.rectangle(imgres,(640,100),(740,550),(208,58,13),cv2.FILLED)
            #         vol = np.interp(y1,[120,500],[minvol,maxvol])
                
            #         volume.SetMasterVolumeLevel(vol, None)


            # To change bass using pointer
            if dist_midTh < 0.007 and dist_ringMid < 0.007:
                if dist_ringPinky < 0.007 and dist_indMid>0.02:
                    print("Changing bass")
                    if len(lmlist)>=12:
                        x1,y1 = lmlist[8][1],lmlist[8][2]
                        x2,y2 = lmlist[12][1],lmlist[12][2]
                        length = np.hypot(x2-x1,y2-y1)
                        if length<100 and 980<x1<1140 and 200<y1<520:
                            cv2.rectangle(imgres,(980,200),(1140,520),(208,58,13),cv2.FILLED)
                            # Write code for changing base
            
            # To change treble using two fingers touching
            if dist_thRing < 0.01 and dist_ringPinky < 0.01:
                if dist_ringMid > 0.02 and dist_indMid < 0.01:
                    print("Changing treble")
                    if len(lmlist)>=12:
                        x1,y1 = lmlist[8][1],lmlist[8][2]
                        x2,y2 = lmlist[12][1],lmlist[12][2]
                        length = np.hypot(x2-x1,y2-y1)
                        if length<100 and 980<x1<1140 and 200<y1<520:
                            cv2.rectangle(imgres,(980,200),(1140,520),(208,58,13),cv2.FILLED)
                            # Write code for changing base
            
            # To change tempo using thumbs up
            if dist_indMid < 0.01 and dist_ringPinky < 0.01:
                if dist_ringMid < 0.01 and dist_indMid < 0.01:
                    if dist_pinkbasePinkpip < 0.007 and dist_thInd > 0.02:
                        print("Changing tempo")
                        if len(lmlist)>=12:
                            x1,y1 = lmlist[8][1],lmlist[8][2]
                            x2,y2 = lmlist[12][1],lmlist[12][2]
                            length = np.hypot(x2-x1,y2-y1)
                            if length<100 and 980<x1<1140 and 200<y1<520:
                                cv2.rectangle(imgres,(980,200),(1140,520),(208,58,13),cv2.FILLED)
                                # Write code for changing base

            # To change reverb using L
            if dist_indMid > 0.02 and dist_ringPinky < 0.01:
                if dist_ringMid < 0.01 and dist_thInd > 0.02:
                    print("Changing reverb")
                    if len(lmlist)>=12:
                        x1,y1 = lmlist[8][1],lmlist[8][2]
                        x2,y2 = lmlist[12][1],lmlist[12][2]
                        length = np.hypot(x2-x1,y2-y1)
                        if length<100 and 980<x1<1140 and 200<y1<520:
                            cv2.rectangle(imgres,(980,200),(1140,520),(208,58,13),cv2.FILLED)
                            # Write code for changing base

                

    
    
    cv2.imshow("vid",imgres)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()