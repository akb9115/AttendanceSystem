from tkinter.ttk import*
from tkinter import*
from tkinter.messagebox import*
from pymysql import*
from connection import *


class updatesubject:

    def search(self):
        if self.tb_sid.get()=="":
            showerror("","Please enter a subject id name to search")
        else:
            db=connection()
            query="select * from subject where sid='"+self.tb_sid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            db.conn.commit()
            if p==None:
                showinfo("",text="Subject id doesn't exist")
                self.tb_sname.delete(0, END)
                self.tb_desc.delete(0.1, END)
                self.cb_tid.delete(0, END)
                self.cb_cname.delete(0, END)
                self.cb_sem.delete(0, END)
            else:
                tid = p[3]
                s = "select tname from teacher where tid='"+str(tid)+"'"
                db = connection()
                cr1 = db.conn.cursor()
                cr1.execute(s)
                p1 = cr1.fetchone()
                tname = p1[0]
                teacher = str(tid)+"-"+ tname
                self.tb_sname.delete(0, END)
                self.tb_desc.delete(0.1, END)
                self.cb_tid.delete(0, END)
                self.cb_cname.delete(0, END)
                self.cb_sem.delete(0, END)
                self.tb_sname.insert(0, p[1])
                self.tb_desc.insert(0.1,p[2])
                self.cb_tid.set(teacher)
                self.cb_cname.set(p[4])
                self.cb_sem.set( p[5])


    def delete(self):
        if self.tb_sid.get()=="" or self.tb_sname.get()=="" or self.tb_desc.get()=="" or self.cb_tid.get(0.1,END)=="" or self.cb_cname.get()==""or self.tb_sem.get()=="":
            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            query="delete from subject where sid='"+self.tb_sid.get()+"'"
            cr=db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","course Deleted Successfully")

            self.tb_sname.delete(0, END)
            self.tb_desc.delete(0.1, END)
            self.cb_tid.delete(0, END)
            self.cb_cname.delete(0, END)
            self.cb_sem.delete(0, END)

    def update(self):
        if self.tb_sid.get() == "" or self.tb_sname.get() == "" or self.tb_desc.get() == "" or self.cb_tid.get() == "" or self.cb_cname.get() == "" or self.tb_sem.get() == "":

            showerror("","All fields are mandatory",parent=self.root)
        else:
            db=connection()
            cr = db.conn.cursor()
            query = "update subject set tid='" + self.cb_tid.get() + "',description='" + self.tb_desc.get(0.1,END)+"',sname='" + self.tb_sname.get()+"' where sid='" + self.tb_sid.get() + "'"

            cr.execute(query)
            db.conn.commit()
            showinfo("","Subject updated successfully")

    def __init__(self):

        self.root=Tk()
        self.root.geometry("650x300")
        self.root.configure(background='sky blue')
        self.root.title("UPDATE DETAILS")

        self.lb_heading=Label(self.root,text="UPDATE DETAILS",padx=5)
        Labelfont=('Arial','20','bold')
        self.lb_heading.configure(foreground='brown',background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=2)

        self.lb_sid =Label(self.root,text="Subject ID",background='sky blue',foreground='black').grid(row=1, column=0, sticky=(W))

        self.lb_name =Label(self.root,text="Subject name",background='sky blue',foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_desc = Label(self.root, text="Subject description", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_tid = Label(self.root, text="Teacher id", background='sky blue', foreground='black').grid(row=4, column=0, sticky=(W))
        self.lb_cname = Label(self.root, text="Course Name", background='sky blue', foreground='black').grid(row=5, column=0, sticky=(W))
        self.lb_sem=Label(self.root,text="Enter Semester",background='sky blue',foreground='black').grid(row=6, column=0, sticky=(W))



        self.tb_sid = Entry(self.root)

        self.tb_sid.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.tb_sname=Entry(self.root)

        self.tb_sname.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_desc=Text(self.root,width=30,height=6)
        self.tb_desc.grid(row=3, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_tid=Combobox(self.root,state='readonly')


        db=connection()
        cr1 = db.conn.cursor()
        s1 = "select tid,tname from teacher"
        cr1.execute(s1)
        p1 = cr1.fetchall()
        lst_tname = []
        for i in range(0, len(p1)):
            a = str(p1[i][0]) + "-" + p1[i][1]
            lst_tname.append(a)

        self.cb_tid.config(values=tuple(lst_tname))
        self.cb_tid.grid(row=4, column=1, padx=(5), pady=(5), sticky=(N, E, W))




        self.cb_cname = Combobox(self.root,state='readonly')
        db = connection()
        cr = db.conn.cursor()
        s = "select coursename from courses"
        cr.execute(s)
        p = cr.fetchall()
        lst_cname = []
        for i in range(0, len(p)):
            lst_cname.append(p[i][0])

        self.cb_sem = Combobox(self.root, state='readonly')
        self.l=[]
        for i in range (0,11):
            self.l.append(i)
            self.cb_sem.config(values=tuple(self.l))

        self.cb_cname.config(values=tuple(lst_cname))
        self.cb_cname.grid(row=5, column=1, padx=(5), pady=(5), sticky=(N, E, W))

        self.cb_sem.grid(row=6, column=1, padx=(5), pady=(5), sticky=(N, E, W))


        self.bt_find=Button(self.root,text="Find",command=self.search,borderwidth=3,width=12).grid(row=1,column=3)
        self.bt_update=Button(self.root,text="Update",command=self.update,borderwidth=3,width=12).grid(row=2,column=3)
        self.bt_delete=Button(self.root,text="Delete",command=self.delete,borderwidth=3,width=12).grid(row=3,column=3)

        self.root.mainloop()

#---------------------------------------------------

