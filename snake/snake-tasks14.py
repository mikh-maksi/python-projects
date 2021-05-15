from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

WIDTH = 300
HEIGHT= 300
SEG_SIZE = 10
BACKCOLOR = "#003300"
FONTSIZE1 = "Arial 15"
FONTSIZE2 = "Arial 20"
IN_GAME = True


def clicked(event):
    print(event.x)
    print(event.y)
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    create_block()

def set_state(item, state):
    c.itemconfigure(item, state=state)

def create_block(): # Функци
    global BLOCK
    nw = (WIDTH-SEG_SIZE) / SEG_SIZE
    nh = (HEIGHT-SEG_SIZE) / SEG_SIZE

    posx = SEG_SIZE * random.randint(1,nw)
    posy = SEG_SIZE * random.randint(1,nh)

    BLOCK = c.create_oval(posx, posy,
                            posx+SEG_SIZE, posy+SEG_SIZE,
                            fill="red")

def main():
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance) # Получаем координаты головы
        x1, y1, x2, y2 = head_coords # "Расшиваем координаты головы на переменные"
        if head_coords == c.coords(BLOCK): #Съедаем яблочко
            s.add_segment() # Добавляем сегмент
            c.delete(BLOCK) # Удаляем  яблочко
            create_block() # Создаем новое яблочко
        root.after(100, main)
    else:
        set_state(restart_text, 'normal') # Пишем текст "перезапустить игру"
        set_state(game_over_text, 'normal') # Пишем текст "Игра окончена"

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

        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # Начальное направление движение - выносим в глобальные переменныеы
        self.vector = self.mapping["Down"]


    def move(self):
        for index in range(len(self.segments)-1):  # проходимся по каждому сегментику, начиная с 0
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance) # Получаем координаты, смещенные на место следующего
            c.coords(segment, x1, y1, x2, y2) # Размещаем сегмент в точке следующего сегмента
       
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance) # Получаем координаты
        c.coords(self.segments[-1].instance,  # Рисуем новый сегмент
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)   



    def change_direction(self, event):
        # Изменяем направление у змейки
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
            print(event.keysym)

def create_snake():
    # creating segments and snake
    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
    return Snake(segments)

def start_game(): # Функция, которая стартует игру
    global s # Определяем глобальную переменную
    create_block()  # Создаем блоу
    s = create_snake() # создаем змейку
    c.bind("<KeyPress>", s.change_direction) # устанавливаем реакцию на нажатие кнопки.
    main() # Запускаем программу



root = Tk()
root.title("My Game")



c = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKCOLOR)
c.grid()

c.focus_set()


game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!",
                               font=FONTSIZE1, fill='red',
                               state='hidden')
restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                             font=FONTSIZE2,
                             fill='white',
                             text="Click here to restart",
                             state='hidden')

c.tag_bind(restart_text, "<Button-1>", clicked)




start_game()
root.mainloop()