import tkinter
from tkinter import *
from tkinter import ttk

class progress:

    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 100
        self.progress["maximum"] = 100
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 1
        abc = "Loading.... (" + str(self.bytes // 1) + "%)"
        self.lb_blank.config(text=abc)
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.lgfrm.after(100, self.read_bytes)
        else:
            print("Loop Completed")


    def __init__(self):
        self.lgfrm = Tk()
        self.lgfrm.title("Admin Login Form")
        self.lb_head = tkinter.Label(self.lgfrm, text="ADMIN LOGIN FORM")
        self.lb_head.config(foreground='green')
        labelfont = ('Arial', 20, 'bold')
        self.lb_head.config(font=labelfont)

        self.lgfrm.geometry("400x220")  # window size
        self.lb1 = tkinter.Label(self.lgfrm, text="Enter Username", foreground='green')
        self.txtusername = tkinter.Entry(self.lgfrm)
        self.lb2 = tkinter.Label(self.lgfrm, text="Enter Password", foreground='green')
        self.txtpassword = tkinter.Entry(self.lgfrm, show='*')
        self.btn_login = tkinter.Button(self.lgfrm, text="LOGIN", command=self.start)
        self.btn_exit = tkinter.Button(self.lgfrm, text="Exit", command=quit)
        # self.lblerror = tkinter.Label(self.lgfrm, text="", foreground='red')
        self.lb_head.grid(row=0, column=0, columnspan=3)

        self.lb1.grid(row=1, column=0, sticky=(E))
        self.txtusername.grid(row=1, column=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.lb2.grid(row=2, column=0, sticky=(E))
        self.txtpassword.grid(row=2, column=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

        self.btn_login.config(bg='white', fg='#333', width='20')
        self.btn_exit.config(bg='red', fg='white', width='10')

        self.btn_login.grid(row=3, column=1, sticky=(N, E, W), pady=5, padx=5)
        self.btn_exit.grid(row=6, column=2, sticky=(E), pady=5, padx=5)

        # self.btn_login.grid(row=2, column=1, sticky=(W))
        self.lb_blank = tkinter.Label(self.lgfrm, text="")
        self.progress = tkinter.ttk.Progressbar(self.lgfrm, orient="horizontal", length=400, mode="determinate")
        self.lb_blank.grid(row=4, column=0)
        self.progress.grid(row=5, column=0, columnspan=3)
        self.bytes = 0
        self.maxbytes = 0
        self.txtusername.focus()
        self.txtusername.insert(0, 'Monika')
        self.txtpassword.insert(0, '12345')
        self.lgfrm.resizable(0, 0)
        self.lgfrm.mainloop()


progress()