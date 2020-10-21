from tkinter.ttk import *
from tkinter import *
from pymysql import *
from tkinter.messagebox import *
from connection import *
import shutil
from tkinter import filedialog
# from teacherlogin import *
from tkcalendar import DateEntry
from manageattendance import *
from datetime import datetime
import http.client


class count_attendance:


    def getstudent(self,event):
        if self.cb_course.get()!="" and self.cb_sem.get()!="":
            db = connection()
            cr = db.conn.cursor()
            s = "select studentid,studentname from student where course='" + self.cb_course.get() + "' and semester='" + self.cb_sem.get() + "'"
            cr.execute(s)
            p = cr.fetchall()
            self.lst_s = []
            for i in range(0, len(p)):
                a = str(p[i][0])+"-"+p[i][1]
                self.lst_s.append(a)
            self.cb_student.config(values=tuple(self.lst_s))

    def show_attendance(self):
        db=connection()
        cr=db.conn.cursor()
        abc = self.cb_student.get().split("-")
        global sid
        sid = abc[0]

        global fromdate
        global todate
        fromdate = datetime.strptime(self.tb_from.get(),"%Y-%m-%d").strftime('%Y-%m-%d')
        todate = datetime.strptime(self.tb_to.get(),"%Y-%m-%d").strftime('%Y-%m-%d')

        s = "select rollno,pmobileno from student where studentid='" + str(sid) +  "' and course='"+ self.cb_course.get() +"' and semester='"+ str(self.cb_sem.get()) +"'"
        cr.execute(s)
        p2=cr.fetchone()
        parent_mobileno = p2[1]
        self.lb_roll2 = Label(self.root, text=p2[0], background='sky blue', foreground='black').grid(row=3,column=1,sticky=(W))

        s1 = "Select count(*) from attendancetable where course='"+ self.cb_course.get()+"' and semester='"+ str(self.cb_sem.get()) +"' and sid='"+ str(sid) +"' and date1>='"+ str(fromdate) +"' and date1<='"+ str(todate) +"'"
        cr1 = db.conn.cursor()
        cr1.execute(s1)
        p3 = cr1.fetchone()
        global attendance_percentage
        noofdayspresent = p3[0]
        attendance_percentage = str(int(noofdayspresent)*100/30)+ " %"
        self.lb_att2 = Label(self.root,text=p3[0]).grid(row=4,column=1,sticky=(W))
        self.lb_per2 = Label(self.root,text=attendance_percentage).grid(row=5,column=1,sticky=(W))

    def send_sms(self):

        abc = self.cb_student.get().split("-")
        name = abc[1]

        db=connection()
        cr=db.conn.cursor()
        s2 = "Select pmobileno from student where studentname='" + name + "'"
        cr.execute(s2)
        p=cr.fetchone()
        pmobile=p[0]
        db.conn.commit()
        conn = http.client.HTTPConnection("server1.vmm.education")
        textmessage = "The attendance of your child "+name+" from "+str(fromdate)+" to "+str(todate)+" is "+attendance_percentage
        textmessage = textmessage.replace(" ", "%20")
        conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?username=dhk_py&password=GNEP0QCE&message=" + textmessage + "&phone_numbers=" + "8054889286")
        response = conn.getresponse()



    def __init__(self):

        self.root = Tk("COUNT ATTENDANCE")
        self.root.configure(bg='sky blue')
        self.root.geometry("1000x200")
        self.root.title("COUNT ATTENDANCE")

        self.lb_heading = Label(self.root, text='TEACHER LOGIN')
        Labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground="black",background='sky blue',font=Labelfont)
        self.lb_heading.grid(row=0, column=1)



        self.lb_from = Label(self.root, text="From", background='sky blue', foreground='black').grid(row=1, column=0, sticky=(W))
        self.lb_to = Label(self.root, text="To", background='sky blue', foreground='black').grid(row=1, column=3, sticky=(W))

        self.lb_course = Label(self.root, text="Course", background='sky blue', foreground='black').grid(row=2, column=0, sticky=(W))
        self.lb_sem = Label(self.root, text="Semester", background='sky blue', foreground='black').grid(row=2, column=3, sticky=(W))
        self.lb_student = Label(self.root, text="Student", background='sky blue', foreground='black').grid(row=2, column=5, sticky=(W))
        self.lb_roll = Label(self.root, text="Student Roll no ", background='sky blue', foreground='black').grid(row=3, column=0, sticky=(W))
        self.lb_att = Label(self.root, text="No of Days Present ", background='sky blue', foreground='black').grid(row=4, column=0, sticky=(W))
        self.lb_per = Label(self.root, text="Attendance Percentage ", background='sky blue', foreground='black').grid(row=5, column=0, sticky=(W))


        self.bt_find=Button(self.root,text="Send sms",command=self.send_sms,borderwidth=3,width=12).grid(row=6,column=2)
        self.bt1_find=Button(self.root,text="Go",borderwidth=3,width=12,command=self.show_attendance).grid(row=2,column=7)


        self.tb_from = DateEntry(self.root)

        self.tb_to = DateEntry(self.root)
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
        self.cb_sem = Combobox(self.root)
        self.lst_sem = []
        for i in range(1, 11):
            self.lst_sem.append(i)
        self.cb_sem.config(values=tuple(self.lst_sem))

        self.cb_student = Combobox(self.root)

        self.cb_course.bind("<<ComboboxSelected>>",self.getstudent)
        self.cb_sem.bind("<<ComboboxSelected>>",self.getstudent)

        self.cb_course.grid(row=2, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_sem.grid(row=2, column=4, padx=(5), pady=(5), sticky=(N, E, W))
        self.cb_student.grid(row=2, column=6, padx=(5), pady=(5), sticky=(N, E, W))

        self.tb_from.grid(row=1, column=1, padx=(5), pady=(5), sticky=(N, E, W))
        self.tb_to.grid(row=1, column=4, padx=(5), pady=(5), sticky=(N, E, W))

        self.root.mainloop()


x=count_attendance()