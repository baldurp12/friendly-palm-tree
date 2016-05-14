import tkinter

counter = 0
list_test=['a','b','c','d','e','f','g','h','i','j']

window = tkinter.Tk()
window.title("Baldur did it")
window.geometry("300x300")
def callback():
    global counter
    counter += 1
    if counter >= 10:
        newwind()
    lbl.configure(text=list_test[counter])

##for i in range(10):
##    lbl = tkinter.Label(window, text=i)
##    btn = tkinter.Button(window, text= 'shiiii')
##    lbl.pack(side=tkinter.TOP)
##    btn.pack(side=tkinter.TOP)


def newwind():
    popwindow = tkinter.Tk()
    popwindow.title("shit")
    popwindow.geometry('100x100')
    butt = tkinter.Button(popwindow, text=quit, command=quit())
    butt.pack()
    window.mainloop()


window.wm_iconbitmap('favicon.ico')

lbl = tkinter.Label(window, text='dont like the odds')

ent = tkinter.Entry(window)

btn = tkinter.Button(window, text="Button", command=callback)

lbl.pack()
ent.pack()
btn.pack()





window.mainloop()


