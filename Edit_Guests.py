from tkinter import *
from tkinter.ttk import Combobox 
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk 
from tkcalendar import DateEntry
import pymysql

class Edit_Guestclass:
    default_img_name="DefaultID.jpg"
    def __init__(self,pwindow):
        self.window  = Toplevel(pwindow)
        self.window.title("Edit Guests")
        self.window.configure(background="#81CCFF")

        w=self.window.winfo_screenwidth()
        h=self.window.winfo_screenheight()
        w0=w-200
        h0=h-200
        #self.window.minsize(w0,h0)
        self.window.geometry("%dx%d+%d+%d"%(w0,h0,50,50))
        self.window.state('zoomed')

        font1=("Anton",20)
        color1="#81CCFF"
        self.MHD=Label(self.window,text="Edit Booking",font=("Franklin Gothic Medium",50,"bold"),background="#F03838",foreground="white",relief=FLAT)
        self.L0=Label(self.window,text="Name",font=font1,background=color1)
        self.L1=Label(self.window,text="Mobile",font=font1,background=color1)
        self.L2=Label(self.window,text="E-Mail",font=font1,background=color1)
        self.L3=Label(self.window,text="Gender",font=font1,background=color1)
        self.L4=Label(self.window,text="Number of Guests",font=font1,background=color1)
        self.L5=Label(self.window,text="Check in Date",font=font1,background=color1)
        self.L6=Label(self.window,text="Check out Date",font=font1,background=color1)
        self.L7=Label(self.window,text="Type of room",font=font1,background=color1)
        self.L8=Label(self.window, text="Allotted Room no", font=font1, background=color1)
        self.imglbl=Label(self.window,borderwidth=1,relief='groove')
        self.L9=Label(self.window, text="Identity Proof", font=font1, background=color1)

        self.t0=Entry(self.window,width=35,font=("Anton",15))
        self.t1=Entry(self.window,width=35,font=("Anton",15))
        self.t2=Entry(self.window,width=35,font=("Anton",15))
        self.v0=StringVar()
        self.r1=Radiobutton(self.window,text="Male",value="male",variable=self.v0,width=12,tristatevalue=0,font=("Anton",15))
        self.r2=Radiobutton(self.window,text="Female",value="female",variable=self.v0,width=12,tristatevalue=0,font=("Anton",15))
        self.t4=Entry(self.window,width=35,font=("Anton",15))
        self.t5= DateEntry(self.window,  background='darkblue',font=font1,
                         foreground='white', borderwidth=2, year=2010,date_pattern='y-mm-dd',width=24)
        self.t6= DateEntry(self.window,  background='darkblue',font=font1,
                         foreground='white', borderwidth=2, year=2010,date_pattern='y-mm-dd',width=24)
        self.v1=StringVar()
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=["Luxury Room","Creative Room","Lodge Room"],textvariable=self.v1,state="readonly",width=33,font=("Anton",15))
        self.t7 = Entry(self.window,width=35,font=("Anton",15))
        self.B2=Button(self.window,text="Clear All",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.ClearData)
        self.B3=Button(self.window,text="Get Data",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.FetchData)
        self.B4=Button(self.window,text="Update",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.updateData)
        self.B5=Button(self.window,text="Select",font=("Anton",20,'bold'),background="#F03838",foreground="white",relief=RAISED,command=self.selectImage)

        self.MHD.place(x=0,y=0,width=w)
        x1=30
        y1=130
        x_gap=150
        y_gap=80
        self.L0.place(x=x1,y=y1)
        self.t0.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L3.place(x=x1,y=y1)
        self.r1.place(x=x1+x_gap+150,y=y1,height=30)
        self.r2.place(x=x1+3+x_gap+x_gap+220,y=y1,height=30)
        y1=y1+y_gap
        self.L4.place(x=x1,y=y1)
        self.t4.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+x_gap+150,y=y1+5,height=30)
        y1=y1+y_gap
        self.L8.place(x=x1, y=y1)
        self.t7.place(x=x1+x_gap+150,y=y1+5,height=30)

        self.L9.place(x=1250, y=120)

        self.imgsize=600
        self.imglbl.place(x=x1+1000,y=y1-self.imgsize,width=self.imgsize,height=self.imgsize)
        self.B5.place(x=x1+1190,y=y1+70,width=160,height=40)

        y1 = y1 + y_gap
        self.B4.place(x=x1+420,y=y1+50,width=150,height=40)
        self.B2.place(x=x1+300,y=y1-10,width=150,height=40)
        self.B3.place(x=x1+540,y=y1-10,width=150,height=40)
        
        self.databaseConnection()
        self.ClearData()
        self.window.mainloop()

    def selectImage(self):
        filename = askopenfilename(filetypes=[ ('All Pictures',"*.jpg;*.png;*.jpeg"),
                                               ("PNG Images",'*.png'),("Jpg Images",'*.jpg')],parent=self.window)
        if filename!="":
            self.img1  = Image.open(filename).resize((self.imgsize,self.imgsize))
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)

            path = filename.split("/")
            name = path[-1]
            import time
            unique = str(int(time.time()))
            self.actualname = unique+name

    def databaseConnection(self): 
        try:
            self.connection=pymysql.connect(host='localhost',db='HotelManagement_db',user='root',password="")
            self.curr=self.connection.cursor()
        except Exception as e:
            messagebox.showerror("Error","Error in connectiong to database : \n"+str(e),parent=self.window)

    def updateData(self):
        if(self.validationCheck()==False):
            return 
        
        if self.actualname==self.oldname: 
            pass
        else: 
            self.img1.save("guestpic//" + self.actualname)
            if self.oldname==self.default_img_name: 
                pass

        try:
            qry = " update newcustomers set Name=%s, Mobile=%s, E_Mail=%s, Gender=%s, " \
                    "Number_of_Members=%s, Check_in_Date=%s, Check_out_Date=%s,Type_of_room=%s,photo=%s where Allotted_Room_no=%s"
            rowcount=self.curr.execute(qry,(self.t0.get(),self.t1.get(),self.t2.get(),self.v0.get(),self.t4.get(),self.t5.get_date(),
                                             self.t6.get_date(),self.v1.get(),self.actualname,self.t7.get()))
            self.connection.commit()
            if rowcount==1:
                messagebox.showinfo("Success","Student Record Updated Successfully",parent=self.window)
                self.ClearData()
        except Exception as e:
            messagebox.showerror("Error","Update Error : \n"+str(e),parent=self.window)

    def ClearData(self):
        self.t0.delete(0,END)
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v0.set(None)
        self.t4.delete(0,END)
        self.t5.delete(0,END)
        self.t6.delete(0,END)
        self.v1.set("Choose Room type")
        self.t7.delete(0,END)
        self.actualname=self.default_img_name
        self.img1 = Image.open(r"GuestID/DefaultID.jpg").resize((self.imgsize, self.imgsize))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def FetchData(self,pk_value=None):
        if pk_value==None:
            Type_of_room = self.v1.get()
        else:
            Type_of_room=pk_value
        try:
            qry="select * from newcustomers where Allotted_Room_no=%s"
            rowcount=self.curr.execute(qry,(self.t7.get()))
            data=self.curr.fetchone()
            self.ClearData()
            if data:
                self.t0.insert(0,data[0])
                self.t1.insert(0,data[1])
                self.t2.insert(0,data[2])
                self.v0.set(data[3])
                self.t4.insert(0,data[4])
                self.t5.insert(0,data[5])
                self.t6.insert(0,data[6])
                self.v1.set(data[7])
                self.t7.insert(0,data[8])
                self.actualname = data[9]
                self.oldname = data[9]

                self.img1 = Image.open("guestpic//" + self.actualname).resize((self.imgsize, self.imgsize))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

            else:
                messagebox.showwarning("Not Found","No record found",parent=self.window)
        except Exception as e:
            messagebox.showerror("Error","Error in getting data : \n"+str(e),parent=self.window)

    def validationCheck(self):
        if len(self.t0.get())<1      or          (self.t0.get().isdigit()):
                messagebox.showwarning("Empty","Enter Proper Name",parent=self.window)
                return False
        elif len(self.t1.get())<1    :
                messagebox.showwarning("Empty","Enter Mobile",parent=self.window)
                return False
        elif (self.t2.get().isdigit() or len(self.t2.get())<1 ):    
                messagebox.showwarning("Empty","Enter E-Mail",parent=self.window)
                return False
        elif  not(self.v0.get()=="male" or self.v0.get()=="female"):
                messagebox.showwarning("Empty","Select gender",parent=self.window)
                return False
        elif self.t4.get()==""    :
                messagebox.showwarning("Empty","Enter No. of guests",parent=self.window)
                return False
        elif self.t5.get()=="" :
                messagebox.showwarning("Empty","Select Check In Date",parent=self.window)
                return False
        elif self.t6.get()=="" :
                messagebox.showwarning("Empty","Select Check out Date",parent=self.window)
                return False
        elif not(self.v1.get()=="Luxury Room" or self.v1.get()=="Creative Room" or self.v1.get()=="Lodge Room"):
                messagebox.showwarning("Empty","Choose Type of Room",parent=self.window)
                return False
        elif self.t7.get()==""  :
                messagebox.showwarning("Empty","Enter Allotted Room no",parent=self.window)
                return False
        return True


if __name__ == '__main__':
    dummy_pwindow = Tk()
    obj = Edit_Guestclass(dummy_pwindow)
    dummy_pwindow.mainloop()