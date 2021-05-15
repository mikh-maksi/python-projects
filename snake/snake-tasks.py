from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

# Глобальные переменные 
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True

#Создаем блок
# Helper functions
def create_block(): # Функци
    """ Создаем яблочко, которое будет съедено """
    global BLOCK # говорим, чтобы блок глобальный
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE) # Случайная позиция х
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE) # Случайная позиция у
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")
    # Создаем овал


def main():
    """ игровой процесс """
    global IN_GAME # говорим, чтобы блок глобальный
    if IN_GAME: # Переменная-флаг - 
        s.move() # Говорим змейке "Двигайся"
        head_coords = c.coords(s.segments[-1].instance) # Получаем координаты головы
        x1, y1, x2, y2 = head_coords # "Расшиваем координаты головы на переменные"
        # Check for collision with gamefield edges
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT: # Условие, чтобы не выйти за края
            IN_GAME = False
        elif head_coords == c.coords(BLOCK): #Съедаем яблочко
            s.add_segment() # Добавляем сегмент
            c.delete(BLOCK) # Удаляем  яблочко
            create_block() # Создаем новое яблочко
        
        else:  # съедает себя
            for index in range(len(s.segments)-1): # проверяем каждый элементик
                if head_coords == c.coords(s.segments[index].instance): # если голова
                    IN_GAME = False # Изменяем флаг игру
        root.after(100, main) # Делаем паузу
    # если не играем - выводим текст Игра окончена и перезапустить игру
    else:
        set_state(restart_text, 'normal') # Пишем текст "перезапустить игру"
        set_state(game_over_text, 'normal') # Пишем текст "Игра окончена"

#Змейка, цвет
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
        # возможные направления движения
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # Начальное направление движение - выносим в глобальные переменныеы
        self.vector = self.mapping["Down"]

    def move(self):
        # Движение змейки с вектором.
        for index in range(len(self.segments)-1):  # проходимся по каждому сегментику, начиная с 0
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance) # Получаем координаты, смещенные на место следующего
            c.coords(segment, x1, y1, x2, y2) # Размещаем сегмент в точке следующего сегмента

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance) # Получаем координаты
        c.coords(self.segments[-1].instance,  # Рисуем новый сегмент
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
        # Добавляем сегмент к змейке
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        # Изменяем направление у змейки
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def reset_snake(self): # сбрасываем змейку
        for segment in self.segments:
            c.delete(segment.instance)


def set_state(item, state):
    c.itemconfigure(item, state=state)


def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME = True
    c.delete(BLOCK)
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    start_game()


def start_game(): # Функция, которая стартует игру
    global s # Определяем глобальную переменную
    create_block()  # Создаем блоу
    s = create_snake() # создаем змейку
    c.bind("<KeyPress>", s.change_direction) # устанавливаем реакцию на нажатие кнопки.
    main() # Запускаем программу


def create_snake():
    # creating segments and snake
    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
    return Snake(segments)


# Setting up window
root = Tk()
root.title("Way Snake")


c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# catch keypressing
c.focus_set()
game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER!",
                               font='Arial 20', fill='red',
                               state='hidden')
restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                             font='Arial 30',
                             fill='white',
                             text="Click here to restart",
                             state='hidden')
c.tag_bind(restart_text, "<Button-1>", clicked)
start_game()
root.mainloop()
