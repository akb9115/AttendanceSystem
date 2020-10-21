from tkinter import *
from PIL import ImageTk,Image

root=Tk()
screen_height = root.winfo_screenheight()
screen_width=root.winfo_screenwidth()
root.geometry("355x355")

path="4.jpg"
img = ImageTk.PhotoImage(Image.open(path))
lb=Label(root,image=img,height=355,width=355)

path="3.jpg"
img2 = ImageTk.PhotoImage(Image.open(path))
lb2=Label(root,image=img2,height=80,width=355)
lb3=Label(root,text="Email",compound=CENTER)
lb4=Label(root,text="Password",compound=CENTER)

tf1=Entry(root,width=40)
tf2=Entry(root,width=40)

lb.place(x=0,y=0)
lb.grid(row=1,column=0,columnspan=2,rowspan=5)
lb2.grid(row=1,column=0,columnspan=2,sticky=(N))
tf1.grid(row=2,column=1,sticky=(W,N))
tf2.grid(row=3,column=1,sticky=(W,N))

lb3.grid(row=2,column=0,sticky=(W,N,E))
lb4.grid(row=3,column=0,sticky=(W,N,E))
root.mainloop()