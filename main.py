from tkinter import *
from pickle import load, dump

def set_status():
    pass

def pause_toggle():
    pass

def menu_toggle():
    pass

def key_handler():
    pass


def check_finish():
    pass


game_width = 800
game_height = 800

KEY_UP = 87
KEY_DOWN = 83
KEY_ESC = 27
KEY_ENTER = 13

player_size = 100
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'

x_finish = game_width - 50

KEY_PLAYER1 = 39
KEY_PLAYER2 = 68
KEY_PAUSE = 19

SPEED = 12

game_over = False
pause = False

window = Tk()
window.title('Меню игры')

canvas = Canvas(window, width=game_width, height=game_height, bg='white')
canvas.pack()

player1 = canvas.create_rectangle(x1,
                                  y1,
                                  x1 + player_size,
                                  y1 + player_size,
                                  fill=player1_color)
player2 = canvas.create_rectangle(x2,
                                  y2,
                                  x2 + player_size,
                                  y2 + player_size,
                                  fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')


window.bind('<KeyRelease>', key_handler)
window.mainloop()
