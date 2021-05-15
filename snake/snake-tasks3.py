from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

WIDTH =300
HEIGHT=300
BACKCOLOR = "#003300"
FONTSIZE1 = "Arial 15"
FONTSIZE2 = "Arial 20"


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


root.mainloop()