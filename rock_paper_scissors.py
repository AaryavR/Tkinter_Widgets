from tkinter import *
from PIL import Image, ImageTk
import random 

root = Tk()
root.title('Rock Paper Scissors') 
root.geometry('1000x700')

options = ["rock", "paper", "scissors"]
choice = ""
bot = ""
result_text = ""

def choose_rock():
    global choice
    choice = "rock"
    play_game()

def choose_paper():
    global choice
    choice = "paper"
    play_game()

def choose_scissors():
    global choice
    choice = "scissors"
    play_game()

def play_game():
    global bot, result_text
    bot = random.choice(options)

    result_text = get_result(choice, bot)

    player_label.config(text=f"Your Choice: {choice}")
    bot_label.config(text=f"Bot's Choice: {bot}")

    if result_text == "win":
        result_label.config(text="You Win!", fg="green")
    elif result_text == "lose":
        result_label.config(text="You Lose!", fg="red")
    else:
        result_label.config(text="It's a Draw!", fg="blue")

def get_result(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def reset_game():
    global choice, bot, result_text
    choice = ""
    bot = ""
    result_text = ""
    player_label.config(text="Your Choice: ")
    bot_label.config(text="Bot's Choice: ")
    result_label.config(text="Choose your move!", fg="black")

# Labels for images
upload = Image.open('rock.jpg')
rock = ImageTk.PhotoImage(upload)
label_rock = Label(root, image=rock, height=350, width=300)
label_rock.place(x=20, y=20)
rb = Button(root, text="Select", command=lambda: choose_rock())
rb.place(x=150, y=320)

upload = Image.open('paper.jpg')
paper = ImageTk.PhotoImage(upload)
label_paper = Label(root, image=paper, height=350, width=300)
label_paper.place(x=320, y=20)
pb = Button(root, text="Select", command=lambda: choose_paper())
pb.place(x=450, y=320)

upload = Image.open('scissors.jpg')
scissors = ImageTk.PhotoImage(upload)
label_scissors = Label(root, image=scissors, height=350, width=300)
label_scissors.place(x=620, y=20)
sb = Button(root, text="Select", command=lambda: choose_scissors())
sb.place(x=750, y=320)

# Result labels
player_label = Label(root, text="Your Choice: ", font=("Arial", 16))
player_label.place(x=100, y=400)

bot_label = Label(root, text="Bot's Choice: ", font=("Arial", 16))
bot_label.place(x=100, y=450)

result_label = Label(root, text="Choose your move!", font=("Arial", 24, "bold"))
result_label.place(x=350, y=520)

reset_button = Button(root, text="Play Again", command=reset_game, font=("Arial", 14))
reset_button.place(x=440, y=600)

root.mainloop() 