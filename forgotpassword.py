from tkinter.ttk import *
from tkinter import *
from connection import *
from tkinter.messagebox import *
import random

class fpassword:

    def __init__(self):

        self.root=Tk("FORGOT PASSWORD")
        self.root.configure(bg='sky blue')
        self.root.geometry("370x150")
        self.root.title("FORGOT PASSWORD")

        self.lb_heading = Label(self.root, text='FORGOT PASSWORD')
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black", background='sky blue', font=Labelfont)
        self.lb_heading.grid(row=0, column=1)

        self.lb_email = Label(self.root, text="Email", background='sky blue', foreground='black').grid(row=1, column=0,sticky=(W))
        self.lb_OTP=Label(self.root,text="Enter OTP",background='sky blue',foreground='black').grid(row=2,column=0,sticky=(W))

        self.tb_email = Entry(self.root)
        self.tb_OTP = Entry(self.root)

        self.tb_email.grid(row=1, column=1, padx=(5), pady=(5),columnspan=4, sticky=(N, E, W))
        self.tb_OTP.grid(row=2, column=1, padx=(5), pady=(5),columnspan=4, sticky=(N, E, W))

        self.bt1 = Button(self.root, text="Get OTP",command=self.test, width=15, bg='white', fg='black').grid(row=3,column=1,sticky=(W))
        self.bt2 = Button(self.root, text="Change Password", width=15, bg='white', fg='black').grid(row=3, column=1, sticky=(E))

        self.root.mainloop()

    def test(self):
        s=0
        db = connection()
        s1 = "select email from teacher"
        cr = db.conn.cursor()
        cr.execute(s1)
        p = cr.fetchall()
        print(p)
        db.conn.commit()
        for i in range (0,len(p)):
            if p[i][0] ==self.tb_email.get():
                s=1
        if s==1:
            x=random.randint(1000,9999)
            print(x)
            if x==self.tb_OTP.get():
                showinfo("","success")
        else:
            showinfo("","Email Not found")
