import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import pyautogui as pg
def aimouse():
    ##########################
    wCam, hCam = 640, 480
    frameR=150 # Frame Reduction
    smoothening = 10
    ########################

    pTime = 0
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(maxHands=1)
    wScr, hScr = autopy.screen.size()
    # print(wScr, hScr)

    while True:
        # 1. Find hand Landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            # print(x1, y1, x2, y2)

            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            # print(fingers)
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                        (255, 0, 255), 2)
            # 4. Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0 and fingers[3] ==0 and fingers[4] == 0 and fingers[0] ==0:######changes#######
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                # 7. Move Mouse
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] ==0 and fingers[4] ==0 and fingers[0] ==0:############changes
                # 9. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)
                print(length)
                # 10. Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                            15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
            ####################### THIS IS FOR RIGHTCLICKING #####################
            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0 and fingers[0] ==0:#############changes
                length1,img1,lineInfo = detector.findDistance(8, 12,img)############changes
                length2,img2,lineInfo = detector.findDistance(12,16,img)############changes
                if length1<40 and length2<40:############changes
                    pg.rightClick()#############changes

            #######################THIS IS FOR SCROLLING #################
            # if fingers[0]== 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3]== 0 and fingers[4] == 0:############changes
            #     length1,img1,lineInfo = detector.findDistance(4, 8,img)############changes
            #     # length2,img2,lineInfo = detector.findDistance(8,12,img)############changes
            #     # length3,img3,lineInfo = detector.findDistance(12, 16,img)############changes
            #     # length4,img4,lineInfo = detector.findDistance(16,20,img)############changes
            #     if length1>180:
            #         print(length1)
            #         print("scrollinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
            #         pg.scroll(-1.5)########changes

            # if fingers[0]== 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3]== 1 and fingers[4] == 1:############changes
            #     pg.scroll(2)########changes


        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        # 12. Display
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return
if __name__ == "__main__":
    aimouse()