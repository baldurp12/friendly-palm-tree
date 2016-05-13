from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
##    def showImg(self):
##        load = Image.open('my_smiley.jpg')
##        render = ImageTk.PhotoImage(load)
##
##        img = Label(self, image = render)
##        img.image = render
##        img.place(x=100, y=100)

        

        
    def client_exit(self):
        exit()
    def init_window(self):
        self.master.title("Quiz for kids")
        
        self.pack(fill = BOTH, expand=1)
        
##        quitButton = Button(self, text = "Quit", command = self.client_exit)
##        quitButton.place(x=0, y=0)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)
        ##-------add image-----------
        load = Image.open('hjalti.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.image = render
        img.place(x=330, y=5)
        ##----text---------
        text = Label(self, text = "Welcome to our educating Quiz for kids!!!")
        text.pack()
        text.place(x=50, y=0)

        text = Label(self, text = "Please choose a category")
        text.pack()
        text.place(x=50, y=30)

        ##-------checkbutton-------

        self.var = IntVar()
        a = Checkbutton(self, text="Animals",
            variable=self.var,
            command=self.animal)
        a.pack()
        a.place(x=50, y=60)

        self.var = IntVar()
        b = Checkbutton(self, text="Human",
            variable=self.var,
            command=self.human)
        b.pack()
        b.place(x=50, y=90)

        self.var = IntVar()
        c = Checkbutton(self, text="Planet",
            variable=self.var,
            command=self.planet)
        c.pack()
        c.place(x=50, y=120)

        self.var = IntVar()
        d = Checkbutton(self, text="Space",
            variable=self.var,
            command=self.space)
        d.pack()
        d.place(x=50, y=150)


        ##-----EnterButton----
        enterButton = Button(self, text = "Make Quiz", command=self.questions)
        enterButton.place(x=50, y=200)

        
        
    def questions(self):
        ##-----question-----
        text = Label(self, text = "Why is the sky blue??????")
        text.pack()
        text.place(x=50, y=230)
        
        ##-----EntryWidget----
        global v
        v = StringVar()
        e = Entry(self, textvariable=v)
        e.pack()
        e.place(x=50, y=260)

        v.set("answer")        
        b = Button(self, text="send", width=10, command=self.callback)
        b.pack()
        b.place(x=50, y=290)
        
        

    def callback(self):
        print (v.get())
        
    def animal(self):
            print("Þu ert flottur!")
            
    def human(self):
            print("OH BABY!")
    def planet(self):
            print("OOOOOJEEEEE!")
    def space(self):
            print("BaldurSkvaldurKaldurFlaldur!")
            

        
       
        
    

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("500x600")
app = Window(root)
root.mainloop()

