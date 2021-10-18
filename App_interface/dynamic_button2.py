from tkinter import *
from functools import partial
import os

def get_mp3_file(path):
    list_file = os.listdir(path)
    #print(list_file)
    list_file = [ extension for extension in list_file if extension.endswith(".mp3")]
    #print(list_file)
    return list_file


library ={"ROCK": get_mp3_file("/home/mateusz/dwhelper/ROCK"),"POP": get_mp3_file("/home/mateusz/dwhelper/POP")}


win = Tk()
button_identities = []

#tekst = ['ROCK', 'POP',"JAZZ", "FOLK", "BLUES"]


def change(n):
    # function to get the index and the identity (bname)
    print(n)
    bname = (button_identities[n])
    print(library[bname['text']])


# creating the buttons, assigning a unique argument (i) to run the function (change)
button = Button(win, width=10, text="ROCK", command=partial(change, 0))
button.place(x=0, y=0*30)
# add the button's identity to a list:
button_identities.append(button)

button = Button(win, width=10, text="POP", command=partial(change, 1))
button.place(x=0, y=1 * 30)
# add the button's identity to a list:
button_identities.append(button)

# just to show what happens:
print(button_identities)

win.mainloop()




