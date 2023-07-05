from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import Image,ImageTk
import os

def showimage():
	filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("JPG File",".jpg"),("PNG File",".png"),("All file","how are you.txt")))
	img = Image.open(filename)
	img = ImageTk.PhotoImage(img)
	lbl.configure(image=img)
	lbl.image=img

root = Tk()

frame11 = Frame(root)
frame11.pack(side=BOTTOM,padx=15,pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frame11,text="select image",command=showimage)
btn.pack(side=tkinter.LEFT)

btn = Button(frame11,text="capture image",command=lambda:exit())
btn.pack(side=tkinter.LEFT)

root.title("Upload profile photo")
root.geometry("400x400")
root.mainloop()
