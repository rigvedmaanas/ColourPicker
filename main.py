import tkinter
import customtkinter as win
import pyautogui
import pyperclip
from PIL import Image, ImageGrab, ImageTk

win.set_default_color_theme("dark-blue")
win.set_appearance_mode("dark")

root = win.CTk()
root.geometry("300x150")
root.title("Color Picker")
display = win.CTkFrame(root, width=100, height=100)
display.place(relx=0.1, rely=0.15)

switch_var = tkinter.StringVar()
switch_var.set("hex")

pixelValue = ""

switch = win.CTkSwitch(root, text="RGB", variable=switch_var, onvalue="rgb", offvalue="hex")
switch.place(relx=0.7, rely=0.5)
lbl = win.CTkLabel(root, text="HEX", width=10)
lbl.place(relx=0.55, rely=0.485)
def takeScreenShot():
    global pixelValue
    img = ImageGrab.grab(bbox=None)
    mousePos = pyautogui.position()
    pixelValue = img.getpixel((mousePos[0], mousePos[1]))
    pixelValue = (pixelValue[0], pixelValue[1], pixelValue[2])
    display.config(fg_color = "#" + '%02x%02x%02x' % pixelValue)
    root.after(10, takeScreenShot)


def copyText(e):
    if switch.get() == "hex":
        pyperclip.copy("#" + '%02x%02x%02x' % pixelValue)
    if switch.get() == "rgb":
        pyperclip.copy(f"{str(pixelValue[0])},{str(pixelValue[1])},{str(pixelValue[2])}")

root.after(10, takeScreenShot)
root.bind("c", copyText)
root.mainloop()