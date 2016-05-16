from tkinter import *
from PIL import Image, ImageTk
import json
import os
from os import path


counter = 0
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
        self.master.title("Quiz for kids and Hjalti")
        self.picture_folder = os.path.join(os.getcwd(), 'pictures')
        
        self.pack(fill = BOTH, expand=1)
        
##        quitButton = Button(self, text = "Quit", command = self.client_exit)
##        quitButton.place(x=0, y=0)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)
        ##-------add image-----------
        load = Image.open(os.path.join(self.picture_folder,'logo.png'))
        render = ImageTk.PhotoImage(load)
        
        img = Label(self, image = render)
        img.image = render
        img.grid(row=1, column=3)
        ##------build quiz dictionary
        self.quiz_dict = {}
        if os.path.isfile('QandA.json'):
            pass
        else:
            self.quiz_maker_2000()
        with open("QandA.json", 'r', encoding='utf-8') as f:
            self.quiz_dict = json.load(f)
        self.topic_list = sorted(list(self.quiz_dict))        
        ##----text---------
        text = Label(self, text = "Welcome to our educating Quiz for kids!!!")

        text.grid(row=1, column=1)

        text = Label(self, text = "Please choose a category")
        text.grid(row=2, column=1)

        ##-------checkbutton-------
        self.buttonvalue = StringVar()

##        for i in range(len(self.topic_list)):
##            R = Radiobutton(self, text=self.topic_list[i].title(), variable=self.buttonvalue,
##                            command=self.buttonvalue.set(self),
##                            value=self.topic_list[i])
##            R.pack()
##            R.place(x=50, y = 60 + i*35)
##            
##
##

        R1 = Radiobutton(self, text="Animal", variable=self.buttonvalue, value='animal',
                          command=self.buttonvalue.set(self))
        R1.grid(row=3, column=1)

        R2 = Radiobutton(self, text="Human", variable=self.buttonvalue, value='human',
                          command=self.buttonvalue.set(self))
        R2.grid(row=3, column=2)

        R3 = Radiobutton(self, text="Space", variable=self.buttonvalue, value='space',
                          command=self.buttonvalue.set(self))
        R3.grid(row=4, column=1)

        R4 = Radiobutton(self, text="Planets", variable=self.buttonvalue, value='planet',
                          command=self.buttonvalue.set(self)) ### SHIT FUCK
        R4.grid(row=4, column=2)


##
##
##
##        self.var = IntVar()
##        a = Checkbutton(self, text="Animals",
##            variable=self.var,
##            command=self.animal)
##        a.pack()
##        a.place(x=50, y=60)
##
##        self.var = IntVar()
##        b = Checkbutton(self, text="Human",
##            variable=self.var,
##            command=self.human)
##        b.pack()
##        b.place(x=50, y=90)
##
##        self.var = IntVar()
##        c = Checkbutton(self, text="Planet",
##            variable=self.var,
##            command=self.planet)
##        c.pack()
##        c.place(x=50, y=120)
##
##        self.var = IntVar()
##        d = Checkbutton(self, text="Space",
##            variable=self.var,
##            command=self.space)
##        d.pack()
##        d.place(x=50, y=150)


        ##-----MakeQuizButton----

        makeQuizButton = Button(self, text = "Make Quiz", command = self.questions)
        
        makeQuizButton.grid(row=5, column=1)
        
##        enterButton = Button(self, text = "Make Quiz", command = self.questions)
##        
##        enterButton.pack()
##        enterButton.place(x=50, y=200)

        
        
    def questions(self):
        global text
        global s
        global counter
        counter = 0
        self.current_topic = self.buttonvalue.get()
        
        ##-----question-----
        try:
            text = Label(self, text = self.quiz_dict[self.current_topic]['question01'])
        except:
            text = Label(self, text = "No topic selected")
        text.grid(row=6, column=1)
  
        
        ##-----EntryWidget----
        self.usertext = StringVar()
        self.entr = Entry(self, textvariable=self.usertext)
        self.entr.grid(row=7, column=1)
        ##v.set("answer")
        ##s = v.get()
        
        b = Button(self, text="send", width=10, command=self.callback)
        b.grid(row=8, column=1)
            


    def callback(self):
        global counter
        ##global s
  
        if self.usertext.get() == self.quiz_dict[self.current_topic]["answer" + str(counter + 1).zfill(2)]:
            correct_text = Label(self, text = "You are corrent!, good job!")
            correct_text.grid(row=9, column=1)
            
            load = Image.open(os.path.join(self.picture_folder,'correct_answer.jpg'))
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.grid(row=9, column=3)
        else:
            wrong_text = Label(self, text = "You are an idiot, not sorry")
            wrong_text.grid(row=9, column=1)
            wrong_text = Label(self, text = 'Correct answer is: \n' + self.quiz_dict[self.current_topic]["answer" + str(counter+1).zfill(2)])
            wrong_text.grid(row=10, column=1)
            
            load = Image.open(os.path.join(self.picture_folder,'wrong_answer.jpg'))
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.grid(row=9, column=3)
        counter += 1
        text.configure(text=self.quiz_dict[self.current_topic]["question" + str(counter+1).zfill(2)])  


        


##    def compare_ans(self):
##        print(v.get())

##    def radio_update():
##        pass
##        
##    def animal(self):
##            print("Þu ert flottur!")
##    def human(self):
##            print("OH BABY!")
##    def planet(self):
##            print("OOOOOJEEEEE!")
##    def space(self):
##            print("BaldurSkvaldurKaldurFlaldur!")




    def quiz_maker_2000(self):
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
##
##animal= {
##    "answer01": "Bamboo",
##    "answer02": "False",
##    "answer03": "Arachnophobia",
##    "answer04": "The tiger",
##    "answer05": "True",
##    "answer06": "Yes",
##    "answer07": "Cows",
##    "answer08": "True",
##    "answer09": "Antarctica",
##    "answer10": "True",
##    "question01": "What is the closest planet to the Sun?",
##    "question02": "What is the name of the 2nd biggest planet in our solar system?",
##    "question03": "What is the hottest planet in our solar system?",
##    "question04": "What planet is famous for its big red spot on it?",
##    "question05": "What planet is famous for the beautiful rings that surround it?",
##    "question06": "Can humans breathe normally in space as they can on Earth?",
##    "question07": "Is the sun a star or a planet?",
##    "question08": "Who was the first person to walk on the moon?",
##    "question09": "What planet is known as the red planet?",
##    "question10": "What is the name of the force holding us to the Earth?"}

root = Tk()
root.resizable(width=FALSE, height=TRUE)
root.geometry("500x600")
root.wm_iconbitmap(os.path.join(os.getcwd(),'pictures', 'turtles.ico'))
app = Window(root)
root.mainloop()

