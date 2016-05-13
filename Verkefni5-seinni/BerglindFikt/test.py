##
##from tkinter import *
##from PIL import Image, ImageTk
##
##class Window(Frame):
##    def __init__(self, master = None):
##        Frame.__init__(self, master)
##        self.master = master
##        self.init_window()
##
##        
##
##        
##    def client_exit(self):
##        exit()
##    def init_window(self):
##        self.master.title("Quiz for kids")
##        
##        self.pack(fill = BOTH, expand=1)
##        
####        quitButton = Button(self, text = "Quit", command = self.client_exit)
####        quitButton.place(x=0, y=0)
##        
##        menu = Menu(self.master)
##        self.master.config(menu=menu)
##        
##   
##    
##        ##-----EntryWidget----
##
##        v = StringVar()
##        e = Entry(self, textvariable=v)
##        e.pack()
##
##        v.set("a default value")
##        s = v.get()
##        
##        b = Button(self, text="get", width=10, command=self.callback)
##        b.pack()
##
##
##
##    def callback():
##        print(e.get())
##
##        
##    def animal(self):
##        print("Þu ert flottur!")
##            
##    def human(self):
##        print("OH BABY!")
##    def planet(self):
##        print("OOOOOJEEEEE!")
##    def space(self):
##        print("BaldurSkvaldurKaldurFlaldur!")
##            
##
##        
##       
##        
##    
##
##root = Tk()
##root.resizable(width=FALSE, height=FALSE)
##root.geometry("500x600")
##app = Window(root)
##root.mainloop()



from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print (e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry













