from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

WIDTH =300
HEIGHT=300
BACKCOLOR = "#003300"

root = Tk()
root.title("My Game")



c = Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKCOLOR)
c.grid()


root.mainloop()