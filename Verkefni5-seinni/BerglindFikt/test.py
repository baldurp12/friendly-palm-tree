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
        img.pack()
        ##----text---------
        text = Label(self, text = "Welcome to our educating Quiz for kids!!!")
        text.pack()
        

        text = Label(self, text = "Please choose a category")
        text.pack()
        

        ##-------checkbutton-------

        self.var = IntVar()
        a = Checkbutton(self, text="Animals",
            variable=self.var,
            command=self.animal)
        a.pack()
        

        self.var = IntVar()
        b = Checkbutton(self, text="Human",
            variable=self.var,
            command=self.human)
        b.pack()
        

        self.var = IntVar()
        c = Checkbutton(self, text="Planet",
            variable=self.var,
            command=self.planet)
        c.pack()
       

        self.var = IntVar()
        d = Checkbutton(self, text="Space",
            variable=self.var,
            command=self.space)
        d.pack()
        


        ##-----EnterButton----
        enterButton = Button(self, text = "Make Quiz", command=self.questions)
        enterButton.place(x=50, y=200)

        
        
    def questions(self):
        for i in range(10):
            ##-----question-----
            text = Label(self, text = animal["question" + str(i+1).zfill(2)]).pack()
            
            ##-----EntryWidget----
            global v
            v = StringVar()
            e = Entry(self, textvariable=v)
            e.pack()
           

            v.set("answer")        
            b = Button(self, text="send", width=10, command=self.callback)
            b.pack()
        
        
        
        

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
            

animal= {
    "answer01": "Bamboo",
    "answer02": "False - Captive mice live for up to 2 and a half years while wild mice only live for an average of around 4 months.",
    "answer03": "Arachnophobia",
    "answer04": "The tiger, weighing up to 300 kilograms (660 pounds).",
    "answer05": "True - They often sleep with their mouth open to cool down.",
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

