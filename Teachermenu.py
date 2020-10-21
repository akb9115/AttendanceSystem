from tkinter.ttk import *
from tkinter import *
from pymysql import *
from tkinter.messagebox import *
from connection import *
# from teacherlogin import *
from manageattendance import *

from tkinter import *
from PIL import ImageTk,Image


class tlogin:
    TID = 0
    def __init__(self):

        self.root = Tk()
        self.root.geometry("450x300")
        self.root.resizable(0, 0)
        self.root.config(background="snow")
        self.root.title("Teacher Login")

        self.root.geometry("+{}+{}".format(520, 280))

        lb = Label(self.root, text="Teacher Login", font=("Elephant", 30), fg="blue", bg="snow").pack()
        f = Frame(self.root, width=500, height=80, bd=4, relief="raise", bg="white")
        f.pack()
        lb = Label(f, text="Email", bg="white")
        lb1 = Label(f, text="Password", bg="white")

        self.tf_email = Entry(f, width=40, font=("times new roman", 14), relief="groove", bg="lemonchiffon")
        self.tf_password = Entry(f, width=40, font=("times new roman", 14), relief="groove", bg="lemonchiffon")
        self.tf_password.configure(show="*")
        self.lb_blank = Label(f, text="")
        self.progress = Progressbar(f, orient="horizontal", length=410, mode="determinate")
        self.progress.config()
        bt = Button(f, text="Login", command=self.test, font=("arial", 8, "bold"), fg="brown",activebackground="skyblue", activeforeground="snow", height=1, width=15)

        lb.grid(row=0, column=0, padx=20, sticky=W, pady=5)
        self.tf_email.grid(row=1, column=0, padx=20, pady=5, columnspan=2)
        lb1.grid(row=2, column=0, padx=20, sticky=W, pady=5)
        self.tf_password.grid(row=3, column=0, padx=20, pady=5, columnspan=2)
        bt.grid(row=4, column=0, padx=20, pady=5, sticky=E)
        self.bytes = 0
        self.maxbytes = 0

        self.lb_blank.grid(row=5, column=0, sticky=(W))
        self.progress.grid(row=6, column=0, columnspan=3)

        self.root.mainloop()

    def test(self):
        global TID
        db=connection()
        cr1 = db.conn.cursor()
        s1 = "select * from teacher where email='"+ self.tf_email.get() +"' and password='"+ self.tf_password.get() +"'"
        cr1.execute(s1)
        global p1
        p1 = cr1.fetchone()
        if p1==None:
            showerror("","Invalid Email or Password!!!")
        else:
            self.progress["value"] = 0
            self.maxbytes = 100
            self.progress["maximum"] = 100
            self.read_bytes()

    def read_bytes(self):
        self.bytes += 1
        abc = "Loading.... (" + str(self.bytes // 1) + "%)"
        self.lb_blank.config(text=abc)
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            self.root.after(100, self.read_bytes)
        else:
            global TID
            TID = p1[0]
            self.root.withdraw()
            x.deiconify()







def test3():
    global TID
    a = frm_mark_attandence(x,TID)

def logout():
    x.destroy()
    y = tlogin()

x= Tk()
x.title("Teacher Menu")
x.configure(background='sky blue')

x.geometry("+{}+{}".format(380, 100))

path="1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
lb=Label(x,image=img,height=400,width=800)
lb.place(x=0,y=0)
lb.pack()
mymenu=Menu(x)
x.config(menu=mymenu)
option1=Menu(mymenu,tearoff=0)
option2=Menu(mymenu,tearoff=0)
mymenu.add_cascade(label="File",menu=option1)
option1.add_cascade(label="Log out",command=logout)
mymenu.add_cascade(label='Mark Attendance',menu=option2)
option2.add_cascade(label='Mark Attendence',command=test3)
x.withdraw()
y = tlogin()
x.mainloop()


