from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox 
import pymysql
from printing import my_cust_PDF
import os
from deleteguest import deletelol

class bye:
    def __init__(self,pwindow):
        self.window  = Toplevel(pwindow)
        self.window.title("Checking Out Guest")
        self.window.configure(background="#81CCFF")
        W=self.window.winfo_screenwidth()
        H=self.window.winfo_screenheight()
        w0=W-200
        h0=H-200
        self.window.geometry("%dx%d+%d+%d"%(w0,h0,50,50))
        self.window.state('zoomed')

        font1=("Anton",20)
        color1="#81CCFF"
        self.MHD=Label(self.window,text="Guest Check Out",font=("Franklin Gothic Medium",50,"bold"),background="#F03838",foreground="white",relief=FLAT,width=W)
    

        self.L9=Label(self.window,text="Allotted Room no",font=font1,background=color1)
        self.t0=Entry(self.window,width=15,font=("Anton",15))
        self.L9.place(x=200,y=135)
        self.t0.place(x=430,y=140)
        self.L1=Label(self.window,text="(Delete After Billing)",font=font1,background=color1)
        self.b3=Button(self.window,text="Delete Data",width=15,font=("Anton",15),command=lambda: deletelol(self.window))
        self.L1.place(x=1150,y=135)
        self.b3.place(x=1430,y=140)
       
        self.B1=Button(self.window,text="Get Data",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.getAllData)
        self.B1.place(x=630,y=135,height=35)
        self.B2=Button(self.window,text="Print Bill",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.getPrintout)
        self.B2.place(x=850,y=875,height=35)

        self.table = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9'],height=30)

        self.table.heading('c1',text="Name")
        self.table.heading('c2',text="Mobile")
        self.table.heading('c3',text="E-Mail")
        self.table.heading('c5',text="No. of Guests")
        self.table.heading('c6',text="Check in")
        self.table.heading('c7',text="Check Out")
        self.table.heading('c8',text="Room Type")
        self.table.heading('c9',text="Allotted Room no")
        self.table.heading('c4',text="Gender")

        self.table['show']='headings'

        self.table.column('c1',width=175,anchor='center')
        self.table.column('c2',width=155,anchor='center')
        self.table.column('c3',width=200,anchor='center')
        self.table.column('c5',width=175,anchor='center')
        self.table.column('c6',width=175,anchor='center')
        self.table.column('c7',width=175,anchor='center')
        self.table.column('c8',width=175,anchor='center')
        self.table.column('c9',width=150,anchor='center')
        self.table.column('c4',width=175,anchor='center')

        self.MHD.pack()
        self.databaseConnection()
        self.table.place(x=150,y=200)
        self.window.mainloop()

    
    def getPrintout(self):
        pdf = my_cust_PDF()
        headings = ['Name', 'No. of guest', 'Check IN', 'Check OUT', 'Type of Room','Alloted Room','Bill']

        pdf.print_chapter(self.pdata, headings)

        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')

    def databaseConnection(self):
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)
 
    def getAllData(self):
        try:
            qry="select * from newcustomers where Allotted_Room_no=%s"
            rowcount=self.curr.execute(qry,(self.t0.get()))
            data = self.curr.fetchall()
            self.pdata=[]
            self.sdata=[]
            if data:
                for myrow in data:
                    from datetime import datetime
                    d1 = myrow[5]
                    d2 = myrow[6]
                    self.days = (d2-d1).days
                    self.bill=800*self.days
                    print(self.bill)
                    print(self.pdata)
                    self.pdata.append([myrow[0],myrow[4],myrow[5],myrow[6],myrow[7],myrow[8],int(self.bill)])
                    self.table.insert("",END,values=myrow)


            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error while fetching Data  : \n"+str(e),parent=self.window)
        
    
if __name__ == '__main__':
    dummy_pwindow = Tk()
    obj = bye(dummy_pwindow)
    dummy_pwindow.mainloop()