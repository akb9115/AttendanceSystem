from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class updateteacher:

    def search(self):
        if self.tb_tid.get()=="":
            showerror("","Please enter a Teacher ID to search")
        else:
            db=connection()
            query="select * from teacher where tid='"+self.tb_tid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            if p==None:
                showinfo("",text="teacher doesn't exist")
                self.tb_tname.delete(0, END)
                self.tb_mobileno.delete(0, END)
                self.tb_address.delete(0, END)
                self.cb_gen.delete(0, END)
                self.cb_qual.delete(0, END)
                self.cb_exp.delete(0, END)
                self.tb_email.delete(0, END)
                self.tb_pass.delete(0, END)
            else:
                self.tb_tname.delete(0, END)
                self.tb_mobileno.delete(0, END)
                self.tb_address.delete(0, END)
                self.cb_gen.delete(0, END)
                self.cb_qual.delete(0, END)
                self.cb_exp.delete(0, END)
                self.tb_email.delete(0, END)
                self.tb_pass.delete(0, END)

                self.tb_tname.insert(0, p[1])
                self.tb_mobileno.insert(0, p[2])
                self.tb_address.insert(0, p[3])
                self.cb_gen.insert(0, p[4])
                self.cb_qual.insert(0, p[5])
                self.cb_exp.insert(0, p[6])
                self.tb_email.insert(0, p[7])
                self.tb_pass.insert(0, p[8])


    def delete(self):
        if self.tb_tname.get() == "" or self.tb_mobileno.get() == "" or self.tb_address.get() == "" or self.cb_gen.get() == "" or self.cb_qual.get() == "" or self.cb_exp.get() == "" or self.tb_email.get() == "" or self.tb_pass.get() == "":

            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from teacher where tid='"+self.tb_tid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","Teacher Deleted Successfully")
            self.tb_tname.delete(0, END)
            self.tb_mobileno.delete(0, END)
            self.tb_address.delete(0, END)
            self.cb_gen.delete(0, END)
            self.cb_qual.delete(0, END)
            self.cb_exp.delete(0, END)
            self.tb_email.delete(0, END)
            self.tb_pass.delete(0, END)

    def update(self):
        self.x = int(self.tb_email.get().count("@"))
        self.d = int(self.tb_email.get().count("."))

        if self.tb_tname.get() == "" or self.tb_mobileno.get() == "" or self.tb_address.get() == "" or self.cb_gen.get() == "" or self.cb_qual.get() == "" or self.cb_exp.get() == "" or self.tb_email.get() == "" or self.tb_pass.get() == "":

            showerror("","All fields are mandatory",parent=self.root)

        elif self.tb_mobileno.get().isalpha() == True:
            showerror("", "Mobile number not valid")

        elif self.x != 1 and self.tb_email.get()!=""  and self.d != 1 :
            showerror("", "Wrong Email", parent=self.root)

        else:
            db=connection()
            cr = db.conn.cursor()
            query = "update teacher set tname='" + self.tb_tname.get() + "',mobileno='" + self.tb_mobileno.get() + "',address='" + self.tb_address.get() + "', gender='"+self.cb_gen.get() +"',qualification='"+self.cb_qual.get()+ "',experience='"+self.cb_exp.get()+ "',email='"+self.tb_email.get()+ "',password='"+ self.tb_pass.get()+"' where tid='" + self.tb_tid.get() + "'"

            cr.execute(query)
            db.conn.commit()
            showinfo("","Teacher updated successfully")


    def __init__(self):

        self.root=Tk()
        self.root.geometry("650x300")
        self.root.configure(background='sky blue')
        self.root.title("UPDATE DETAILS")

        self.lb_heading=Label(self.root,text="UPDATE DETAILS",padx=5)
        Labelfont=('Arial','20','bold')
        self.lb_heading.configure(foreground='brown',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=2)

        self.lb_tid = Label(self.root, text="Enter Teacher ID", background='sky blue', foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_tname = Label(self.root, text="Enter Teacher Name", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_mobileno = Label(self.root, text="Enter Mobile no", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_address = Label(self.root, text='Enter Address', background='sky blue', foreground='black').grid(row=4,column=0,sticky=(W))
        self.lb_gen = Label(self.root, text="Select Gender", background='sky blue', foreground='black').grid(row=5,column=0,sticky=(W))
        self.lb_qual = Label(self.root, text="Select Qualification", background='sky blue', foreground='black').grid(row=6, column=0, sticky=(W))
        self.lb_exp = Label(self.root, text="Select Experience", background='sky blue', foreground='black').grid(row=7,column=0,sticky=( W))
        self.lb_email = Label(self.root, text='Enter Email ID', background='sky blue', foreground='black').grid(row=8,column=0,sticky=(W))
        self.lb_pass = Label(self.root, text="Enter Password", background='sky blue', foreground='black').grid(row=9,column=0,sticky=(W))

        self.tb_tid=Entry(self.root)
        self.tb_tname = Entry(self.root)
        self.tb_mobileno = Entry(self.root)
        self.tb_address = Entry(self.root)
        self.cb_gen = Combobox(self.root, values=('Female', 'Male'))
        self.cb_qual = Combobox(self.root, values=('B.tech', 'M.tech', 'BCA', 'MCA'))
        self.cb_exp = Combobox(self.root, values=('1 year', '2 year', '3 year', '4 year', '5 year',))
        self.tb_email = Entry(self.root)
        self.tb_pass = Entry(self.root)

        self.tb_tid.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_tname.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_mobileno.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_address.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_gen.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_qual.grid(row=6, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_exp.grid(row=7, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_email.grid(row=8, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_pass.grid(row=9, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.bt_find = Button(self.root, text="Find", command=self.search, borderwidth=3, width=12).grid(row=1,column=3)
        self.bt_update = Button(self.root, text="Update", command=self.update, borderwidth=3, width=12).grid(row=2,column=3)
        self.bt_delete = Button(self.root, text="Delete", command=self.delete, borderwidth=3, width=12).grid(row=3,column=3)

        self.root.mainloop()

