from tkinter import *
from PIL import ImageTk, Image

class Messager:
    def __init__(self, master, func=None):
        self.text = Text(master, width=25, height=5, bg="white",
            fg='white', wrap=WORD)
        self.text.pack(side=RIGHT)

class StateFrame:
    def __init__(self):
        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Выход")

        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

        self.f_top = Frame()  # root можно не указывать
        self.f_bot = Frame()
        self.f_left = Frame()  # root можно не указывать
        self.f_right = Frame()
        self.f_top.pack(side=TOP)
        self.f_bot.pack(side=BOTTOM)
        self.f_left.pack(side=LEFT)
        self.f_right.pack(side=RIGHT)
        self.label1 = Label(self.f_top, width=20, height=20)
        self.label2 = Label(self.f_left, width=20, height=20)
        self.label3 = Label(self.f_right, width=20, height=20)
        self.label4 = Label(self.f_bot, width=20, height=20)
        self.label1.bind('<Button-1>',self.b1)
        self.label1['text']='Нажмите чтобы вставить фото'
        self.label2['text'] = 'f_left'
        self.label3['text'] = 'f_right'
        self.label4['text'] = 'f_bot'
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.messager = Messager(self.f_bot)

    def b1(self,event):
        image = Image.open(r"C:\Users\ArtificialGod\PycharmProjects\tsifrovoy\venv\resource\oTX49n5Szsc.jpg")
        image = image.resize((250, 250),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image)
        self.label1['width']=250
        self.label1['heigh']=250
        self.label1['image']=self.img
        self.label1.pack(side="bottom", fill="both", expand="yes")

root = Tk()
state_frame = StateFrame()


root.mainloop()