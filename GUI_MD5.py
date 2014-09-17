from tkinter import *
#!/usr/bin/python
'''
Title: Kampen's Method
Author: Adrian Emmanuel M. Antonio
Date: April 22, 2014
Description: Program to translate input word to MD5 hashes
'''
from tkinter import ttk
import hashlib

class MD5(object):
    def __init__(self, master):
        frame = Frame(master, width=130, height=75)
        frame.pack()
        
        self.label = Label(frame, text="Enter String:", font=('Courier', 12))
        self.label.pack()
        self.label.grid(row=1, column = 1,  sticky=W)

        self.input = Entry(frame, width = 50, text="type here")
        self.input.pack()
        self.input.grid(row=2, column=1, sticky=W, pady=5, padx=10)
        self.input.focus_set()
        
        self.button = Button(frame, text="Convert", command = self.convert, font=('Courier', 12))
        self.button.pack()
        self.button.grid(row=2, column = 2,sticky = W)

        self.label2 = Label(frame, text = "Converted MD5 value is:", font=('Courier', 12))
        self.label2.pack()
        self.label2.grid(row=3, column = 1,sticky = W)

        self.md5value = Label(frame, text ="################################", font=('Courier', 12))
        self.md5value.pack()
        self.md5value.grid(row=4, column = 1, sticky=W)
        self.md5value.configure(bg=master.cget('bg'), relief=FLAT)
        self.md5value.configure(state="disabled")
        
    def convert (self, *args):
        if self.input.get() == "":
            print("null")
        else:
            hashing = self.input.get()
            self.md5value["text"] = hashlib.md5(hashing.encode('utf-8')).hexdigest()

class Flashing(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.label = Label(self, text="By: Adrian Emmanuel M. Antonio", 
                              background="black", foreground="white", font=('Courier', 8))
        self.label.pack(side="top", fill="both", expand=True)
        self.flash()

    def flash(self):
        bg = self.label.cget("bg")
        fg = self.label.cget("fg")
        self.label.configure(background=fg, foreground=bg)
        self.after(750, self.flash)
        
if __name__ == '__main__': 
    root = Tk()
    root.title("MD5 CONVERTER")
    md5 = MD5(root)
    root.bind("<Return>",md5.convert)
    Flashing(root).pack(fill="both", expand=True)
    root.resizable(width=FALSE, height=FALSE)
    root.mainloop()