from tkinter import*
from pymysql import*
from tkinter.ttk import*
from connection import *

class viewdept:

    def __init__(self):

        self.root=Tk()
        self.root.title("View Details")
        self.root.configure(background='sky blue')

        self.lb_heading = Label(self.root, text="DEPARTMENT DETAILS")
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=0)

        self.t=Treeview(self.root,columns=("Depart","HOD","Desc"))
        self.t.heading("Depart",text="Department Name")
        self.t.heading("HOD",text="HOD Name")
        self.t.heading("Desc",text="Description")



        cb=connection()
        query="select deptname,hodname,description from department"
        cr=cb.conn.cursor()
        cr.execute(query)
        self.p=cr.fetchall()

        for i in range(0,len(self.p)):
            self.t.insert("",values=self.p[i],index=i)

        self.t.column("#0",width=0)
        self.t.column("HOD",width=170)
        self.t.grid(row=1,column=0)
        self.root.mainloop()


