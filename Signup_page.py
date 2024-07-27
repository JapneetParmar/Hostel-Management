from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class SignupClass:
    def __init__(self):
        self.window  = Tk()
        self.window.title("Hotel Manager/Sign up")
        #----------- settings ------------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))
        # ---------- widgets -----------------------
        font1 = ("Anton" , 15,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="User",background=color2,foreground='white',font=('Clarendon Lt BT',30,'bold'),borderwidth=5,relief='flat')
        self.L1 = Label(self.window,text="Username",background=color1,font=font1)
        self.L2 = Label(self.window,text="Password",background=color1,font=font1)
        self.L3 = Label(self.window,text="Usertype",background=color1,font=font1)

        self.t1 = Entry(self.window,font=font1)
        self.t2 = Entry(self.window,font=font1,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,values=("Admin","Employee"), foreground='white',textvariable=self.v1, font=font1)
        self.c1.current(0)

        # -------------------------buttons ----------------------
        self.b1 = Button(self.window,text="Create Account",foreground='white',background=color2,font=font1,command=self.saveData)
        # ------------------placements --------------------

        self.hdlbl.place(x=0,y=0,width=w1,height=80)
        x1=w1/2-w1/4
        y1=100
        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=380,height=40)

        self.databaseConnection()
        self.window.mainloop()

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            qry = " insert into UserData values(%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get(),self.v1.get()))
            self.connection.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User created Successfully",parent=self.window)
                self.window.destroy()
                from Login_Page import LoginClass
                LoginClass()
        except Exception as e:
            messagebox.showerror("Error","Insertion Error : \n"+str(e),parent=self.window)


if __name__ == '__main__':
    SignupClass()