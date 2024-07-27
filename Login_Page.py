from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class LoginClass:
    def __init__(self):
        self.window  = Tk()
        self.window.title("Hotel Manager-Login")
        self.window.configure(background="#81CCFF")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        font1 = ("Anton" , 15,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="Welcome to Hotel Ocean View Manager",background=color2,foreground='white',font=('Anton',30,'bold'),borderwidth=5,relief='flat')
        self.L1 = Label(self.window,text="Username",background=color1,font=font1)
        self.L2 = Label(self.window,text="Password",background=color1,font=font1)

        cb=Checkbutton(self.window,text="Show Password",command=self.showpswd)
        cb.place(x=x1+160,y=y1-70)
        self.t1 = Entry(self.window,font=font1)
        self.t2 = Entry(self.window,font=font1,show='*')

        self.b1 = Button(self.window,text="Login",background=color2,foreground='white',font=font1,command= self.checkData)

        self.hdlbl.place(x=0,y=0,width=w1,height=80)
        x1=w1/2-w1/4
        y1=150
        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1+180,y=y1,width=150,height=40)

        self.databaseConnection()
        self.window.mainloop()

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)
            
    def showpswd(self):
        if self.t2.cget("show")=="*":
            self.t2.config(show="")
        else:
            self.t2.config(show="*")

    def checkData(self):
        try:
            qry = " select * from UserData where Name=%s and Password=%s"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()
            if data:
                un = data[0]
                ut = data[2]
                self.window.destroy()
                from homepage import homepageclass
                homepageclass(un,ut)

            else:
                messagebox.showwarning("Empty","Wrong username or password",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)

if __name__ == '__main__':
    LoginClass()