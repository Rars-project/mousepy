import cv2
import numpy as np
import pyautogui
from gmouse import gmouse
from aimouse import aimouse
import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

def callback(url):
    webbrowser.open_new(url)

# def manual():
#     control_mouse("manual")

# def automatic():
#     control_mouse("automatic")

root = tk.Tk()
root.title('TALK IS CHEAP.SHOW ME THE CODE MF')
root.geometry("590x500+50+50")
root.resizable(False,False)

image = ImageTk.PhotoImage(Image.open("tap.png"))
img_label = tk.Label(image=image)
img_label.grid(row=0, columnspan=2, pady=10)

label = tk.Label(root, text="Welcome to Virtual Mouse", font='system 18 bold')
label.grid(row=1, columnspan=2, pady=5)

button = tk.Button(root, text="Gesture based interaction",fg="green", font='TkDefaultFont 12 bold', command=gmouse, height="3",width="20")
button.grid(row=2, column=0, pady=20, padx=10)


button = tk.Button(root,text="AI virtual mouse",fg="green", font='TkDefaultFontTkDefaultFont 12 bold', command=aimouse, height="3",width="16")
button.grid(row=2, column=1, pady=20)

# button = tk.Button(root,text="Draw in Air",fg="green", font='TkDefaultFont 12 bold', command=draw_in_air, height="4", width="16")
# button.grid(row=3, column=0, pady=20)

button = tk.Button(root,text="Close",fg="red", font='TkDefaultFont 12 bold', command=root.quit, height="3", width="16")
button.grid(row=3, columnspan=2)

link1 = tk.Label(root, text="How to use?", fg="blue", cursor="hand2", font='TkDefaultFont 12 bold',height="3")
link1.grid(rows=4, columnspan=2)
link1.bind("<Button-1>", lambda e: callback("about.html"))
root.attributes('-alpha',0.8)

root.mainloop()


