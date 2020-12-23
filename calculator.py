from tkinter import Tk,StringVar,Entry,Button
from math import degrees,radians,exp,asin,acos,floor,pi,e,sin,cos,tan,log,log10,ceil

class calculator:
    def __init__(self):
        window=Tk()
        window.title('Scientific Calculator')
        window.configure(background="white")
        self.string=StringVar()

        entry=Entry(window,textvariable=self.string)
        entry.grid(row=0,column=0,columnspan=8)
        entry.configure(background="white")
        entry.focus()

        icons = ["7","8","9","/","%","clear","AC","4","5","6","*","(",")","pow","1","2","3","-","=",",","0",".","+","sin","asin","cos","acos","tan","atan","min","max","log","abs","floor","ceil","pi","e","log","degrees","radians"]

        entry = Entry(window,textvariable=self.string)
        entry.grid(row=0,column=0,columnspan=8)
        entry.configure(background="white")
        entry.focus()
        
        
