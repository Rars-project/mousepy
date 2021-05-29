# import sys
# import os
# import subprocess
# import re
# import cv2
import pyautogui
import autopy
import cv2
import numpy as np
import HandTrackingModule as htm
import time


def get_active_window_title():
    #time.sleep(5)
    output = pyautogui.getActiveWindow().title 
    #print(output)
    #subprocess.check_output(["c:/Users/Rohan J Billava/Desktop/fproj/Gesture Recognition-20210208T032343Z-001/Gesture Recognition/app.sh"])
    if len(output)==0:
        return "Desktop"
    elif "-" in output:
        x=output.rfind("-")
        return output[x+2:]
    elif "C:" in output:  #to extract title of file explorer
        return "File Explorer"
    else:
        return output
#     if  "Desktop" in output:
#         return "Desktop"
#     else:
        # root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
        # stdout, stderr = root.communicate()

        # m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
        # if m != None:
        #     window_id = m.group(1)
        #     window = subprocess.Popen(['xprop', '-id', window_id, 'WM_CLASS'], stdout=subprocess.PIPE)
        #     stdout, stderr = window.communicate()
        # else:
        #     return None

        # match = re.match(b'WM_CLASS\(\w+\) = ".*", (?P<name>.+)$', stdout)
        # if match != None:
        #     return match.group("name").strip(b'"')

        # return 
#trcking variable 
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
frameR=100

def track(success, img,wCam, hCam,smooth):
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0
         # 1. Find hand Landmarks
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
            if fingers[1] == 1 and fingers[2] == 0:
                # 5. Convert Coordinates
                x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                # 6. Smoothen Values
                clocX = plocX + (x3 - plocX) / smooth
                clocY = plocY + (y3 - plocY) / smooth

                # 7. Move Mouse
                autopy.mouse.move(wScr-clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            # 8. Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:
                # 9. Find distance between fingers
                length, img, lineInfo = detector.findDistance(8, 12, img)
                print(length)
                # 10. Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                            15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()


if __name__ == "__main__":
				print(get_active_window_title())
#b'Google-chrome'
#b'Google-chrome'
#b'Gnome-terminal
#b'Spotify'
