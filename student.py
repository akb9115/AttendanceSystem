from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox

from pymysql import *
from connection import *

class student:

    def __init__(self):

        self.root = Tk("STUDENT INFO")
        self.root.configure(bg='sky blue')
        self.root.geometry("680x310")
        self.root.title("Student")

        self.lb_heading = Label(self.root, text='ADD STUDENT', padx=110,width=15)
        Labelfont = ('Arial', 20, 'bold',)
        self.lb_heading.configure(foreground='black', background='sky blue', font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=3)

        self.lb_rollno =Label(self.root,text="Enter Rollno",background='sky blue',foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_studentname = Label(self.root, text="Enter Student name", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_course=Label(self.root,text='Select Course',background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_gen = Label(self.root, text="Select Gender", background='sky blue', foreground='black').grid(row=4, column=0, sticky=(W))
        self.lb_mobileno=Label(self.root,text="Enter Mobileno ",background='sky blue',foreground='black').grid(row=5, column=0, sticky=(W))
        self.lb_pmobileno = Label(self.root, text="Parent Mobileno", background='sky blue', foreground='black').grid(row=6, column=0, sticky=(W))
        self.lb_fname=Label(self.root,text='Enter Father Name',background='sky blue', foreground='black').grid(row=2, column=2, sticky=(E))
        self.lb_semester = Label(self.root, text="Select Semester", background='sky blue', foreground='black').grid(row=3, column=2, sticky=(E))
        self.lb_email = Label(self.root, text="Enter Email", background='sky blue', foreground='black').grid(row=4, column=2, sticky=(E))
        self.lb_address = Label(self.root, text="Enter Address", background='sky blue', foreground='black').grid(row=5, column=2, sticky=(E))
        self.lb_paddress = Label(self.root, text="Enter Permanent Address", background='sky blue', foreground='black').grid(row=6, column=2, sticky=(E))


        self.tb_roll = Entry(self.root)
        self.tb_sname = Entry(self.root)
        self.cb_course = Combobox(self.root)

        db = connection()
        cr = db.conn.cursor()
        s = "select coursename from courses"
        cr.execute(s)
        p = cr.fetchall()
        lst_cname = []
        for i in range(0, len(p)):
            lst_cname.append(p[i][0])

        self.cb_course.config(values=tuple(lst_cname))
        self.cb_gen=Combobox(self.root,values=('Female','Male'),state='readonly')
        self.cb_sem = Combobox(self.root,state='readonly')

        self.lst_sem=[]
        for i in range(1,11):
            self.lst_sem.append(i)

        self.cb_sem.config(values=tuple(self.lst_sem))
        self.tb_mobile = Entry(self.root)
        self.tb_pmobile = Entry(self.root)
        self.tb_fname=Entry(self.root)
        self.tb_email=Entry(self.root)
        self.tb_address=Entry(self.root)
        self.tb_paddress=Entry(self.root)

        self.tb_roll.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_sname.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_course.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_gen.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_mobile.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_pmobile.grid(row=6, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_fname.grid(row=2, column=3, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_sem.grid(row=3, column=3, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_email.grid(row=4,column=3,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_address.grid(row=5,column=3,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_paddress.grid(row=6,column=3,padx=(5),pady=(5),sticky=(N,E,W))

        self.bt1 = Button(self.root, text="submit",command=self.test ,  width=15, bg='white', fg='black',padx=10).grid(row=8,column=2,sticky=(S),pady=15)

        self.root.mainloop()

    def test(self):

        self.x = int(self.tb_email.get().count("@"))
        self.d = int(self.tb_email.get().count("."))

        if self.tb_roll.get() == "" or self.tb_sname.get() == "" or self.cb_course.get() == "" or self.cb_gen.get() == "" or self.cb_sem.get() == "" or self.tb_mobile.get() == "" or self.tb_pmobile.get() == "" or self.tb_fname.get() == "" or self.cb_sem.get() == "" or self.tb_email.get() == "" or self.tb_address.get() == "" or self.tb_paddress.get() == "":
            showerror("", "Cannot Leave any field blank", parent=self.root)

        elif self.tb_mobile.get().isalpha() == True:
            showerror("", "Mobile number not valid")

        elif self.tb_pmobile.get().isalpha() == True:
            showerror("", "Mobile number not valid")

        elif self.x != 1 or self.tb_email.get() == "" or self.d != 1:
            showerror("", "Wrong Email", parent=self.root)




        else:
            db = connection()
            cr = db.conn.cursor()
            query = "insert into student values(null,'" + self.tb_roll.get() + "','" + self.tb_sname.get() + "','" + self.tb_fname.get() + "','" + self.cb_gen.get() + "','" + self.cb_course.get() + "','" + self.cb_sem.get() + "','" + self.tb_mobile.get() + "','" + self.tb_address.get() +  "','" + self.tb_email.get() +  "','" + self.tb_pmobile.get() +  "','" + self.tb_paddress.get() + "')"
            cr.execute(query)
            db.conn.commit()
            showinfo("Success", "Student added successfully")
