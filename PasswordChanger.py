from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

class ChangePasswordClass:
    def __init__(self,p_window):
        self.window  = Toplevel(p_window)
        self.window.title("Change Password")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = w-100
        h1 = h-150
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))
        self.window.state('zoomed')
        font1 = ("Anton" , 20,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="Change Password",background=color2,foreground='white',font=('Clarendon Lt BT',40,'bold'),borderwidth=7,relief='flat')
        self.L1 = Label(self.window,text="Name",background=color1,font=font1)
        self.L1 = Label(self.window,text="Current Password",background=color1,font=font1)
        self.L2 = Label(self.window,text="New Password",background=color1,font=font1)
        self.L3 = Label(self.window,text="Confirm Password",background=color1,font=font1)

        self.t0 = Entry(self.window,font=font1)
        self.t1 = Entry(self.window,font=font1,show='*')
        self.t2 = Entry(self.window,font=font1,show='*')
        self.t3 = Entry(self.window,font=font1,show='*')

        cb1=Checkbutton(self.window,text="Show Password",command=self.showpswd1)
        cb1.place(x=1250,y=305)
        cb2=Checkbutton(self.window,text="Show Password",command=self.showpswd2)
        cb2.place(x=1250,y=405)
        cb3=Checkbutton(self.window,text="Show Password",command=self.showpswd3)
        cb3.place(x=1250,y=505)

        self.b1 = Button(self.window,text="Change",background=color2,foreground='white',font=font1,command=self.changeData)

        self.hdlbl.place(x=0,y=0,width=w,height=80)
        x1=50
        y1=100
        x_diff=190
        y_diff=50

        self.L1.place(x=600,y=300)
        self.t1.place(x=900,y=300)

        y1+=y_diff
        self.L2.place(x=600,y=400)
        self.t2.place(x=900,y=400)

        y1+=y_diff
        self.L3.place(x=600,y=500)
        self.t3.place(x=900,y=500)

        y1+=y_diff
        self.b1.place(x=950,y=600,width=150,height=40)
        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)

    def showpswd1(self):
        if self.t1.cget("show")=="*":
            self.t1.config(show="")
        else:
            self.t2.config(show="*")
    def showpswd2(self):
        if self.t2.cget("show")=="*":
            self.t2.config(show="")
        else:
            self.t2.config(show="*")
    def showpswd3(self):
        if self.t3.cget("show")=="*":
            self.t3.config(show="")
        else:
            self.t3.config(show="*")

    def changeData(self):
        if self.t2.get()!=self.t3.get():
            messagebox.showwarning("Failure","Please Check password ",parent=self.window)
            return
        try:
            qry = " update userdata set Password=%s where Password=%s"
            rowcount = self.curr.execute(qry , (self.t2.get(),self.t1.get()))
            self.connection.commit()
            
            if rowcount==1:
                messagebox.showinfo("Success","User Data Updated Successfully",parent=self.window)
                self.clearPage()
            else:
                messagebox.showwarning("Failure","Wrong password",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Update Error : \n"+str(e),parent=self.window)
        
    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)

if __name__ == '__main__':
    dummy_pwindow = Tk()
    obj = ChangePasswordClass(dummy_pwindow)
    dummy_pwindow.mainloop()