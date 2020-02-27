import tkinter
from tkinter import ttk
import random

window = tkinter.Tk()
window.title("treasure hunt")
window.geometry("500x500+200+200")



plansza = [["☐" for x in range(10)]for y in range(10)]
def print_board():
    board = ""
    for x in plansza:
        for y in x:
            board += y + " "
        board += "\n"

    return board

treasure_a = random.randint(0, 9)
treasure_b = random.randint(0, 9)
plansza[treasure_a][treasure_b] = "$"

player_a = random.randint(0, 9)
player_b = random.randint(0, 9)
plansza[player_a][player_b] = ""
win = False

def print_hint():
    global treasure_a, treasure_b, player_a, player_b, win
    hint_text = ""
    if treasure_a < player_a:
        hint_text += "go up "
    if treasure_a > player_a:
        hint_text += "go down "
    if treasure_b < player_b:
        hint_text += "go left"
    if treasure_b > player_b:
        hint_text += "go right"
    if treasure_b == player_b and treasure_a == player_a:
        hint_text = "YOU WIN"
        win = True
    return hint_text

counters = 21

def counter():
    global counters
    counters -= 1
    return str(counters)

def move_up():
    global player_a, player_b, counters, win
    if counters > 0 and not win:
        plansza[player_a][player_b] = "☐"
        if player_a - 1 >= 0:
            player_a -= 1
        plansza[player_a][player_b] = ""
        labelka["text"] = print_board()
        hint["text"] = print_hint()
        move_counter["text"] = "moves: " + counter()
    else:
        hint["text"] = "Game over"

def move_down():
    global player_a, player_b, counters, win
    if counters > 0 and not win:
        plansza[player_a][player_b] = "☐"
        if player_a + 1 <= 9:
            player_a += 1
        plansza[player_a][player_b] = ""
        labelka["text"] = print_board()
        hint["text"] = print_hint()
        move_counter["text"] = "moves: " + counter()
    else:
        hint["text"] = "Game over"

def move_left():
    global player_a, player_b, counters, win
    if counters > 0 and not win:
        plansza[player_a][player_b] = "☐"
        if player_b - 1 >= 0:
            player_b -= 1
        plansza[player_a][player_b] = ""
        labelka["text"] = print_board()
        hint["text"] = print_hint()
        move_counter["text"] = "moves: " + counter()
    else:
        hint["text"] = "Game over"

def move_right():
    global player_a, player_b, counters, win
    if counters > 0 and not win:
        plansza[player_a][player_b] = "☐"
        if player_b + 1 <= 9:
            player_b += 1
        plansza[player_a][player_b] = ""
        labelka["text"] = print_board()
        hint["text"] = print_hint()
        move_counter["text"] = "moves: " + counter()
    else:
        hint["text"] = "Game over"

labelka = tkinter.Label(window, font=("Arial", 20), text=print_board())
labelka.pack(side=tkinter.TOP)

hint = tkinter.Label(window, text=print_hint(), width=50, fg="red", bg="pink")
hint.pack(side=tkinter.TOP)

move_counter = tkinter.Label(window, text=counter(), width=50, fg="red", bg="pink")
move_counter.pack(side=tkinter.TOP)

frame = tkinter.Frame(window)
frame.pack(side=tkinter.BOTTOM)

up = ttk.Button(frame, text="↑", command=move_up)
up.pack(side=tkinter.TOP)
down = ttk.Button(frame, text="↓", command=move_down)
down.pack(side=tkinter.BOTTOM)
left = ttk.Button(frame, text="←", command=move_left)
left.pack(side=tkinter.LEFT)
right = ttk.Button(frame, text="→", command=move_right)
right.pack(side=tkinter.RIGHT)



window.mainloop()