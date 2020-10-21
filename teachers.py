from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from connection import *

class teachers:

    def __init__(self):

        self.root = Tk("TEACHER INFO")
        self.root.configure(bg='sky blue')
        self.root.geometry("450x290")
        self.root.title("Teacher")

        self.lb_heading = Label(self.root, text='ADD TEACHER', padx=110)
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='black', background='sky blue', font=Labelfont)
        self.lb_heading.grid(row=0, column=0, columnspan=3)

        self.lb_tname =Label(self.root,text="Enter Teacher Name",background='sky blue',foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_mobileno = Label(self.root, text="Enter Mobile no", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_address=Label(self.root,text='Enter Address',background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_gen = Label(self.root, text="Select Gender", background='sky blue', foreground='black').grid(row=4, column=0, sticky=(W))
        self.lb_qual=Label(self.root,text="Select Qualification",background='sky blue',foreground='black').grid(row=5, column=0, sticky=(W))
        self.lb_exp = Label(self.root, text="Select Experience", background='sky blue', foreground='black').grid(row=6, column=0, sticky=(W))
        self.lb_email=Label(self.root,text='Enter Email ID',background='sky blue', foreground='black').grid(row=7, column=0, sticky=(W))
        self.lb_pass = Label(self.root, text="Enter Password", background='sky blue', foreground='black').grid(row=8, column=0, sticky=(W))

        self.tb_tname = Entry(self.root)
        self.tb_mobileno = Entry(self.root)
        self.tb_address = Entry(self.root)
        self.cb_gen=Combobox(self.root,values=('Female','Male'))
        self.cb_qual = Combobox(self.root, values=('B.tech', 'M.tech','BCA','MCA'))
        self.cb_exp = Combobox(self.root, values=('1 year', '2 year','3 year','4 year','5 year', ))
        self.tb_email = Entry(self.root)
        self.tb_pass = Entry(self.root)

        self.tb_tname.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_mobileno.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_address.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_gen.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_qual.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_exp.grid(row=6, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_email.grid(row=7, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_pass.grid(row=8, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.bt1 = Button(self.root, text="submit", command=self.test, width=15, bg='white', fg='black').grid(row=9,column=1)

        self.root.mainloop()

    def test(self):

        self.x = int(self.tb_email.get().count("@"))
        self.d = int(self.tb_email.get().count("."))

        if self.tb_tname.get() == "" or self.tb_mobileno.get() == "" or self.tb_address.get() == "" or self.cb_gen.get() == "" or self.cb_qual.get() == "" or self.cb_exp.get() == "" or self.tb_email.get() == "" or self.tb_pass.get() == "":
            showerror("", "Cannot Leave any field blank", parent=self.root)

        elif self.tb_mobileno.get().isalpha() == True:
            showerror("", "Mobile number not valid")

        elif self.x != 1 or self.tb_email.get() == "" or self.d != 1:
            showerror("", "Wrong Email", parent=self.root)




        else:
            db = connection()
            cr = db.conn.cursor()
            query = "insert into teacher values(null,'"+ self.tb_tname.get() + "','" + self.tb_mobileno.get() + "','" + self.tb_address.get() + "','" + self.cb_gen.get() +  "','" + self.cb_qual.get() + "','" + self.cb_exp.get() + "','" + self.tb_email.get() + "','" + self.tb_pass.get() + "')"
            cr.execute(query)
            db.conn.commit()
            showinfo("Success", "Teacher added successfully")


