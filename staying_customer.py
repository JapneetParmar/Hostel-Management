from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

class stayingcustomersclass():
    def __init__(self,pwindow):
        self.window  = Toplevel(pwindow)
        self.window.title("Residing Guests")
        self.window.configure(background="#81CCFF")

        #************Window Settings***************
        W=self.window.winfo_screenwidth()
        H=self.window.winfo_screenheight()
        w0=W-200
        h0=H-200
        #self.window.minsize(w0,h0)
        self.window.geometry("%dx%d+%d+%d"%(w0,h0,50,50))
        self.window.state('zoomed')

        #*********** Main UI*******************
        font1=("Anton",20)
        color1="#F03838"
        self.MHD=Label(self.window,text="Customers Record",font=("Franklin Gothic Medium",50,"bold"),background="#F03838",foreground="white",relief=FLAT)
        self.L0=Label(self.window,text="Name",font=font1,background=color1)
        self.L1=Label(self.window,text="Mobile",font=font1,background=color1)
        self.L2=Label(self.window,text="E-Mail",font=font1,background=color1)
        self.L3=Label(self.window,text="Gender",font=font1,background=color1)
        self.L4=Label(self.window,text="Number of Members",font=font1,background=color1)
        self.L5=Label(self.window,text="Check in Date",font=font1,background=color1)
        self.L6=Label(self.window,text="Check out Date",font=font1,background=color1)
        self.L7=Label(self.window,text="Type of room",font=font1,background=color1)
        self.L8=Label(self.window, text="Allotted Room no", font=font1, background=color1)

        #*****************StayingCustomers****************
        self.table = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9'],height=40)

        self.table.heading('c1',text="Name")
        self.table.heading('c2',text="Mobile")
        self.table.heading('c3',text="E-Mail")
        self.table.heading('c4',text="Gender")
        self.table.heading('c5',text="No. of Guests")
        self.table.heading('c6',text="Check in")
        self.table.heading('c7',text="Check Out")
        self.table.heading('c8',text="Room Type")
        self.table.heading('c9',text="Allotted Room no")

        self.table['show']='headings'

        self.table.column('c1',width=200,anchor='center')
        self.table.column('c2',width=200,anchor='center')
        self.table.column('c3',width=200,anchor='center')
        self.table.column('c4',width=150,anchor='center')
        self.table.column('c5',width=150,anchor='center')
        self.table.column('c6',width=200,anchor='center')
        self.table.column('c7',width=175,anchor='center')
        self.table.column('c8',width=175,anchor='center')
        self.table.column('c9',width=175,anchor='center')

        self.MHD.place(x=0,y=0,width=W,height=90)
        self.databaseConnection()
        self.getdata()
        self.table.place(x=150,y=125)
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)
 
    def getdata(self):
        try:
            qry = " select * from newcustomers"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            if data:
                for row in data:
                    self.table.insert("",END,values=row)
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummy_pwindow = Tk()
    obj = stayingcustomersclass(dummy_pwindow)
    dummy_pwindow.mainloop()