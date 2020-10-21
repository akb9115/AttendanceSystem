from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class updatestudent:

    def search(self):
        if self.tb_studentid.get()=="":
            showerror("","Please enter a Student ID to search")
        else:
            db=connection()
            query="select * from student where studentid='"+self.tb_studentid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            if p==None:
                showinfo("",text="teacher doesn't exist")
                self.tb_roll.delete(0, END)
                self.tb_sname.delete(0, END)
                self.cb_course.delete(0, END)
                self.cb_gen.delete(0, END)
                self.tb_fname.delete(0, END)
                self.tb_mobile.delete(0, END)
                self.tb_pmobile.delete(0, END)
                self.tb_address.delete(0, END)
                self.tb_paddress.delete(0, END)
                self.tb_email.delete(0, END)
                self.cb_sem.delete(0, END)
            else:
                self.tb_roll.delete(0, END)
                self.tb_sname.delete(0, END)
                self.cb_course.delete(0, END)
                self.tb_fname.delete(0, END)
                self.tb_mobile.delete(0, END)
                self.tb_pmobile.delete(0, END)
                self.tb_address.delete(0, END)
                self.tb_paddress.delete(0, END)
                self.tb_email.delete(0, END)


                self.tb_roll.insert(0, p[1])
                self.tb_sname.insert(0,p[2])
                self.cb_course.insert(0,p[5])
                self.cb_gen.set(p[4])
                self.tb_fname.insert(0,p[3])
                self.tb_mobile.insert(0,p[7])
                self.tb_pmobile.insert(0,p[10])
                self.tb_address.insert(0,p[8])
                self.tb_paddress.insert(0,p[11])
                self.tb_email.insert(0,p[9])
                self.cb_sem.set(p[6])


    def delete(self):
        if self.tb_studentid.get() == "" or self.tb_roll.get() == "" or self.tb_sname.get() == "" or self.cb_course.get() == "" or self.cb_gen.get() == "" or self.cb_sem.get() == "" or self.tb_mobile.get() == "" or self.tb_pmobile.get() == "" or self.tb_fname.get() == "" or self.cb_sem.get() == "" or self.tb_email.get() == "" or self.tb_address.get() == "" or self.tb_paddress.get() == "":

            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from student where studentid='"+self.tb_studentid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","Subject Deleted Successfully")
            self.tb_roll.delete(0, END)
            self.tb_sname.delete(0, END)
            self.cb_course.delete(0, END)
            self.cb_gen.delete(0, END)
            self.tb_fname.delete(0, END)
            self.tb_mobile.delete(0, END)
            self.tb_pmobile.delete(0, END)
            self.tb_address.delete(0, END)
            self.tb_paddress.delete(0, END)
            self.tb_email.delete(0, END)
            self.cb_sem.delete(0, END)


    def update(self):
        self.x = int(self.tb_email.get().count("@"))
        self.d = int(self.tb_email.get().count("."))

        if self.tb_studentid.get() == "" or self.tb_roll.get() == "" or self.tb_sname.get() == "" or self.cb_course.get() == "" or self.cb_gen.get() == "" or self.cb_sem.get() == "" or self.tb_mobile.get() == "" or self.tb_pmobile.get() == "" or self.tb_fname.get() == "" or self.cb_sem.get() == "" or self.tb_email.get() == "" or self.tb_address.get() == "" or self.tb_paddress.get() == "":

            showerror("","All fields are mandatory",parent=self.root)

        elif self.tb_mobile.get().isalpha() == True:
            showerror("", "Mobile number not valid")

        elif self.tb_pmobile.get().isalpha() == True:
            showerror("", "Mobile number not valid")


        elif self.x != 1 and self.tb_email.get()!=""  and self.d != 1 :
            showerror("", "Wrong Email", parent=self.root)

        else:
            db=connection()
            cr = db.conn.cursor()
            query = "update student set rollno='" + self.tb_roll.get() + "',studentname='" + self.tb_sname.get() + "',fname='" + self.tb_fname.get() + "', gender='"+self.cb_gen.get() +"',course='"+self.cb_course.get()+ "',semester='"+self.cb_sem.get()+ "',mobileno='"+self.tb_mobile.get()+ "',pmobileno='"+self.tb_pmobile.get()+"',email='"+self.tb_email.get()+ "',paddress='"+self.tb_paddress.get()+"',address='"+ self.tb_address.get()+"' where studentid='" + self.tb_studentid.get() + "'"

            cr.execute(query)
            db.conn.commit()
            showinfo("","Subject updated successfully")


    def __init__(self):

        self.root=Tk()
        self.root.geometry("650x300")
        self.root.configure(background='sky blue')
        self.root.title("UPDATE DETAILS")

        self.lb_heading=Label(self.root,text="UPDATE DETAILS",padx=8)
        Labelfont=('Arial','20','bold')
        self.lb_heading.configure(foreground='brown',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=2)

        self.lb_studentid = Label(self.root, text="Enter Student ID", background='sky blue', foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_rollno = Label(self.root, text="Enter Rollno", background='sky blue', foreground='black').grid(row=2,column=0,sticky=(W))
        self.lb_studentname = Label(self.root, text="Enter Student name", background='sky blue',foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_course = Label(self.root, text='Select Course', background='sky blue', foreground='black').grid(row=4,column=0,sticky=(W))
        self.lb_gen = Label(self.root, text="Select Gender", background='sky blue', foreground='black').grid(row=5,column=0,sticky=(W))
        self.lb_mobileno = Label(self.root, text="Enter Mobileno ", background='sky blue', foreground='black').grid(row=6, column=0, sticky=(W))
        self.lb_pmobileno = Label(self.root, text="Parent Mobileno", background='sky blue', foreground='black').grid(row=7, column=0, sticky=(W))
        self.lb_fname = Label(self.root, text='Enter Father Name', background='sky blue', foreground='black').grid(row=2, column=2, sticky=(E))
        self.lb_semester = Label(self.root, text="Select Semester", background='sky blue', foreground='black').grid(row=3, column=2, sticky=(E))
        self.lb_email = Label(self.root, text="Enter Email", background='sky blue', foreground='black').grid(row=4,column=2,sticky=(E))
        self.lb_address = Label(self.root, text="Enter Address", background='sky blue', foreground='black').grid(row=5,column=2,sticky=(E))
        self.lb_paddress = Label(self.root, text="Enter Permanent Address", background='sky blue',foreground='black').grid(row=6, column=2, sticky=(E))

        self.tb_studentid=Entry(self.root)
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
        self.cb_gen = Combobox(self.root, values=('Female', 'Male'), state='readonly')
        self.cb_sem = Combobox(self.root, state='readonly')

        self.lst_sem = []
        for i in range(1, 11):
            self.lst_sem.append(i)

        self.cb_sem.config(values=tuple(self.lst_sem))
        self.tb_mobile = Entry(self.root)
        self.tb_pmobile = Entry(self.root)
        self.tb_fname = Entry(self.root)
        self.tb_email = Entry(self.root)
        self.tb_address = Entry(self.root)
        self.tb_paddress = Entry(self.root)

        self.tb_studentid.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.tb_roll.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_sname.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_course.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_gen.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_mobile.grid(row=6, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_pmobile.grid(row=7, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_fname.grid(row=2, column=3, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_sem.grid(row=3, column=3, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_email.grid(row=4,column=3,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_address.grid(row=5,column=3,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_paddress.grid(row=6,column=3,padx=(5),pady=(5),sticky=(N,E,W))


        self.bt_find = Button(self.root, text="Find", command=self.search, borderwidth=3, width=12).grid(row=2,column=5)
        self.bt_update = Button(self.root, text="Update", command=self.update, borderwidth=3, width=12).grid(row=3,column=5)
        self.bt_delete = Button(self.root, text="Delete", command=self.delete, borderwidth=3, width=12).grid(row=4,column=5)

        self.root.mainloop()
