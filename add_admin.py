from tkinter.ttk import*
from tkinter import *
from tkinter.messagebox import *
from pymysql import *



class Admin:

    def __init__(self):

        self.root = Tk("ADMIN")
        self.root.configure(bg='sky blue')
        self.root.geometry("300x250")
        self.root.title("Admin page")

        self.lb_heading=Label(self.root,text='ADD ADMIN',padx=70)
        Labelfont=('Arial',20,'bold')
        self.lb_heading.configure(foreground='black',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0,column=0,columnspan=3)

        self.lb_email = Label(self.root, text="Email",background='sky blue',foreground='black')
        self.lb_pass = Label(self.root, text="password",background='sky blue',foreground='black')
        self.lb_cpass = Label(self.root, text="Confirm password",background='sky blue',foreground='black')
        self.lb_mobile= Label(self.root, text="Mobile",background='sky blue',foreground='black')
        self.lb_type= Label(self.root, text="Type",background='sky blue',foreground='black')

        self.tb_email = Entry(self.root)
        self.tb_pass = Entry(self.root, show="*")
        self.tb_cpass = Entry(self.root, show="*")
        self.tb_mobile = Entry(self.root)

        self.cb_type = Combobox(self.root, state="readonly", values=("admin", "limited"))

        self.bt = Button(self.root, text="submit", command=self.test,width=15,bg='white',fg='black').grid(row=6, column=1)

        self.lb_email.grid(row=1, column=0,sticky=(W))
        self.lb_pass.grid(row=2, column=0,sticky=(W))
        self.lb_cpass.grid(row=3, column=0,sticky=(W))
        self.lb_mobile.grid(row=4, column=0,sticky=(W))
        self.lb_type.grid(row=5, column=0,sticky=(W))

        self.tb_email.grid(row=1,column=1,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_pass.grid(row=2,column=1,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_cpass.grid(row=3,column=1,padx=(5),pady=(5),sticky=(N,E,W))
        self.tb_mobile.grid(row=4,column=1,padx=(5),pady=(5),sticky=(N,E,W))

        self.cb_type.grid(row=5,column=1,padx=(5),pady=(5),sticky=(N,E,W))

        self.root.mainloop()


    def test(self):

        self.k=0
        self.x = int(self.tb_email.get().count("@"))
        self.d = int(self.tb_email.get().count("."))

        if self.tb_email.get()=="" or self.tb_pass.get()=="" or self.tb_cpass.get()=="" or self.tb_mobile.get()=="":
            showerror("","Cannot Leave any field blank",parent=self.root)
            self.k=1

        elif self.tb_pass.get()!=self.tb_cpass.get():
            showerror("","Password don't match",parent=self.root)
            self.k=1



        elif self.x!=1 and self.tb_email.get()!="" and self.d==1:
            showerror("","Wrong Email('@' is missing)",parent=self.root)
            self.k=1


        elif self.d!=1 and self.tb_email.get()!="" and self.x==1:
            showerror("","Wrong email('.'is missing)",parent=self.root)
            self.k=1

        if self.k==0:
            self.conn = connect("127.0.0.1", "root", "", "type1")
            cr = self.conn.cursor()
            query = "insert into admins values('" + self.tb_email.get() + "','" + self.tb_pass.get() + "','" + self.tb_mobile.get() + "','" + self.cb_type.get() + "')"
            cr.execute(query)
            self.conn.commit()
            showinfo("Success", "Admin added successfully")




