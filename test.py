# # from pyautogui import press, typewrite, hotkey
# # import os
# # hotkey('win','tab')
# # hotkey('winleft')
# # typewrite('chrome\n','0.5')
# # typewrite('www.youtube.com\n','0.2')
# # hotkey('win','e')
# # typewrite('cmd\n')
# # os.system("start chrome")
# import pyautogui
# import time
# # import win32gui
# def get_active_window_title():
#     time.sleep(3)
#     output = pyautogui.getWindowsWithTitle('File Explorer')
#     # w=win32gui
#     # output=w.GetWindowText (w.GetForegroundWindow())
#     # output = pyautogui.getAllTitles()
#     print(output)
# if __name__ == "__main__":
# 				get_active_window_title()
# import sys
# import os
# import subprocess
# import re
# import cv2
import pyautogui
import time
def get_active_window_title():
    time.sleep(5)
    output = pyautogui.getActiveWindow().title 
    print(output)
    #subprocess.check_output(["c:/Users/Rohan J Billava/Desktop/fproj/Gesture Recognition-20210208T032343Z-001/Gesture Recognition/app.sh"])
    if len(output)==0:
        return "Desktop"
    elif "-" in output:
        x=output.rfind("-")
        return output[x+2:]
    elif "C:" in output:
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

        # return None

if __name__ == "__main__":
				print(get_active_window_title())
#b'Google-chrome'
#b'Google-chrome'
#b'Gnome-terminal
#b'Spotify'
