from tkinter import *
from PIL import Image, ImageTk
counter = 1
s = ""

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
        
        enterButton.pack()
        enterButton.place(x=50, y=200)

        
        
    def questions(self):
        global text
        global s
        ##-----question-----
        text = Label(self, text = animal["question01"])
        text.place(x=50, y=230)
  
        
        ##-----EntryWidget----
        self.usertext = StringVar()
        self.entr = Entry(self, textvariable=self.usertext)
        self.entr.place(x=50, y=260)
        ##v.set("answer")
        ##s = v.get()
        
        b = Button(self, text="send", width=10, command=self.callback)
        b.place(x=50, y=290)
            


    def callback(self):
        global counter
        ##global s
        counter +=1
        if self.usertext.get() == animal["answer" + str(counter).zfill(2)]:
            print("REETTT SVVAAAAR")
        else:
            print("Rangt svaaaaar :(")
        text.configure(text=animal["question" + str(counter).zfill(2)])

##    def compare_ans(self):
##        print(v.get())
        
    def animal(self):
            print("Þu ert flottur!")
            
    def human(self):
            print("OH BABY!")
    def planet(self):
            print("OOOOOJEEEEE!")
    def space(self):
            print("BaldurSkvaldurKaldurFlaldur!")

animal= {
    "answer01": "Bamboo",
    "answer02": "False",
    "answer03": "Arachnophobia",
    "answer04": "The tiger",
    "answer05": "True",
    "answer06": "Yes",
    "answer07": "Cows",
    "answer08": "True",
    "answer09": "Antarctica",
    "answer10": "True",
    "question01": "What is the closest planet to the Sun?",
    "question02": "What is the name of the 2nd biggest planet in our solar system?",
    "question03": "What is the hottest planet in our solar system?",
    "question04": "What planet is famous for its big red spot on it?",
    "question05": "What planet is famous for the beautiful rings that surround it?",
    "question06": "Can humans breathe normally in space as they can on Earth?",
    "question07": "Is the sun a star or a planet?",
    "question08": "Who was the first person to walk on the moon?",
    "question09": "What planet is known as the red planet?",
    "question10": "What is the name of the force holding us to the Earth?"}

        
       
        
    

root = Tk()
root.resizable(width=FALSE, height=TRUE)
root.geometry("500x600")
app = Window(root)
root.mainloop()

