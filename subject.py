from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from connection import *


class subject:

    def __init__(self):

        self.root = Tk("SUBJECTS")
        self.root.configure(bg='sky blue')
        self.root.geometry("450x350")
        self.root.title("Subjects")

        self.lb_heading = Label(self.root, text='ADD SUBJECT', padx=70)
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='black', background='sky blue', font=Labelfont)
        self.lb_heading.grid(row=0, column=0, columnspan=3)

        self.lb_course = Label(self.root, text="Select Course", background='sky blue', foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_sem = Label(self.root, text="Select Semester", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_sname = Label(self.root, text="Enter Subject Name", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_desc = Label(self.root, text="Enter Description", background='sky blue', foreground='black').grid(row=4,column=0,sticky=(W))
        self.lb_teacher = Label(self.root, text="Select Teacher", background='sky blue', foreground='black').grid(row=5,column=0,sticky=(W))

        self.cb_course = Combobox(self.root, state='readonly')

        db = connection()
        cr = db.conn.cursor()
        s = "select coursename from courses"
        cr.execute(s)
        p = cr.fetchall()
        lst_cname = []
        for i in range(0, len(p)):
            lst_cname.append(p[i][0])

        self.cb_course.config(values=tuple(lst_cname))
        self.cb_course.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_sem=Combobox(self.root, values=("1", "2", "3", "4","5","6","7","8","9","10"))
        self.cb_sem.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_sname = Entry(self.root)
        self.tb_sname.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_desc = Text(self.root,height=7, width=40)
        self.tb_desc.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        cr1 = db.conn.cursor()
        s1 = "select tid,tname from teacher"
        cr1.execute(s1)
        p1 = cr1.fetchall()
        lst_tname = []
        for i in range(0, len(p1)):
            a = str(p1[i][0])+"-" + p1[i][1]
            lst_tname.append(a)

        self.cb_teacher = Combobox(self.root,values=tuple(lst_tname),state='readonly')
        self.cb_teacher.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.bt1 = Button(self.root, text="submit", command=self.test, width=15, bg='white', fg='black').grid(row=6,column=1)

        self.root.mainloop()

    def test(self):
        if self.cb_course.get() == "" or self.cb_sem.get() == "" or self.tb_sname.get() == "" or self.tb_desc.get(0.1, END) == "" or self.cb_teacher.get() == "":
            showerror("", "Cannot Leave any field blank", parent=self.root)
        else:
            teacher = self.cb_teacher.get().split("-")
            tid=teacher[0]
            db = connection()
            cr = db.conn.cursor()
            query = "insert into subject values(null,'" + self.tb_sname.get() + "','" + self.tb_desc.get(0.1,END) + "','"+ str(tid) +"','"+ self.cb_course.get() + "','" + self.cb_sem.get() + "')"
            cr.execute(query)
            db.conn.commit()
            showinfo("Success", "Subject added successfully")

