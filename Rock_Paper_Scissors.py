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
listt=['Stone', 'Paper', 'Scissor']
#print(listt)
comp_choice = random.choice(['Stone', 'Paper', 'Scissor'])
#print(comp_choice)

def stone_press():

    if comp_choice == 'Scissor':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    elif comp_choice == 'Stone':
        messagebox.showinfo(message="Match has been Draw !! Computer also Chooses Stone.")
        reload()
    else:
        messagebox.showerror(title="You Lose", message="You Loose !!\n Computer Chooses {}".format(comp_choice))
        reload()


def paper_press():

    if comp_choice == 'Stone':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    elif comp_choice == 'Paper':
        messagebox.showinfo(message="Match has been Draw !! Computer also Chooses Paper.")
        reload()

    else:
        messagebox.showerror(title="You Lose", message="You Loose !!\n Computer Chooses {}".format(comp_choice))
        reload()


def scissors_press():

    if comp_choice == 'Paper':
        messagebox.showinfo(message="CONGRATULATIONS!!\n You Win the Game. :)")
        reload()
    elif comp_choice == 'Scissor':
        messagebox.showinfo(message="Match has been Draw !! Computer also Chooses Scissor.")
        reload()
    else:
        messagebox.showerror(title="You Lose", message="You Loose !!\n Computer Chooses {}".format(comp_choice))
        reload()


def refresh():
    global comp_choice
    comp_choice = random.choice(['Stone', 'Paper', 'Scissor'])
    messagebox.showinfo(message="Game Reset! Try Again.")

def reload():
    global comp_choice
    comp_choice = random.choice(['Stone', 'Paper', 'Scissor'])



button1 = tk.Button(wind, text="Stone", command=stone_press)
button2 = tk.Button(wind, text="Paper", command=paper_press)
button3 = tk.Button(wind, text="Scissors", command=scissors_press)
button4 = tk.Button(wind, text="↻", command=refresh)


button1.pack(pady=2)
button2.pack(pady=2)
button3.pack(pady=2)
button4.pack(pady=30)

wind.mainloop()
