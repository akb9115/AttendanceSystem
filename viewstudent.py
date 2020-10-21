from tkinter.ttk import*
from tkinter import*
from pymysql import*
from connection import *

class viewstudent:

    def __init__(self):

        self.root=Tk()
        self.root.title("View Details")
        self.root.configure(background='sky blue')

        self.lb_heading = Label(self.root, text='STUDENT DETAILS' ,padx=2)
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=0,columnspan=1)

        self.t=Treeview(self.root,columns=("stid","roll","sname",'fname','gender','course','sem','mobile','address','email','pmobile','paddress'))
        self.t.heading("stid",text="Student ID")
        self.t.heading("roll",text="Roll Number")
        self.t.heading("sname",text="Student Name")
        self.t.heading("fname", text="Father Name")
        self.t.heading("gender",text="Gender")
        self.t.heading("course", text="Course")
        self.t.heading("sem", text="Semester")
        self.t.heading("mobile", text="Mobile Number")
        self.t.heading("address", text="Address")
        self.t.heading("email", text="Email")
        self.t.heading("pmobile", text="Parent Mobile Number")
        self.t.heading("paddress", text="Parmanent Address")






        cb=connection()
        query="select studentid,rollno,studentname,fname,gender,course,semester,mobileno,address,email,pmobileno,paddress from student"
        cr=cb.conn.cursor()
        cr.execute(query)
        self.p=cr.fetchall()

        for i in range(0,len(self.p)):
            self.t.insert("",values=self.p[i],index=i)

        self.t.column("#0",width=0)

        self.t.grid(row=1,column=0)
        self.root.mainloop()

