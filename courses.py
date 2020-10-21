from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from connection import *

class courses:

    def __init__(self):

        self.root = Tk("COURSES")
        self.root.configure(bg='sky blue')
        self.root.geometry("450x290")
        self.root.title("Courses")

        self.lb_heading = Label(self.root, text='ADD COURSES', padx=70)
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='black', background='sky blue', font=Labelfont)
        self.lb_heading.grid(row=0, column=0, columnspan=3)

        self.lb_dept =Label(self.root,text="Select Departments",background='sky blue',foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_cname = Label(self.root, text="Enter Course Name", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_duration = Label(self.root, text="Enter Duration", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_desc=Label(self.root,text="Enter Description",background='sky blue',foreground='black').grid(row=4, column=0, sticky=(W))

        self.cb_dept = Combobox(self.root,state='readonly')
        
        db = connection()
        cr = db.conn.cursor()
        s = "select deptname from department"
        cr.execute(s)
        p = cr.fetchall()
        lst_deptname= []
        for i in range(0,len(p)):
            lst_deptname.append(p[i][0])
        
        self.cb_dept.config(values=tuple(lst_deptname))
        self.cb_dept.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_cname=Entry(self.root)
        self.tb_cname.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_duration = Combobox(self.root, values=("1 Year", "2 Year", "3 Year", "4 Year", "5 Year"))
        self.cb_duration.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_desc = Text(self.root,height=7,width=40)
        self.tb_desc.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))




        self.bt1 = Button(self.root, text="submit", command=self.test, width=15, bg='white', fg='black').grid(row=6,column=1)

        self.root.mainloop()

    def test(self):
        if self.cb_dept.get()== "" or self.tb_cname.get()== "" or self.cb_duration.get()== "" or self.tb_desc.get(0.1,END)== "":
            showerror("", "Cannot Leave any field blank", parent=self.root)

        elif self.cb_dept.get().isalpha() == False:
            showerror("", "Name cannot be numeric")

        else:
            db = connection()
            cr = db.conn.cursor()
            query = "insert into courses values('" + self.tb_cname.get() + "','" + self.cb_duration.get() + "','" + self.tb_desc.get(0.1,END) + "','" + self.cb_dept.get() + "')"
            cr.execute(query)
            db.conn.commit()
            showinfo("Success", "Courses added successfully")


