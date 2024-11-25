import random
import tkinter as tk
from tkinter import messagebox

wind = tk.Tk()
wind.title("Stone Paper Scissors")
wind.geometry("400x300")

rules = tk.Label(wind,
                 text="Rules of the Game:\nYou have to Select between Stone, Paper and Scissors\nStone - Paper: Paper Wins\nPaper - Scissors: Scissors Wins\nStone - Scissors: Stone Wins")
rules.pack(pady=10)

# Initialize computer's choice
listt=['stone', 'paper', 'scissor']
#print(listt)
comp_choice = random.choice(['stone', 'paper', 'scissor'])
#print(comp_choice)

def stone_press():

    if comp_choice == 'scissor':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    else:
        messagebox.showinfo(title="You Lose", message="Please Try Again!!\n Computer Choses {}".format(comp_choice))
        reload()


def paper_press():

    if comp_choice == 'stone':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    else:
        messagebox.showinfo(title="You Lose", message="Please Try Again!!\n Computer Choses {}".format(comp_choice))
        reload()


def scissors_press():

    if comp_choice == 'paper':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    else:
        messagebox.showinfo(title="You Lose", message="Please Try Again!!\n Computer Choses {}".format(comp_choice))
        reload()


def refresh():
    global comp_choice
    comp_choice = random.choice(['stone', 'paper', 'scissor'])
    messagebox.showinfo(message="Game Reset! Try Again.")

def reload():
    global comp_choice
    comp_choice = random.choice(['stone', 'paper', 'scissor'])



button1 = tk.Button(wind, text="Stone", command=stone_press)
button2 = tk.Button(wind, text="Paper", command=paper_press)
button3 = tk.Button(wind, text="Scissors", command=scissors_press)
button4 = tk.Button(wind, text="↻", command=refresh)


button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=20)

wind.mainloop()
