from tkinter.ttk import*
from tkinter import*
from pymysql import*
from connection import *

class viewteacher:

    def __init__(self):

        self.root=Tk()
        self.root.title("View Details")
        self.root.configure(background='sky blue')

        self.lb_heading = Label(self.root, text='TEACHER DETAILS' ,padx=20)
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=0)

        self.t=Treeview(self.root,columns=("tid","tname","mobileno",'address','gender','qual','exp','email','pass'))
        self.t.heading("tid",text="Teacher ID")
        self.t.heading("tname",text="Teacher Name")
        self.t.heading("mobileno",text="Mobile number")
        self.t.heading("address", text="Adderss")
        self.t.heading("gender",text="Gender")
        self.t.heading("qual", text="Qualification")
        self.t.heading("exp", text="Experience")
        self.t.heading("email", text="E_mail")
        self.t.heading("pass", text="Password")




        cb=connection()
        query="select tid,tname,mobileno,address,gender,qualification,experience,email,password from teacher"
        cr=cb.conn.cursor()
        cr.execute(query)
        self.p=cr.fetchall()

        for i in range(0,len(self.p)):
            self.t.insert("",values=self.p[i],index=i)

        self.t.column("#0",width=0)

        self.t.grid(row=1,column=0)
        self.root.mainloop()

