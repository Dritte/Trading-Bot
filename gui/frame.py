from tkinter import *

class MyApp:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack
            
            self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
            self.button.pack(side=LEFT)

            self.hi_there = Button(frame, text="Hello", command=self.say_hi)
            self.hi_there.pack(side=RIGHT)

        def say_hi(self):
            print("Hi there")

root = Tk()
myapp = MyApp(root)
root.mainloop()
