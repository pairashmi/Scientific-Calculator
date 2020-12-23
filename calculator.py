from tkinter import Tk,StringVar,Entry,Button
from math import degrees,radians,exp,asin,acos,atan,floor,pi,e,sin,cos,tan,log,log10,ceil

class calculator:
    def __init__(self):
        window=Tk()
        window.title('Scientific Calculator')
        window.configure(background="white")
        self.string=StringVar()

        icons = ["7","8","9","/","%","clear","AC","4","5","6","*","(",")","pow","1","2","3","-","=",",","0",".","+","sin","asin","cos","acos","tan","atan","min","max","log","abs","floor","ceil","pi","e","log","degrees","radians"]

        entry = Entry(window,textvariable=self.string)
        entry.grid(row=0,column=0,columnspan=8)
        entry.configure(background="white")
        entry.focus()


        text=1
        i=0
        row=1
        col=0
        for icon in icons:
            padx=10
            pady=10
            if(i==7):
                row=2
                col=0
            if(i==14):
                row=3
                col=0
            if(i==19):
                row=4
                col=0
            if(i==26):
                row=5
                col=0
            if(i==33):
                row=6
                col=0
            if(icon=='='):
                btn=Button(window,height=2,width=4,padx=70,pady=pady,text=icon,command=lambda txt=icon:self.equals())
                btn.grid(row=row,column=col,columnspan=3,padx=2,pady=2)
                btn.configure(background="grey")

            elif(icon=='clear'):
                btn=Button(window,height=2,width=4,padx=padx,pady=pady, text=icon ,command=lambda txt=icon:self.delete())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="grey")
            elif(icon=='AC'):
                btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=icon,command=lambda txt=icon:self.clearall())
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="red")
            else:
                btn=Button(window,height=2,width=4,padx=padx,pady=pady,text=icon ,command=lambda txt=icon:self.addChar(txt))
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="grey")

            col=col+1
            i=i+1
        window.mainloop()


    def clearall(self):
        self.string.set("")

    def equals(self):
        result=""

        try:
            result=eval(self.string.get())
            self.string.set(result)
        except:
            result="INVALID INPUT"
        self.string.set(result)

    def addChar(self,char):
        self.string.set(self.string.get()+(str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

calculator()
