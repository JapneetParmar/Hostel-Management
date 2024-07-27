from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

import pymysql


class UserClass:
    def __init__(self,hp_window):
        self.window  = Toplevel(hp_window)
        self.window.title("Manage Users")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = w-100
        h1 = h-150
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,50))
        self.window.state('zoomed')
        font1 = ("Anton" , 15,'bold')
        color1 = "#81CCFF"
        color2 = "#F03838"
        self.window.config(background=color1)
        self.hdlbl = Label(self.window,text="Manage Users",background=color2,foreground='white',font=('Clarendon Lt BT',30,'bold'),borderwidth=5,relief='flat')
        self.L1 = Label(self.window,text="Username",background=color1,font=font1)
        self.L2 = Label(self.window,text="Password",background=color1,font=font1)
        self.L3 = Label(self.window,text="Usertype",background=color1,font=font1)

        self.t1 = Entry(self.window,font=font1)
        self.t2 = Entry(self.window,font=font1,show='*')
        self.v1 = StringVar()
        self.c1 = Combobox(self.window,values=("Admin","Employee"), textvariable=self.v1, font=font1,state='readonly')

        self.mytable = Treeview(self.window, columns=['c1', 'c2'],
                                height=10)

        self.mytable.heading('c1', text="Username")
        self.mytable.heading('c2', text="Usertype")

        self.mytable['show'] = 'headings'

        self.mytable.column('c1', width=200, anchor='center')
        self.mytable.column('c2', width=200, anchor='center')

        self.mytable.bind("<ButtonRelease>",lambda e: self.getSelectedRow())

        self.b1 = Button(self.window,text="Save",background=color2,foreground='white',font=font1,command=self.saveData)
        self.b2 = Button(self.window,text="Update",background=color2,foreground='white',font=font1,command=self.updateData)
        self.b3 = Button(self.window,text="Delete",background=color2,foreground='white',font=font1,command=self.deleteData)
        self.b4 = Button(self.window,text="Fetch",background=color2,foreground='white',font=font1,command=self.fetchData)
        self.b5 = Button(self.window,text="Search",background=color2,foreground='white',font=font1,command=self.getAllData)

        self.hdlbl.place(x=0,y=0,width=w,height=80)
        x1=80
        y1=0
        x_diff=150
        y_diff=50

        self.L1.place(x=x1+150,y=y1+300)
        self.t1.place(x=x1+320,y=y1+300)
        self.b4.place(x=x1+600,y=y1+300,width=130,height=30)
        self.mytable.place(x=x1+x_diff+950,y=y1+350)

        y1+=y_diff
        self.L2.place(x=x1+150,y=y1+350)
        self.t2.place(x=x1+320,y=y1+350)

        y1+=y_diff
        self.L3.place(x=x1+150,y=y1+400)
        self.c1.place(x=x1+320,y=y1+400)
        self.b5.place(x=x1+600,y=y1+400,width=130,height=30)

        y1+=y_diff
        self.b1.place(x=x1+150,y=y1+420,width=150,height=40)
        self.b2.place(x=x1+x_diff+150+40,y=y1+420,width=150,height=40)
        self.b3.place(x=x1+x_diff+150+x_diff+80,y=y1+420,width=150,height=40)

        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            qry = " insert into userdata values(%s,%s,%s)"
            rowcount = self.curr.execute(qry , (self.t1.get(),self.t2.get(),self.v1.get()))
            self.connection.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Error","Insertion Error : \n"+str(e),parent=self.window)

    def updateData(self):
        try:
            qry = " update userdata set Password=%s, UserType=%s where Name=%s"
            rowcount = self.curr.execute(qry , (self.t2.get(),self.v1.get(), self.t1.get()))
            self.connection.commit()
            if rowcount==1:
                messagebox.showinfo("Success","User Record Updated Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Error","Update Error : \n"+str(e),parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ??",parent=self.window)
        if ans =="yes":
            try:
                qry = "delete from userdata where Name=%s"
                rowcount = self.curr.execute(qry , (self.t1.get()))
                self.connection.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","User Record Deleted Successfully",parent=self.window)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Error","Deletion Error : \n"+str(e),parent=self.window)

    def getSelectedRow(self):
        rowid = self.mytable.focus()
        rowdata = self.mytable.item(rowid)
        row_values = rowdata['values']
        coldata = row_values[0]
        self.fetchData(coldata)

    def fetchData(self,pk_value=None):
        if pk_value==None:
            un = self.t1.get()
        else:
            un=pk_value
        try:
            qry = " select * from userdata where Name=%s"
            rowcount = self.curr.execute(qry , (un))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])

                self.b2['state'] = 'normal'
                self.b3['state'] = 'normal'
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.c1.set("Choose UserType")
        self.b2['state']='disable'
        self.b3['state']='disable'
        self.getAllData()

    def getAllData(self):
        try:
            qry = " select * from userdata where UserType like %s"
            utype = self.v1.get()
            if utype=="Choose UserType":
                utype=""
            rowcount = self.curr.execute(qry,(utype+"%"))
            data = self.curr.fetchall()

            self.mytable.delete(*self.mytable.get_children())
            if data:
                for myrow in data:
                    r1 = [myrow[0],myrow[2]]
                    self.mytable.insert("",END,values=r1)
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)

if __name__ == '__main__':
    dummy_hpwindow = Tk()
    obj = UserClass(dummy_hpwindow)
    dummy_hpwindow.mainloop()