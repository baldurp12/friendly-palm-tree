import tkinter
import string
import json



counter = -1
list_test=[x for x in (string.ascii_letters + string.digits) ]

window = tkinter.Tk()
window.title("Baldur did it")
window.geometry("300x300")
def callback():
    global counter
    counter += 1
    if counter >= len(list_test):
        counter = 0
    lbl.configure(text=list_test[counter])

##for i in range(10):
##    lbl = tkinter.Label(window, text=i)
##    btn = tkinter.Button(window, text= 'shiiii')
##    lbl.pack(side=tkinter.TOP)
##    btn.pack(side=tkinter.TOP)

##
##def newwind():
##    popwindow = tkinter.Tk()
##    popwindow.title("shit")
##    popwindow.geometry('100x100')
##    butt = tkinter.Button(popwindow, text=quit, command=quit())
##    butt.pack()
##    window.mainloop()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(window, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(window, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(window, text="female", variable=var2).grid(row=2, sticky=W)
Button(window, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(window, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

window.wm_iconbitmap('favicon.ico')

lbl = tkinter.Label(window, text='dont like the odds')

ent = tkinter.Entry(window)

btn = tkinter.Button(window, text="Button", command=callback)

lbl.pack()
ent.pack()
btn.pack()


window.mainloop()


