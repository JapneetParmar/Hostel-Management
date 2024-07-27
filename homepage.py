from tkinter import *
from PIL import Image, ImageTk
from staying_customer import stayingcustomersclass
from new_customer import newcustomerclass
from Edit_Guests import Edit_Guestclass
from tkinter import messagebox
from PasswordChanger import ChangePasswordClass
from Manage_User import UserClass
from Search import searchguest
from deleteguest import deletelol
from CheckOut import bye
from Availlrooms import Availrooms
class homepageclass:
    def __init__(self):
        global img
        self.window=Tk()
        self.window.title("Hotel Manager")
        self.window.configure(background="#81CCFF")
        L0=Label(self.window,text="Welcome To ",font=("Anton",30,'bold'),background="#81CCFF",foreground="#F03838")
        L1=Label(self.window,text="Hotel Ocean View",font=("Segoe UI",60,'bold'),background="#81CCFF",foreground="#F03838")
        L0.pack()
        L1.pack() 
        img = ImageTk.PhotoImage(Image.open(r"C:\Hotel_Management\GuestID\ocean-view-hotel.jpg"))
        L2=Label(self.window,image=img)
        L2.pack()
        
        w=self.window.winfo_screenwidth()
        h=self.window.winfo_screenheight()
        w0=int(w/2)
        h0=int(h/2)
        x0=int(w/4)
        y0=int(h/4)
        self.window.minsize(w0,h0)
        self.window.geometry("%dx%d+%d+%d"%(w0,h0,x0,y0))
        self.window.state('zoomed')

        self.menubar=Menu(self.window)
        self.window.config(menu=self.menubar)
        self.window.option_add("*TearOff",False)
        self.menu1=Menu(self.menubar)
        self.menu2=Menu(self.menubar)
        self.menu3=Menu(self.menubar)
        self.menu4=Menu(self.menubar)
        self.menu5=Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu1,label="Manage Guests",font=("Anton",15))
        self.menubar.add_cascade(menu=self.menu2,label="Staying Guests",font=("Anton",15))
        self.menubar.add_cascade(menu=self.menu3,label="Search Guests",font=("Anton",15))
        self.menubar.add_cascade(menu=self.menu4,label="Available Rooms",font=("Anton",15))
        self.menubar.add_cascade(menu=self.menu5,label="User",font=("Anton",15))

        self.menu1.add_command(label="Check IN",command=lambda : newcustomerclass(self.window))
        self.menu1.add_command(label="Check OUT",command=lambda : bye(self.window))

        self.menu2.add_command(label="Edit Guests",command = lambda : Edit_Guestclass(self.window))
        self.menu2.add_command(label="View Residing guests",command = lambda : stayingcustomersclass(self.window))
        self.menu2.add_command(label="Delete Guests",command = lambda : deletelol(self.window))

        self.menu3.add_command(label="Search",command=lambda : searchguest(self.window))

        self.menu4.add_command(label="Available Rooms",command=lambda : Availrooms(self.window))

        self.menu5.add_command(label="Change Password",command=lambda : ChangePasswordClass(self.window))
        self.menu5.add_command(label="Manage User",command=lambda : UserClass(self.window))
        self.menu5.add_command(label="Logout",command=lambda :self.quitter() )

        self.window.mainloop()
        

    def quitter(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to Logout ?",parent=self.window)
        if ans =="yes":
            self.window.destroy()
            from Login_Page import LoginClass
            LoginClass()

obj=homepageclass()
