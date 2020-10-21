import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pymysql
import Pmw
import shutil
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
from datetime import datetime
from connection import *
import http.client
# user defined classes


class frm_mark_attandence(Toplevel):
    global con
    dc1 = dict()
    course = ""
    sem = ""
    sname = ""
    sid=0

    def getallsubjects(self, TEACHERID):
        dct_temp = dict()
        db = connection()
        cursor = db.conn.cursor()
        s = "select * from subject where tid='" + str(TEACHERID) + "' order by sname"
        cursor.execute(s)
        result = cursor.fetchall()
        i = 0
        k = 1
        for row in result:
            dct_temp[row[1]] = row[0]
        return dct_temp

    def mark_attendance(self):
        studentid = ""
        global course,sem,sid
        for r in self.myvarlst:
            print(r.get())

        print("Len is ",len(self.myvarlst))

        date1 = str(self.txt3.get())
        d2 = datetime.strptime(date1, "%Y-%m-%d").strftime('%Y-%m-%d')
        d2 = datetime.strptime(d2, "%Y-%m-%d")

        for g in range(0,len(self.myvarlst)):
            # print(self.myvarlst[g].get())
            if self.myvarlst[g].get()==1:
                studentid=self.sidlst[g]
                db = connection()
                # cursor = db.conn.cursor()
                s2 = "insert into attendancetable (sid,course,semester,date1,subjectid) values ('" + str(studentid) + "','" + course + "','" + str(sem) + "','" + str(d2) + "','"+str(sid)+"')"
                print(s2)
                res = db.conn.cursor()
                res.execute(s2)
                s1 = "select mobileno from student where studentid='"+ str(studentid) +"'"
                rs = db.conn.cursor()
                rs.execute(s1)
                p1 = rs.fetchone()
                mob = p1[0]
                db.conn.commit()
                msg = "Your attendence is marked present on " + str(d2)
                msg = msg.replace(" ","%20")
                conn = http.client.HTTPConnection("server1.vmm.education")
                conn.request('GET',
                             "/VMMCloudMessaging/AWS_SMS_Sender?username=ExamSystem&password=S4J5LT3C&message=" + msg + "&phone_numbers=" + mob)
                response = conn.getresponse()
                print(response.read())
        tkinter.messagebox.showinfo("Python", "Attendance Marked Successfully", parent=self)



    def getstudentdata(self):
        global dc1,course,sem,sid
        sid = dc1[self.cmb1.get()]
        course = ""
        sem = ""
        self.c = ""
        self.chkboxlst = []
        self.v=dict()
        self.sidlst = []
        lstrollno = []
        lstsname = []
        lstmobileno = []
        lstpmobileno = []
        self.myvarlst = []

        db = connection()
        cursor1 = db.conn.cursor()
        cursor = db.conn.cursor()

        s1 = "select * from subject where sid='"+str(sid)+"'"
        print(s1)
        cursor1.execute(s1)
        res1 = cursor1.fetchall()
        for row1 in res1:
            course = row1[4]
            sem = row1[5]

        print(course,"-",str(sem))

        s = "select * from student where course='" + course + "' and semester='" + str(sem) + "' order by rollno"
        print(s)
        cursor.execute(s)
        result = cursor.fetchall()
        i = 4               #row in grid

        font1 = ('Arial', 10, 'bold')
        lb0 = ttk.Label(self,text=' ')
        lb0.config(width=10,font=font1,foreground='brown',background='white')
        lb0.grid(row=3,column=0)
        lb1 = ttk.Label(self,text='Mark')
        lb1.config(width=8,font=font1,foreground='brown',background='white')
        lb1.grid(row=3,column=1,sticky=(W))
        lb2 = ttk.Label(self,text='Rollno')
        lb2.config(width=12,font=font1,foreground='brown',background='white')
        lb2.grid(row=3,column=2,sticky=(W))
        lb3= ttk.Label(self,text='Student Name')
        lb3.config(font=font1,foreground='brown',background='white',width=27)
        lb3.grid(row=3,column=3,sticky=(W))
        lb4= ttk.Label(self,text='Student Mobileno')
        lb4.config(font=font1,foreground='brown',background='white',width=20)
        lb4.grid(row=3,column=4,sticky=(W))
        lb5= ttk.Label(self,text='Parents Mobileno')
        lb5.config(font=font1,foreground='brown',background='white',width=18)
        lb5.grid(row=3,column=5,sticky=(W))
        j=0
        for row in result:
            self.sidlst.append(row[0])
            self.p = IntVar()
            self.c = ttk.Checkbutton(self,text=row[0],variable=self.p)
            self.chkboxlst.append(self.c)
            self.c.grid(row=i,column=1,sticky=(W))
            lstrollno.append(tkinter.Label(self,text=row[1]).grid(row=i,column=2,sticky=(W)))
            lstsname.append(tkinter.Label(self,text=row[2]).grid(row=i,column=3,sticky=(W)))
            lstmobileno.append(tkinter.Label(self,text=row[7]).grid(row=i,column=4,sticky=(W)))
            lstpmobileno.append(tkinter.Label(self,text=row[10]).grid(row=i,column=5,sticky=(W)))
            i = i + 1
            j = j + 1
            self.myvarlst.append(self.p)

        # print(self.sidlst)
        self.btn1 = tkinter.Button(self,text='Mark Attendance',command=self.mark_attendance)
        self.btn1.config(width=20,foreground='brown',background='white')
        self.btn1.grid(row=(i+1),column=3,sticky=(N,E,W))
        self.btn2 = tkinter.Button(self,text='Exit',command=self.close)
        self.btn2.config(width=8, foreground='white', background='red')
        self.btn2.grid(row=(i + 2), column=5, sticky=(E))

    def close(self):
        quit()

    def __init__(self, parent, TEACHERID):
        global dc1
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        self.balloon = Pmw.Balloon(self, xoffset=400, yoffset=-100)
        self.title("View Subjects Window")
        windowWidth = parent.winfo_reqwidth()
        windowHeight = parent.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)
        self.rollno_present = []
        # Gets both half the screen width/height and window width/height
        positionRight = int(parent.winfo_screenwidth() / 2.1 - windowWidth / 2)
        positionDown = int(parent.winfo_screenheight() /4  - windowHeight / 2)
        print(positionRight)
        print(positionDown)
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.geometry("850x420")
        self.lb1 = tkinter.Label(self, text="VIEW SUBJECTS")
        self.lb1.config(foreground='green')
        labelfont = ('Arial', 20, 'bold')
        self.lb1.config(font=labelfont)

        self.lb2 = tkinter.Label(self,text='Select Subject', foreground='brown')
        self.cmb1 = ttk.Combobox(self,state='readonly')
        dc1 = self.getallsubjects(TEACHERID)
        lst = list()
        for k in dc1.keys():
            lst.append(k)
        self.cmb1.config(value=list(lst))

        self.lb3 = tkinter.Label(self, text="Select Date", foreground='brown')
        self.txt3 = DateEntry(self, background='gray', foreground='black', borderwidth=2)
        self.btn_search = Button(self,text='Search',command=self.getstudentdata)
        self.btn_search.config(width=15,foreground='black',background='white')

        self.lb1.grid(row=0, column=1, sticky=(W),columnspan=5)
        self.lb2.grid(row=1,column=0, sticky=(W))
        self.cmb1.grid(row=1,column=1)
        self.lb3.grid(row=1,column=2, sticky=(W))
        self.txt3.grid(row=1,column=3)
        self.btn_search.grid(row=1,column=4)

        self.result = None

