from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd


class MainMenu:
    def __init__(self):
        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Выход", command=self.onExit)
        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

    def onExit(self):
        root.quit()

class Messager:
    def __init__(self, master, func=None):
        self.text = Text(master, width=250, height=25, bg="white",
            fg ='black', wrap=WORD)
        self.text.place(relx=0.75, rely=0.5)


class Module:
    def __init__(self, master, func=None):
        self.text = Text(master,bg="white",
                         fg='black', wrap=WORD)
        self.button = list()
        self.button.append(Button(root, width=20, height=1, text="Сохранить изменения"))
        self.button.append(Button(root, width=20, height=1, text="Проверить на ошибки"))
        self.button.append(Button(root, width=20, height=1, text="Автоверстка курса"))
        self.button.append(Button(root, width=20, height=1, text="Скачать курс"))
        self.but_place()

    def but_place(self):
        w = 160 / 1920
        x, y, = 0 + w, 1080-200
        for but in self.button:
            but.place(relx=x, y=y)
            x += 0.25
        self.text.place(x=180, y=60, width=1920 - 50, height=1080 - 300)

    def isVisible(self, flag):
        if flag==False:
            for but in self.button:
                but.place_forget()
            self.text.place_forget()
        else:
            self.but_place()


class Helper:
    def __init__(self):
        self.img = Image.open("resource/sber.jpg")
        self.image = ImageTk.PhotoImage(self.img)
        self.label1 = Label(image=self.image)
        self.label2 = Text()
        self.text = Text()
        self.button = Button()
        self.place()
        self.i = 0
        self.add("СберПомощь: Вы бездействуете! Нужна помощь? Пиши мне!")
        self.label1.bind('<Button-1>', self.b1)

    def add(self, s):
        self.label2.insert(1.0, s)
        #self.i = self.i + 1

    def place(self):
        w, h = self.img.size
        self.label1.place(width=w, height=h, x=10, y=100)
        self.label2.place(width=w+30, x=10, y=100+h)
        self.text.place(width=w + 30, height=60, x=10, y=100 + h+130)

    def unplace(self):
        self.label1.place_forget()

    def b1(self, event):
        file = fd.askopenfilename(filetypes=(("IMAGE files", "*.jpg"), ("All files", "*.*")))
        image = Image.open(file)
        w, h = image.size
        self.img = ImageTk.PhotoImage(image)
        self.label1['width'] = w
        self.label1['height'] = h
        self.label1['image'] = self.img
        self.label1.pack(side="bottom", fill="both", expand="yes")

class TopMenu:
    def __init__(self, master, func=None):
        self.button = list()
        self.button.append(Button(master, width=20, height=1, text="Добавить модуль", command=self.addModule))
        self.button.append(Button(master, width=20, height=1, text="Просмотр моих модулей"))
        self.button.append(Button(master, width=20, height=1, text="Отправить на рецензию"))
        self.button.append(Button(master, width=20, height=1, text="Личные сообщения"))
        self.but_place()

    def addModule(self):
        self.module = Module(root)

    def but_place(self):
        w = 200 / 1920
        x, y, = 0 + w, 0
        for but in self.button:
            but.place(relx=x, rely=y)
            x += 0.25

    def isVisible(self, flag):
        if flag == False:
            for but in self.button:
                but.place_forget()
        else:
            self.but_place()

class StateFrame:
    def __init__(self):
        mainmenu = MainMenu()
        self.f_top = Frame()  # root можно не указывать
        self.f_bot = Frame()
        self.f_left = Frame()  # root можно не указывать
        self.f_right = Frame()
        self.f_top.place(relwidth=1, relheight=0.2, relx=0, rely=0)
        self.topmenu = TopMenu(self.f_top)
        self.label1 = Label(width=10, height=1, bg='green', fg='black')
        self.label1.place(relx=0.5, rely=0.5)
        self.label1.bind('<Button-1>', self.b2)
        self.label1['text']='Forget'
        self.messager = Messager(self.f_bot)
        self.label2 = Label(width=10, height=1)
        self.label2.place(relx=0.5, rely=0.6)
        self.label2.bind('<Button-1>', self.b3)
        self.label2['text'] = 'Up'

    def b2(self, event):
        self.topmenu.isVisible(False)

    def b3(self, event):
        self.topmenu.isVisible(True)

    def b1(self, event):
        file = fd.askopenfilename(filetypes=(("IMAGE files", "*.jpg"), ("All files", "*.*")))
        image = Image.open(file)
        #image = image.resize((250, 250),Image.ANTIALIAS)
        w, h = image.size
        self.img = ImageTk.PhotoImage(image)
        self.label1['width'] = w
        self.label1['height'] = h
        self.label1['image'] = self.img
        self.label1.pack(side="bottom", fill="both", expand="yes")


root = Tk()
root.geometry("1920x1080")
root.title("Игра в имитацию. Конструктор курсов")
state_frame = StateFrame()
helper = Helper()
module = Module(root)

root.mainloop()
