import cv2
import numpy as np
from pyautogui import hotkey
from gmouse import gmouse
from aimouse import aimouse
import tkinter as tk
# from PIL import ImageTk, Image
import webbrowser
from tkinter import *
def pressq():
    hotkey('q')

def hover(button,coloronhover,coloronleave):
    button.bind("<Enter>",func=lambda e:button.config(background=coloronhover))
    button.bind("<Leave>",func=lambda e:button.config(background=coloronleave))


def callback(url):
    webbrowser.open_new(url)
    
root = tk.Tk()
root.title('TALK IS CHEAP.SHOW ME THE CODE MF')
root.geometry("680x500+50+50")
root.resizable(False,False)
# root.wm_attributes('-transparentcolor',"#b3d9ff")

bg=PhotoImage(file="images/img1.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

image = PhotoImage(file="tap.png")
img_label = tk.Label(image=image)
img_label.grid(row=0, columnspan=2, pady=10)

label = tk.Label(root, text="Welcome to Virtual Mouse", font='system 18 bold',bg="#a6a6a6")
label.grid(row=1, columnspan=2, pady=5)

button = tk.Button(root, text="Gesture based interaction",fg="black", font='TkDefaultFont 12 bold', command=gmouse, height="2",width="20",bg="#ff9900",borderwidth=10)
button.grid(row=2, column=0, pady=20, padx=10)
hover(button,"grey","#ff9900")


button = tk.Button(root,text="AI virtual mouse",fg="black", font='TkDefaultFontTkDefaultFont 12 bold', command=aimouse, height="2",width="20",bg="#ff9900",borderwidth=10)
button.grid(row=2, column=1, pady=20)
hover(button,"grey","#ff9900")

# button = tk.Button(root,text="Stop",fg="green", font='TkDefaultFont 12 bold', command=pressq, height="1",width="10",bg="#ff9900",borderwidth=10)
# button.grid(row=3, column=0, pady=20)

button = tk.Button(root,text="Close",fg="black", font='TkDefaultFont 12 bold', command=root.quit, height="1", width="10",bg="#bfff00",borderwidth=10)
button.grid(row=3, columnspan=2,pady=20)
hover(button,"#ff9900","#bfff00")

link1 = tk.Label(root, text="How to use?", fg="blue",bg="#a6a6a6", cursor="hand2", font='TkDefaultFont 12 bold',height="2",width="10",borderwidth=10)
link1.grid(rows=5, columnspan=2)
link1.bind("<Button-1>", lambda e: callback("about.html"))
root.attributes('-alpha',1.0)

root.mainloop()


