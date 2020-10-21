from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class alterdept:

    def search(self):
        if self.tb_dept.get()=="":
            showerror("","Please enter a department name to search")
        else:
            db=connection()
            query="select * from department where deptname='"+self.tb_dept.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            if p==None:
                showinfo("",text="Department doesn't exist")
            else:
                self.tb_hod.delete(0,END)
                self.tb_desc.delete(0.1,END)
                self.tb_hod.insert(0,p[1])
                self.tb_desc.insert(0.1,p[2])


    def delete(self):
        if self.tb_dept.get()=="" or self.tb_hod.get()=="" or self.tb_desc.get(0.1,END)=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from department where deptname='"+self.tb_dept.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","department Deleted Successfully")

    def update(self):
        if self.tb_dept.get()=="" or self.tb_hod.get()=="" or self.tb_desc.get(0.1,END)=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            cr = db.conn.cursor()
            query = "update department set hodname='" + self.tb_hod.get() + "',description='" + self.tb_desc.get(0.1,END) + "' where deptname='" + self.tb_dept.get() + "'"

            cr.execute(query)
            db.conn.commit()
            showinfo("","Department updated successfully")

    def __init__(self):

        self.root=Tk()
        self.root.geometry("650x300")
        self.root.configure(background='sky blue')
        self.root.title("UPDATE DETAILS")

        self.lb_heading=Label(self.root,text="UPDATE DETAILS",padx=5)
        Labelfont=('Arial','20','bold')
        self.lb_heading.configure(foreground='brown',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=2)

        self.lb_dept=Label(self.root,text="Enter department Name",background="sky blue",foreground="black").grid(row=1,column=0,sticky=(W))
        self.lb_hod=Label(self.root,text="Enter HOD Name",background="sky blue",foreground="black").grid(row=2,column=0,sticky=(W))
        self.lb_desc=Label(self.root,text="Enter Description",background="sky blue",foreground="black").grid(row=3,column=0,sticky=(W))


        self.tb_dept=Entry(self.root,borderwidth=2,width=50)
        self.tb_hod = Entry(self.root, borderwidth=2, width=50)


        self.tb_desc=Text(self.root,borderwidth=2,width=50,height=7)

        self.tb_dept.grid(row=1,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.tb_hod.grid(row=2,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.tb_desc.grid(row=3,column=1,padx=5,pady=5,sticky=(N,E,W))





        self.bt_find=Button(self.root,text="Find",command=self.search,borderwidth=3,width=12).grid(row=1,column=3)
        self.bt_update=Button(self.root,text="Update",command=self.update,borderwidth=3,width=12).grid(row=2,column=3)
        self.bt_delete=Button(self.root,text="Delete",command=self.delete,borderwidth=3,width=12).grid(row=3,column=3)

        self.root.mainloop()

#---------------------------------------------------

