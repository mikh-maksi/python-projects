from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

WIDTH = 300
HEIGHT= 300
SEG_SIZE = 10
BACKCOLOR = "#003300"
FONTSIZE1 = "Arial 15"
FONTSIZE2 = "Arial 20"


def clicked(event):
    print(event.x)
    print(event.y)
    # c.itemconfigure(restart_text, state='hidden')
    # c.itemconfigure(game_over_text, state='hidden')
    create_block()

def create_block(): # Функци
    global BLOCK
    nw = (WIDTH-SEG_SIZE) / SEG_SIZE
    nh = (HEIGHT-SEG_SIZE) / SEG_SIZE

    posx = SEG_SIZE * random.randint(1,nw)
    posy = SEG_SIZE * random.randint(1,nh)

    BLOCK = c.create_oval(posx, posy,
                            posx+SEG_SIZE, posy+SEG_SIZE,
                            fill="red")


class Segment(object):     # Класс, описывающий один квадратик змейки
    def __init__(self, x, y):  # Магический метод, которы создает новый сегмент при инициации.
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="#F0F8FF")
                # Создаем сегмент в виде квадрата

class Snake(object):   # Создаем змею
    """ Simple Snake class """
    def __init__(self, segments):  # Магический класс, который получает сегмент
        self.segments = segments #Поле, которое получает сегменты.


def create_snake():
    # creating segments and snake
    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
    return Snake(segments)



root = Tk()
root.title("My Game")



c = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKCOLOR)
c.grid()

c.focus_set()


game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!",
                               font=FONTSIZE1, fill='red',
                               state='normal')
restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                             font=FONTSIZE2,
                             fill='white',
                             text="Click here to restart",
                             state='normal')

c.tag_bind(restart_text, "<Button-1>", clicked)


s = create_snake()


root.mainloop()