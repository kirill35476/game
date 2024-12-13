from tkinter import *
from pickle import dump, load

window = Tk()
w = 800
h = 500
window.title('Догони меня если сможешь')
canvas = Canvas(window, width=w, height=h, bg='white')
player_size = 100
x1, y1 = 50, 50
x2, y2 = x1, y1 + player_size + 100
player1_color = 'red'
player2_color = 'blue'
x_finish = w - 50
game_over = False
pause = False

KEY_PLAYER1 = 39
KEY_PLAYER2 = 68
SPEED = 12
KEY_PAUSE = 19
images = []
x0 = 10
offset = 100

def set_status(status_text,color = 'black',):
    canvas.itemconfig(text_status_id, text=status_text, fill=color)

def save_game(event):
    x1 = canvas.coords(player1_id)[0]
    x2 = canvas.coords(player2_id)[0]
    data = [x1, x2]
    print(data)
    with open('save.dat', 'wb') as f:
        dump(data, f)
        set_status('Сохранено')


def load_game(event):
    global x1, x2
    with open('save.dat', 'rb') as f:
        data = load(f)
        x1, x2 = data
        canvas.coords(player1_id, x1, y1, x1 + player_size, y1 + player_size)
        canvas.coords(player2_id, x2, y2, x2 + player_size, y2 + player_size)
        set_status('Загружено')


def pause_toggle():
    global pause
    pause = not pause
    if pause:
        set_status('Пауза')
    else:
        set_status('Вперед',)


def key_handler(event):
    if game_over:
        return
    if event.keycode == KEY_PAUSE:
        pause_toggle()

    if pause:
        return
    if event.keycode == KEY_PLAYER1:
        canvas.move(player1_id, SPEED, 0)
    elif event.keycode == KEY_PLAYER2:
        canvas.move(player2_id, SPEED, 0)

    check_finish()


def check_finish():
    global game_over
    coords_player1 = canvas.coords(player1_id)
    coords_player2 = canvas.coords(player2_id)
    coords_finish = canvas.coords(finish_id)
    x1_right = coords_player1[2]
    x2_right = coords_player2[2]
    x_finish = coords_finish[0]
    if x1_right >= x_finish:
        global status_text
        canvas.itemconfig(text_status_id, text='Победа верхнего игрока', fill='red')
        game_over = True
    if x2_right >= x_finish:
        canvas.itemconfig(text_status_id, text='Победа нижнего игрока', fill='blue')
        game_over = True


player1_id = canvas.create_rectangle(x1, y1, x1 + player_size, y1 + player_size, fill=player1_color)
player2_id = canvas.create_rectangle(x2, y2, x2 + player_size, y2 + player_size, fill=player2_color)
finish_id = canvas.create_rectangle(x_finish, 0, x_finish + 10, h, fill='black')
text_status_id = canvas.create_text(x1,h-50, anchor=SW, font=('Arial', '25'), text='Вперед!')
canvas.pack()
window.bind('<KeyRelease>', key_handler)
window.bind('<Control-Key-s>', save_game)
window.bind('<Control-Key-o>', load_game)
window.mainloop()
