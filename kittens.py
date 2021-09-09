#!/usr/bin/env python3
from tkinter import Tk, Canvas, NW
from PIL import ImageTk

win = Tk()

photoimage = ImageTk.PhotoImage(file="kit4.png")

width, height = photoimage.width(), photoimage.height()
canvas = Canvas(win, bg="black", width=width, height=height)
canvas.pack()

canvas.create_image(0, 0, image=photoimage, anchor=NW)

win.mainloop()