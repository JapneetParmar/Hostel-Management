from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox 
import pymysql
from tkcalendar import DateEntry


class searchguest:
    def __init__(self,hp_window):
        self.window  = Toplevel(hp_window)
        self.window.title("Search Guest")
        #----------- settings ------------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = w-100
        h1 = h-150
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))
        self.window.state('zoomed')
        # ---------- widgets -----------------------
        font1 = ("Anton" , 15,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="Guest By type of room",background=color2,foreground='white',font=('Clarendon Lt BT',30,'bold'),borderwidth=5,relief='flat')

        self.L9=Label(self.window,text="Type of room",font=font1,background=color1)
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=["Luxury Room","Creative Room","Lodge Room"],textvariable=self.v1,state="readonly",width=33,font=("Anton",15))
        self.L9.place(x=20,y=90)
        self.c1.place(x=200,y=90,height=30)



        #---------------- table --------------------------------
        self.mytable = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9'],height=35)

        self.mytable.heading('c1',text="Name")
        self.mytable.heading('c2',text="Mobile")
        self.mytable.heading('c3',text="E-Mail")
        self.mytable.heading('c4',text="Gender")
        self.mytable.heading('c5',text="No. of guests")
        self.mytable.heading('c6',text="Check IN date")
        self.mytable.heading('c7',text="Check OUT date")
        self.mytable.heading('c8',text="Type of Room")
        self.mytable.heading('c9',text="Allotted room no")

        self.mytable['show']='headings'

        self.mytable.column('c1',width=175,anchor='center')
        self.mytable.column('c2',width=200,anchor='center')
        self.mytable.column('c3',width=175,anchor='center')
        self.mytable.column('c4',width=175,anchor='center')
        self.mytable.column('c5',width=175,anchor='center')
        self.mytable.column('c6',width=200,anchor='center')
        self.mytable.column('c7',width=175,anchor='center')
        self.mytable.column('c8',width=175,anchor='center')
        self.mytable.column('c9',width=175,anchor='center')


        # -------------------------buttons ----------------------
        self.b1 = Button(self.window,text="Search",background=color2,foreground='white',font=font1,command=self.getAllData)
        # ------------------placements --------------------

        self.hdlbl.place(x=0,y=0,width=w,height=75)
        x1=50
        y1=100
        x_diff=150
        y_diff=50

        self.b1.place(x=x1+550,y=y1-15)

        y1+=y_diff
        self.mytable.place(x=x1+90,y=y1+20)
        self.databaseConnection()
        self.window.mainloop()

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)

    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())
            qry = " select * from newcustomers where Type_of_room=%s"
            rowcount = self.curr.execute(qry,(self.v1.get()))
            data = self.curr.fetchall()
            if data:
                for myrow in data:
                    self.mytable.insert("",END,values=myrow)
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)
        qry="select count(*) from newcustomers"

if __name__ == '__main__':
    dummy_hpwindow = Tk()
    obj = searchguest(dummy_hpwindow)
    dummy_hpwindow.mainloop()