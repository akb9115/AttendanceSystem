from tkinter import *
from PIL import ImageTk,Image
root=Tk()
screen_height = root.winfo_screenheight()
screen_width=root.winfo_screenwidth()


path="3.jpg"
img = ImageTk.PhotoImage(Image.open(path))

lb=Label(root,image=img,height=80,width=355)

lb2=Label(root,text="Email")
tf1=Entry(root,width=40)
lb.place(x=0,y=0)

lb.grid(row=0,column=0,columnspan=2)
lb2.grid(row=1,column=0,sticky=(W))
tf1.grid(row=1,column=0,sticky=(E))

root.mainloop()