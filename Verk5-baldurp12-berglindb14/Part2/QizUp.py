from tkinter import *
from PIL import Image, ImageTk
import json
import os

counter = 0 ##never not use global
corr_answers = 0 ##never not use global

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
   
    def client_exit(self):
        exit()
    def init_window(self):
        self.master.title("Quiz for kids and Hjalti")
        self.picture_folder = os.path.join(os.getcwd(), 'pictures')
        
        self.pack(fill = BOTH, expand=1)

        ##----menu bar----##
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)
        
        ##----add logo----##
        load = Image.open(os.path.join(self.picture_folder,'logo.jpg'))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image = render)
        img.image = render
        img.place(x=330, y=5)
        
        ##----build quiz dictionary----##
        self.quiz_dict = {}
        if os.path.isfile('QandA.json'):
            pass
        else:
            self.quiz_maker_2000()
        with open("QandA.json", 'r', encoding='utf-8') as f:
            self.quiz_dict = json.load(f)
        self.topic_list = sorted(list(self.quiz_dict))

        ##----header----##
        head_text = Label(self, text = "Welcome to our educating Quiz for kids!!!", font=('', 11))
        head_text.place(x=50, y=0)

        self.makeradio()
        
    def questions(self):
        global counter
        counter = 0
        self.current_topic = self.buttonvalue.get()
        
        ##----question text----##
        self.question_text = Label(self, text = self.quiz_dict[self.current_topic]['question01'])
        self.question_text.place(x=50, y=230)
  
        
        ##----entry widget----##
        self.usertext = StringVar()
        self.entr = Entry(self, textvariable=self.usertext)
        self.entr.place(x=50, y=260)

        ##---submit button----##
        self.submit = Button(self, text="Submit answer", width=10, command=self.callback)
        self.submit.place(x=50, y=290)

        ##----hide buttons and 'make quiz'----##
        self.enterButton.place_forget()
        self.R1.place_forget()
        self.R2.place_forget()
        self.R3.place_forget()
        self.R4.place_forget()
        self.text.place_forget()


    def callback(self):
        global counter ##never not use global
        
        ##----check for correct answer----##
        if self.usertext.get().lower() == self.quiz_dict[self.current_topic]["answer" + str(counter + 1).zfill(2)].lower():
            correct_text = Label(self, text = "You are correct, good job!!!")
            correct_text.place(x=50, y=320)
            
            load = Image.open(os.path.join(self.picture_folder,'correct_answer.jpg'))
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.place(x=300, y=300)
            global corr_answers ##never not use global
            corr_answers += 1
            
        else:
            wrong_text = Label(self, text = "Incorrect answer, too bad!!!")
            wrong_text.place(x=50, y=320)
            wrong_text = Label(self, text = 'Correct answer is: \n' + self.quiz_dict[self.current_topic]["answer" + str(counter+1).zfill(2)])
            wrong_text.place(x=50, y=420)
            
            load = Image.open(os.path.join(self.picture_folder,'wrong_answer.jpg'))
            render = ImageTk.PhotoImage(load)
            img = Label(self, image = render)
            img.image = render
            img.place(x=300, y=300)
            
        if (counter+1)*2 >= len(list(self.quiz_dict[self.current_topic].keys())):
            counter = 0

            result_text = Label(self, text = "Quiz finished, you got: " + str(corr_answers) + r'/' +
                               str(len(list(self.quiz_dict[self.current_topic].keys()))//2))
            result_text.place(x=50, y=320)
            self.question_text.place_forget()
            self.entr.place_forget()
            self.submit.place_forget()
            self.makeradio()
        else:
            counter += 1
            self.question_text.configure(text=self.quiz_dict[self.current_topic]["question" + str(counter+1).zfill(2)])  


    def makeradio(self):

        ##----make variable for radibutton selection----##
        self.buttonvalue = StringVar()

        self.text = Label(self, text = "Please choose a category")
        self.text.place(x=50, y=30)

        ##----create the 'make quiz' button----##

        self.enterButton = Button(self, text = "Make Quiz", command = self.questions)
        self.enterButton.place(x=50, y=200)

        ##----radio button soup(our for loop didn't take yes for an answer)----##
        self.R1 = Radiobutton(self, text="Animal", variable=self.buttonvalue, value='animal',
                          command=self.buttonvalue.set(self))
        self.R1.place(x=50, y=60)

        self.R2 = Radiobutton(self, text="Human", variable=self.buttonvalue, value='human',
                          command=self.buttonvalue.set(self))
        self.R2.place(x=50, y=90)

        self.R3 = Radiobutton(self, text="Space", variable=self.buttonvalue, value='space',
                          command=self.buttonvalue.set(self))
        self.R3.place(x=50, y=120)

        self.R4 = Radiobutton(self, text="Planets", variable=self.buttonvalue, value='planet',
                          command=self.buttonvalue.set(self))
        self.R4.place(x=50, y=150)
        self.buttonvalue.set('animal')

    ##---JSON parser----##
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

        with open("QandA.json", "w", encoding='utf-8') as js:
            json.dump(q_a_dict,js, indent=4, sort_keys=True)

root = Tk()
root.resizable(width=FALSE, height=TRUE)
root.geometry("500x600")
root.wm_iconbitmap(os.path.join(os.getcwd(),'pictures', 'turtles.ico'))
app = Window(root)
root.mainloop()
