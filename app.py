import sys
import os
import subprocess
import re
import cv2
def get_active_window_title():
    output = subprocess.check_output(["c:/Users/Rohan J Billava/Desktop/fproj/Gesture Recognition-20210208T032343Z-001/Gesture Recognition/app.sh"])
    if output.decode("utf-8") == "Desktop\n":
        return "Desktop"
    else:
        root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
        stdout, stderr = root.communicate()

        m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
        if m != None:
            window_id = m.group(1)
            window = subprocess.Popen(['xprop', '-id', window_id, 'WM_CLASS'], stdout=subprocess.PIPE)
            stdout, stderr = window.communicate()
        else:
            return None

        match = re.match(b'WM_CLASS\(\w+\) = ".*", (?P<name>.+)$', stdout)
        if match != None:
            return match.group("name").strip(b'"')

        return None

if __name__ == "__main__":
				print(get_active_window_title())
#b'Google-chrome'
#b'Google-chrome'
#b'Gnome-terminal
#b'Spotify'
