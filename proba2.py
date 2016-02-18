from tkinter import *

class MyDialog:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Value").pack()

        self.e = Entry(top)
        Text(top,width=40,height=15,font="12").pack()
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print ("value is", self.e.get())

        self.top.destroy()
root = Tk()
Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)
root.mainloop()
