from menu import *
from tkinter import *


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

def set_status(status_text,color = 'black'):
    canvas.itemconfig(text_id, text=status_text, fill=color)



def pause_toggle():
    global pause
    pause = not pause
    if pause:
        set_status('Пауза')
    else:
        set_status('Вперед',)


def key_handler(event):
    if event.keycode == KEY_UP:
        menu_up()
    if event.keycode == KEY_DOWN:
        menu_down()
    if event.keycode == KEY_ENTER:
        menu_enter()

    if game_over:
        return
    if event.keycode == KEY_PAUSE:
        pause_toggle()

    if pause:
        return
    if event.keycode == KEY_ESC:
        menu_toggle()

    if menu_mode:
        return
    set_status('Вперед!')
    if event.keycode == KEY_PLAYER1:
        canvas.move(player1, SPEED, 0)
    if event.keycode == KEY_PLAYER2:
        canvas.move(player2, SPEED, 0)

    check_finish()

def check_finish():
    global game_over
    coords_player1 = canvas.coords(player1)
    coords_player2 = canvas.coords(player2)
    coords_finish = canvas.coords(finish_id)

    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]

    if x1_right >= x_finish:
        set_status('Победа верхнего игрока', player1_color)
        game_over = True

    if x2_right >= x_finish:
        set_status('Победа нижнего игрока', player2_color)
        game_over = True


player1 = canvas.create_rectangle(x1, y1, x1 + player_size, y1 + player_size, fill=player1_color)
player2 = canvas.create_rectangle(x2, y2, x2 + player_size, y2 + player_size,fill=player2_color)
finish_id = canvas.create_rectangle(x_finish,
                                    0,
                                    x_finish + 10,
                                    game_height,
                                    fill='black')

text_id = canvas.create_text(x1,
                             game_height - 50,
                             anchor=SW,
                             font=('Arial', '25'),
                             text='Вперед!')

canvas.pack()
window.bind('<KeyRelease>', key_handler)
window.mainloop()
