from tkinter import *

def sel():
   selection = "You selected the option " + var.get()
   label.config(text = selection)

root = Tk()
root.resizable(width=FALSE, height=TRUE)
root.geometry("500x600")


var = StringVar()

R1 = Radiobutton(root, text="Animal", variable=var, value='Animal',
                  command=sel)
R1.grid(row=0, sticky=W)

R2 = Radiobutton(root, text="Human", variable=var, value='Human',
                  command=sel)
R2.grid(row=1, sticky=W)

R3 = Radiobutton(root, text="Space", variable=var, value='Space',
                  command=sel)
R3.grid(row=2, sticky=W)

R4 = Radiobutton(root, text="Planets", variable=var, value='Planets',
                  command=sel)
R4.grid(row=3, sticky=W)



label = Label(root, text='Select an option')

label.grid(sticky=W)



root.mainloop()
