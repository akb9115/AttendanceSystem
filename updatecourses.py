from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class updatecourse:

    def search(self):
        if self.tb_cname.get()=="":
            showerror("","Please enter a course name to search")
        else:
            db=connection()
            query="select * from courses where coursename='"+self.tb_cname.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            if p==None:
                showinfo("",text="Course doesn't exist")
                self.cb_duration.delete(0, END)
                self.tb_desc.delete(0.1, END)
                self.cb_dept.delete(0, END)
            else:
                self.cb_duration.delete(0,END)
                self.tb_desc.delete(0.1,END)
                self.cb_dept.delete(0,END)

                self.cb_dept.set(p[3])
                self.cb_duration.insert(0,p[1])
                self.tb_desc.insert(0.1,p[2])


    def delete(self):
        if self.cb_dept.get()=="" or self.tb_cname.get()=="" or self.cb_duration.get()=="" or self.tb_desc.get(0.1,END)=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from courses where coursename='"+self.tb_cname.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","course Deleted Successfully")
            self.cb_duration.delete(0, END)
            self.tb_desc.delete(0.1, END)
            self.cb_dept.delete(0, END)

    def update(self):
        if self.cb_dept.get() == "" or self.tb_cname.get() == "" or self.cb_duration.get() == "" or self.tb_desc.get(0.1, END) == "":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            cr = db.conn.cursor()
            query = "update courses set department='" + self.cb_dept.get() + "',duration='" + self.cb_duration.get() + "',description='" + self.tb_desc.get(0.1,END)+"' where coursename='" + self.tb_cname.get() + "'"

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


        self.lb_dept =Label(self.root,text="Select Departments",background='sky blue',foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_cname = Label(self.root, text="Enter Course Name", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_duration = Label(self.root, text="Enter Duration", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_desc=Label(self.root,text="Enter Description",background='sky blue',foreground='black').grid(row=4, column=0, sticky=(W))



        self.cb_dept = Combobox(self.root, state='readonly')

        db = connection()
        cr = db.conn.cursor()
        s = "select deptname from department"
        cr.execute(s)
        p = cr.fetchall()
        lst_deptname = []
        for i in range(0, len(p)):
            lst_deptname.append(p[i][0])

        self.cb_dept.config(values=tuple(lst_deptname))
        self.cb_dept.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_cname = Entry(self.root)
        self.tb_cname.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_duration = Combobox(self.root, values=("1 Year", "2 Year", "3 Year", "4 Year", "5 Year"))
        self.cb_duration.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_desc = Text(self.root, height=7, width=40)
        self.tb_desc.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.bt_find=Button(self.root,text="Find",command=self.search,borderwidth=3,width=12).grid(row=1,column=3)
        self.bt_update=Button(self.root,text="Update",command=self.update,borderwidth=3,width=12).grid(row=2,column=3)
        self.bt_delete=Button(self.root,text="Delete",command=self.delete,borderwidth=3,width=12).grid(row=3,column=3)

        self.root.mainloop()

#---------------------------------------------------

