
from tkinter.ttk import*
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from connection import *


class department:

    def __init__(self):

        self.root = Tk("DEPARTMENTS")
        self.root.configure(bg='sky blue')
        self.root.geometry("550x250")
        self.root.title("Departments")

        self.lb_heading=Label(self.root,text='ADD DEPARTMENTS',padx=70)
        Labelfont=('Arial',20,'bold')
        self.lb_heading.configure(foreground='black',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0,column=0,columnspan=3)

        self.lb_dept = Label(self.root, text="Enter Department Name",background='sky blue',foreground='black')
        self.lb_hod= Label(self.root, text="Enter HOD Name",background='sky blue',foreground='black')
        self.lb_desc = Label(self.root, text="Enter Description",background='sky blue',foreground='black')

        self.tb_dept = Entry(self.root)
        self.tb_hod = Entry(self.root)
        self.tb_desc = Text(self.root,height=7,width=50)

        self.bt = Button(self.root, text="submit", command=self.test,width=15,bg='white',fg='black').grid(row=6, column=1)

        self.lb_dept.grid(row=1, column=0,sticky=(W))
        self.lb_hod.grid(row=2, column=0,sticky=(W))
        self.lb_desc.grid(row=3, column=0,sticky=(W))

        self.tb_dept.grid(row=1,column=1,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_hod.grid(row=2,column=1,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_desc.grid(row=3,column=1,padx=(5),pady=(5),sticky=(N,E,W))

        self.root.mainloop()


    def test(self):
        if self.tb_dept.get()== "" or self.tb_hod.get()=="":
            showerror("","Cannot Leave any field blank",parent=self.root)

        elif self.tb_dept.get().isalpha()==False:
            showerror("","Name cannot be numeric")

        else:
            db = connection()
            cr = db.conn.cursor()
            query = "insert into department values('" + self.tb_dept.get() + "','" + self.tb_hod.get() + "','" + self.tb_desc.get(0.1,END) + "')"
            cr.execute(query)
            db.conn.commit()
            showinfo("Success", "Departments added successfully")




