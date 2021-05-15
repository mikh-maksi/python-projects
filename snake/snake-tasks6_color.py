from tkinter import Tk, Canvas # Подключаем модуль
import random # Модуль генерирования случайных чисел

WIDTH = 300
HEIGHT= 300
BACKCOLOR = "#003300"
FONTSIZE1 = "Arial 15"
FONTSIZE2 = "Arial 20"


def randomcolor():
    r = "%02x"%random.randint(0,255)
    g = "%02x"%random.randint(0,255)
    b = "%02x"%random.randint(0,255)
    res = "#"+str(r)+str(g)+str(b)
    return res
    
def clicked(event):
    print(event.x)
    print(event.y)
    col = randomcolor()

    print(col)
    c.itemconfigure(restart_text,  fill = col)



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
root.mainloop()