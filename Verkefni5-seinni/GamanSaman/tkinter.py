from tkinter import *
from PIL import Image, ImageTk
import json
import os
from os import path


counter = 0
s = ""
quiz_dict = {}
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        if os.path.isfile('QandA.json'):
            global quiz_dict
            with open("QandA.json", 'r', encoding='utf-8') as f:
                quiz_dict = json.load(f)
        else:
            quiz_maker_2000()
            global quiz_dict
            with open("QandA.json", 'r', encoding='utf-8') as f:
                quiz_dict = json.load(f)


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
        counter += 1
        if self.usertext.get() == animal["answer" + str(counter).zfill(2)]:
            correct_text = Label(self, text = "You are corrent!, good job!")
            correct_text.place(x=50, y=320)
            
            load = Image.open('rettsvar.jpg')
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.place(x=300, y=350)
        else:
            wrong_text = Label(self, text = "You are incorrent, sorry")
            wrong_text.place(x=50, y=320)
            
            load = Image.open('rangtsvar.jpg')
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.place(x=300, y=350)
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
root.wm_iconbitmap('turtles.ico')
app = Window(root)
root.mainloop()

def quiz_maker_2000():
    question_path = os.path.join(os.getcwd(), 'questions')
    answers_path = os.path.join(os.getcwd(), 'answers')
    
    q_files = sorted(os.listdir(question_path))
    a_files = sorted(os.listdir(answers_path))

    topics = []
   
    for i in q_files:
        topics.append(i.split(sep='-')[0])

    q_a_dict = {}
    
    for index, top in enumerate(topics):
        a = open(os.path.join(question_path, q_files[index]), 'r', encoding='utf-8')
        b = open(os.path.join(answers_path, a_files[index]), 'r', encoding='utf-8')
        x = a.read().splitlines()
        y = b.read().splitlines()

        a.close()
        b.close()
        
        temp_dict = {}

        for i in range( len(x) ): ## len(x) ætti að vera == len(y)
            
            temp_dict[str('question' + str(i+1).zfill(2))] = str(x[i])
            temp_dict[str('answer' + str(i+1).zfill(2))] = str(y[i])

        q_a_dict[top] = temp_dict

    with open("QandA.json", "w", encoding='utf_8') as js:
        json.dump(q_a_dict,js, indent=4, sort_keys=True)

