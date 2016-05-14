import tkinter

counter = 0
list_test=['a','b','c','d','e','f','g','h','i','j']

window = tkinter.Tk()
window.title("Baldur did it")
window.geometry("300x300")
def callback():
    global counter
    counter += 1
    lbl.configure(text=list_test[counter])







window.wm_iconbitmap('favicon.ico')

lbl = tkinter.Label(window, text='dont like the odds')

ent = tkinter.Entry(window)

btn = tkinter.Button(window, text="Button", command=callback)

lbl.pack()
ent.pack()
btn.pack()
