from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 
import pymysql

class Availrooms:
    def __init__(self,hp_window):
        self.window  = Toplevel(hp_window)
        self.window.title("Available Rooms")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = w-100
        h1 = h-150
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))
        self.window.state('zoomed')
        font1 = ("Anton" , 30,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="No. of Booked Rooms by Type",background=color2,foreground='white',font=('Clarendon Lt BT',30,'bold'),borderwidth=5,relief='flat')

        self.L1=Label(self.window,text="Booked Creative Rooms",font=font1,background=color1)
        self.L2=Label(self.window,text="Booked Lodge Rooms",font=font1,background=color1)
        self.L3=Label(self.window,text="Booked Luxury Rooms",font=font1,background=color1)
        self.L7=Label(self.window,text="Total Rooms = 50",font=('Anton' , 30),background=color1)
        self.L8=Label(self.window,text="Total Rooms = 50",font=('Anton' , 30),background=color1)
        self.L9=Label(self.window,text="Total Rooms = 50",font=('Anton' , 30),background=color1)

        f1=open("CreativeRoom.txt",'r')
        c=0
        for line in f1:
            line=line.strip()
            c+=1
        if c==0:
            x=c
        else:
            x=c-1
        self.L4=Label(self.window,text=x,font=font1,background="white",width=20)

        f2=open("LodgeRoom.txt",'r')
        d=0
        for line in f2:
            line=line.strip()
            d+=1
        if d==0:
            y=d
        else:
            y=d-1
        self.L5=Label(self.window,text=y,font=font1,background="white",width=20)

        f3=open("LuxuryRoom.txt",'r')
        e=0
        for line in f3:
            line=line.strip()
            e+=1
        if e==0:
            z=e
        else:
            z=e-1
        self.L6=Label(self.window,text=z,font=font1,background="white",width=20)

        self.hdlbl.place(x=0,y=0,width=w,height=75)
        x1=50
        y1=100
        x_diff=150
        y_diff=50
        
        self.L1.place(x=200,y=250)
        self.L2.place(x=200,y=350)
        self.L3.place(x=200,y=450)

        self.L4.place(x=700,y=250)
        self.L5.place(x=700,y=350)
        self.L6.place(x=700,y=450)

        self.L7.place(x=1300,y=250)
        self.L8.place(x=1300,y=350)
        self.L9.place(x=1300,y=450)

        self.window.mainloop()

if __name__ == '__main__':
    dummy_hpwindow = Tk()
    obj = Availrooms(dummy_hpwindow)
    dummy_hpwindow.mainloop()
