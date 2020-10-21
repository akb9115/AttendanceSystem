from tkinter import*
from pymysql import*
from tkinter.ttk import*
from connection import *

class view:

    def __init__(self):

        self.root=Tk()
        self.root.title("View Details")
        self.root.configure(background='sky blue')

        self.lb_heading = Label(self.root, text="ADMIN DETAILS")
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=0)

        self.t=Treeview(self.root,columns=("E-mail","Mobile","Type"))
        self.t.heading("E-mail",text="E-mail")
        self.t.heading("Mobile",text="Mobile")
        self.t.heading("Type",text="Type")



        cb=connection()

        query="select email,mobile,type from admins"
        cr=cb.conn.cursor()
        cr.execute(query)
        self.p=cr.fetchall()

        for i in range(0,len(self.p)):
            self.t.insert("",values=self.p[i],index=i)

        self.t.column("#0",width=0)
        self.t.column("Type",width=130)
        self.t.grid(row=1,column=0)
        self.root.mainloop()


