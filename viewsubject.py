from tkinter.ttk import*
from tkinter import*
from pymysql import*
from connection import *

class viewsubject:

    def __init__(self):

        self.root=Tk()
        self.root.title("View Details")
        self.root.configure(background='sky blue')

        self.lb_heading = Label(self.root, text="SUBJECT DETAILS")
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=0)

        self.t=Treeview(self.root,columns=("sid",'sname',"desc",'tid','cname','sem'))
        self.t.heading("sid",text="Student ID")
        self.t.heading("sname",text="Subject Name")
        self.t.heading("desc",text="Description")
        self.t.heading("tid",text="Teacher")
        self.t.heading("cname",text="Course Name")
        self.t.heading("sem", text="Semester")



        cb=connection()
        query="select sid,sname,description,tid,cname,semester from subject"
        cr=cb.conn.cursor()
        cr.execute(query)
        self.p=cr.fetchall()

        for i in range(0,len(self.p)):
            self.t.insert("",values=self.p[i],index=i)

        self.t.column("#0",width=0)

        self.t.grid(row=1,column=0)
        self.root.mainloop()


