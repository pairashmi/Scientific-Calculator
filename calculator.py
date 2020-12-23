from tkinter import Tk
from tkinter import StringVar,Entry,Button
from math import pi,e,sin,cos,tan,log,log10,ceil,degrees,radians,exp,asin,acos,floor


class calculator:
    def __init__(self):
        window=Tk()
        window.title('Scientific Calculator')
        window.configure(background="white")
        self.string=StringVar()

        entry=Entry(window,textvariable=self.string)
        entry.grid(row=0,column=1,columnspan=6)
        entry.configure(background="white")
        entry.focus()
