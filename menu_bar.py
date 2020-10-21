from tkinter import *
from tkinter.ttk import *
from pymysql import *
from add_admin import *
from view_admin import *
from update import *
from department import *
from viewdept import *
from updatedept import  *
from courses import *
from viewcourses import *
from updatecourses import  *
from teachers import *
from viewteacher import *
from updateteacher import *
from subject import *
from viewsubject import *
from updatesubject import *
from student import *
from viewstudent import *
from updatestudent import *
from PIL import ImageTk,Image

def admin():
    x=Admin()

def view_admin():
    y=view()

def update_admin():
    z=alter()

def add_dept():
    a=department()

def view_dept():
    b=viewdept()

def update_dept():
    c = alterdept()

def add_course():
    p=courses()

def view_course():
    q=viewcourse()

def update_course():
    r=updatecourse()

def add_teacher():
    t1=teachers()

def view_teacher():
    t2=viewteacher()

def update_teacher():
    t3=updateteacher()

def add_sub():
    s1=subject()

def view_sub():
    s2=viewsubject()

def update_sub():
    s3=updatesubject()

def add_student():
    st1=student()

def view_student():
    st2=viewstudent()

def update_student():
    st3=updatestudent()





class menu:
    def logout(self):
        self.x.withdraw()

    def __init__(self):
        self.x= Tk()
        self.x.title("Menu")
        self.x.configure(background='white')

        self.x.geometry("+{}+{}".format(320, 200))

        path = "2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        lb = Label(self.x, image=img, height=400, width=900)
        lb.place(x=0, y=0)
        lb.pack()

        mymenu=Menu(self.x)
        self.x.config(menu=mymenu)
        option1=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Admins",menu=option1)
        option1.add_cascade(label="Add Admin",command=admin)
        option1.add_cascade(label="View Admin",command=view_admin)
        option1.add_cascade(label="Update Admin",command=update_admin)
        self.x.config(menu=mymenu)


        option2=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Departments",menu=option2)
        option2.add_cascade(label="Add Departments",command=add_dept)
        option2.add_cascade(label="View Departments",command=view_dept)
        option2.add_cascade(label="Update Departments",command=update_dept)
        self.x.config(menu=mymenu)


        option3=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Courses",menu=option3)
        option3.add_cascade(label="Add Courses",command=add_course)
        option3.add_cascade(label="View Courses",command=view_course)
        option3.add_cascade(label="Update Courses",command=update_course)
        self.x.config(menu=mymenu)

        option4=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Teacher",menu=option4)
        option4.add_cascade(label="Add Teacher",command=add_teacher)
        option4.add_cascade(label="View Teacher",command=view_teacher)
        option4.add_cascade(label="Update Teacher ",command=update_teacher)
        self.x.config(menu=mymenu)


        option5=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Subject",menu=option5)
        option5.add_cascade(label="Add Subject",command=add_sub)
        option5.add_cascade(label="View Subject",command=view_sub)
        option5.add_cascade(label="Update Subject ",command=update_sub)
        self.x.config(menu=mymenu)


        option6=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Manage Student",menu=option6)
        option6.add_cascade(label="Add Student",command=add_student)
        option6.add_cascade(label="View Student",command=view_student)
        option6.add_cascade(label="Update Student ",command=update_student)
        self.x.config(menu=mymenu)

        option7=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Options",menu=option7)
        option7.add_cascade(label="Exit",command=self.logout)
        self.x.config(menu=mymenu)

        self.x.mainloop()
