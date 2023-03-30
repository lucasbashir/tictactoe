from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Tac Toe")

clicked = True
count = 0

buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text="", font=("Helvetica", 20), height=3, width=6, command=lambda row=i, col=j: click(row, col))
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)

def click(row, col):
    global clicked, count

    if buttons[row][col]["text"] == "" and clicked == True:
        buttons[row][col]["text"] = "X"
        computer_move()
        count += 1

        #check for win

        if check_win("X"):
            messagebox.showinfo("Tic Tac Toe", "You won!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()

        elif check_win("O"):
            messagebox.showinfo("Tic Tac Toe", "You Lost!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "Tie")
            disable_all_buttons()


def check_win(player):
    #check for rows

    for i in range(3):
        if buttons[i][0]["text"] == player and buttons[i][1]["text"] == player and buttons[i][2]["text"] == player:
            buttons[i][0].config(bg="red")
            buttons[i][1].config(bg="red")
            buttons[i][2].config(bg="red")
            return True
        # Check columns for win
        if buttons[0][i]['text'] == player and buttons[1][i]['text'] == player and buttons[2][i]['text'] == player:
            buttons[0][i].config(bg="red")
            buttons[1][i].config(bg="red")
            buttons[2][i].config(bg="red")
            return True
    # Check diagonals for win
    if buttons[0][0]['text'] == player and buttons[1][1]['text'] == player and buttons[2][2]['text'] == player:
        buttons[0][0].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][2].config(bg="red")
        return True
    if buttons[0][2]['text'] == player and buttons[1][1]['text'] == player and buttons[2][0]['text'] == player:
        buttons[0][2].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][0].config(bg="red")
        return True
    return False


def computer_move():
    global count
    empty_cells = []

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                empty_cells.append((i, j))
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]["text"] = "O"
        count += 1
        if check_win("O"):
            disable_all_buttons()

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def reset():
    global clicked, count
    clicked = True
    count = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=NORMAL, bg="SystemButtonFace")
my_menu = Menu(root)
root.config(menu=my_menu)
#create menu options

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()