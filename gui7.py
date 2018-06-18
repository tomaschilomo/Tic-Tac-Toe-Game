import tkinter as tk
import pdb as p

win = {"pair1" : [1,2,3], "pair2": [4,5,6], "pair3": [7,8,9]}
tester = lambda array, y=range(1,10): False not in [val in array for val in y]
target = [val for val in range(1,10)]

# Logic for winning the game
def checker(player):
    if tester(player, win["pair1"]) or tester(player, win["pair2"]) or tester(player, win["pair3"]):
        return True
    elif tester(player,[y[0] for x,y in win.items()]) or tester(player, [y[1] for x,y in win.items()]) or tester(player,[y[2] for x,y in win.items()]):
        return True
    elif tester(player,[1,5,9]) or tester(player,[3,5,7]):
        return True
    else:
        return False


# Layout Creation
root = tk.Tk()
root.minsize(600,600)
turn=[]
player_x = []
player_o = []

def count():
    turn.append(1)
    return len(turn)

# Button Functionallity
def btn_change(name):
    
    val = count()

    if val % 2 == 0: 
        data[name].config(image=image_x, state="disabled")
        player_x.append(name+1)

        if checker(player_x):
            end_of_game['text'] = "Player X: Wins"
            end_of_game.place(x=159,y=255)
            for val in data:
                val.config(state="disabled")
    else:
        data[name].config(image=image_o, state="disabled")
        player_o.append(name+1)

        if checker(player_o):
            end_of_game['text'] = "Player O: Wins"
            end_of_game.place(x=159,y=255)
            for val in data:
                val.config(state="disabled")
    
def restart():
    for val in data:
        val.config(image=image_blank, state="active")
    player_o.clear()
    player_x.clear()
    turn.clear()
    end_of_game.place_forget()      

# Button Images
image_blank = tk.PhotoImage(file="blank.png")
image_x=tk.PhotoImage(file="X.png")
image_o=tk.PhotoImage(file="O.png")

data = []

# Button and Label creation
for val in range(9):
    data.append(tk.Button(root, image=image_blank, state="normal",
     command= lambda name = val: btn_change(name)))

title = tk.Button(root, justify=tk.LEFT, padx=10 ,text="TIC-TAC-TOE",fg="black"
,bg ="green", font="Helvatica 20 bold", disabledforeground="black", state="disabled")
title.pack()

btn_restart = tk.Button(root, text="Click HERE TO RESTART", font="Helvatica 18 bold", bg="green",command=restart)

# End of game
end_of_game = tk.Label(root,compound = tk.CENTER,text=win, fg="red", font="Helvatica 30 bold", bg="black")

# Button Placement
data[0].place(x=75, y=75)
data[1].place(x=225, y=75)
data[2].place(x=375, y=75)
data[3].place(x=75, y=220)
data[4].place(x=225, y=220)
data[5].place(x=375, y=220)
data[6].place(x=75, y=365)
data[7].place(x=225, y=365)
data[8].place(x=375, y=365)
btn_restart.pack(side="bottom")

root.mainloop()
