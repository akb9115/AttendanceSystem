from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class alter:

    def search(self):

        db=connection()

        query="select * from admins where email='"+self.tb_email.get()+"'"
        cr=db.conn.cursor()
        cr.execute(query)
        p=cr.fetchone()
        a=(self.tb_email.get()).count('@')
        b=(self.tb_email.get()).count('.')

        if self.tb_email.get() == "":
            showerror("", "Please provide an email to search", parent=self.root)
        elif p==None:
            showinfo("","Email not found",parent=self.root)
        elif a==0 and b==0:
            showinfo("","Invalid Email",parent=self.root)
        else:
            self.tb_password.insert(0,p[1])
            self.tb_mobile.insert(0,p[2])
            self.cb_type.set(p[3])

    def delete(self):
        if self.tb_email.get()=="" or self.tb_password.get()=="" or self.tb_mobile.get()=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from admins where email='"+self.tb_email.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","Admin Deleted Successfully")

    def update(self):
        if self.tb_email.get()=="" or self.tb_password.get()=="" or self.tb_mobile.get()=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            cr = db.conn.cursor()
            query="update admins set password='"+self.tb_password.get()+"',mobile='"+self.tb_mobile.get()+"',type='"+self.cb_type.get()+"' where email='"+self.tb_email.get()+"'"

            cr.execute(query)
            db.conn.commit()
            showinfo("","update successfully")

    def __init__(self):

        self.root=Tk()
        self.root.geometry("470x200")
        self.root.configure(background='sky blue')
        self.root.title("UPDATE DETAILS")

        self.lb_heading=Label(self.root,text="UPDATE DETAILS",padx=5)
        Labelfont=('Arial','20','bold')
        self.lb_heading.configure(foreground='brown',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=2)

        self.lb_email=Label(self.root,text="E-mail",background="sky blue",foreground="black").grid(row=1,column=0,sticky=(W))
        self.lb_password=Label(self.root,text="Password",background="sky blue",foreground="black").grid(row=2,column=0,sticky=(W))
        self.lb_mobile=Label(self.root,text="Mobile",background="sky blue",foreground="black").grid(row=3,column=0,sticky=(W))
        self.lb_type=Label(self.root,text="Type",background="sky blue",foreground="black").grid(row=4,column=0,sticky=(W))

        self.tb_email=Entry(self.root,borderwidth=2,width=50)
        self.tb_email.grid(row=1,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.tb_password=Entry(self.root,borderwidth=2,width=50)
        self.tb_password.grid(row=2,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.tb_mobile=Entry(self.root,borderwidth=2,width=50)
        self.tb_mobile.grid(row=3,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.cb_type=Combobox(self.root,state="readonly",values=("admin","Limited"))
        self.cb_type.grid(row=4,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.bt_find=Button(self.root,text="Find",command=self.search,borderwidth=3,width=12).grid(row=1,column=3)
        self.bt_update=Button(self.root,text="Update",command=self.update,borderwidth=3,width=12).grid(row=2,column=3)
        self.bt_delete=Button(self.root,text="Delete",command=self.delete,borderwidth=3,width=12).grid(row=3,column=3)

        self.root.mainloop()

#---------------------------------------------------

