from tkinter import *


def start():

    master = Tk()

    Label(master, text="Run which functions:").grid(row=0, sticky=W)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    Checkbutton(master, text="Duffing", variable=var1).grid(row=1, sticky=W)
    Checkbutton(master, text="Vanderpol", variable=var2).grid(row=2, sticky=W)
    Checkbutton(master, text="Simple Damped", variable=var3).grid(row=3, sticky=W)
    Button(master, text='Start', command=master.destroy).grid(row=4, sticky=W, pady=4)
    

    mainloop()

    duffing=    int(var1.get())
    vanderpol=    int(var2.get())
    simple_damped= int(var3.get())

    return duffing, vanderpol, simple_damped

