from tkinter import *
import tkinter.font as font
window = Tk()
window.geometry("1440x1024")
window.configure(bg="#ffffff")

leftframe = Frame(window,bg='black', relief='flat')
leftframe.place(
    x=0,
    y=0,
    width=283,
    height=910)

playframe = Frame(window,bg='black',relief='flat')
playframe.place(x=0,y=913, width=1440,height=112)
linelabel = Label(window, bg='#3c3838',relief='flat')
linelabel.place(x=0,y=910,width=1440, height=3)
def btn_clicked():
    print("Button Clicked")


img_allMusic= PhotoImage(file=f"HOME.png")
btn_allMusic = Button(
    text="ALL Music"+20*" ",
    compound='right',
    image=img_allMusic,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_allMusic.place(
    x = 0, y = 104,
    width = 283,
    height = 47)

img_myMusic= PhotoImage(file=f"SONG.png")
btn_myMusic = Button(
    text="MY Music"+20*" ",
    compound='right',
    image=img_myMusic,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_myMusic.place(
    x = 0, y = 151,
    width = 283,
    height = 47)

img_shareDown= PhotoImage(file=f"shareDOWN.png")
btn_shareDown = Button(
    text="MY Sharing"+18*" ",
    compound='right',
    image=img_shareDown,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_shareDown.place(
    x = 0, y = 198,
    width = 283,
    height = 47)

img_shareUP= PhotoImage(file=f"shareUP.png")
btn_shareUP = Button(
    text="Sharing ME"+18*" ",
    compound='right',
    image=img_shareUP,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_shareUP.place(
    x = 0, y = 245,
    width = 283,
    height = 47)

img_Favourite= PhotoImage(file=f"HEART.png")
btn_Favourite = Button(
    text="Favourite"+19*" ",
    compound='right',
    image=img_Favourite,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_Favourite.place(
    x = 0, y = 292,
    width = 283,
    height = 47)

img_Upload= PhotoImage(file=f"UPLOAD_small.png")
btn_Upload = Button(
    text="Send Music"+18*" ",
    compound='right',
    image=img_Upload,
    activebackground="green",
    bg="black",
    fg='white',
    highlightbackground='black',
    bd=0,
    command=btn_clicked,
    relief="groove")

btn_Upload.place(
    x = 0, y = 339,
    width = 283,
    height = 47)



image_default_user = PhotoImage(file = f"Rectangle 1.png")
default_user = Label(leftframe,
    image = image_default_user,bg='black')
default_user.place(x=21,y=21,width=50,height=50)

font_nickname = font.Font(family='Helvetica',size=18, underline=1)
button_nickname = Button(leftframe,text='tojama4',font=font_nickname,
                         fg='white',bg='black',relief='flat',
                         highlightcolor='black',activeforeground='white',
                         activebackground='black',
                         bd=0,
                         highlightthickness=0, anchor="w")
button_nickname.place(x=79,y=46,width=150,height=25)



def play():
    #play_button.destroy()
    pause_img=PhotoImage(file='Pause.png')
    play_button.configure(image=pause_img)
#     pause_button = Button(playframe, image=pause_img, bd=0, command=pause, highlightcolor='black',
#                          activeforeground='white',
#                          activebackground='black',
#                          highlightthickness=0)
#     pause_button.place(x=712, y=47, width=15.11, height=18.39)
#
# def pause():
#     pause_button.destroy()
#     play_img = PhotoImage(file='Button(1).png')
#     play_button = Button(playframe, image=play_img, bd=0, command=play, highlightcolor='black',
#                          activeforeground='white',
#                          activebackground='black',
#                          highlightthickness=0, bg='black')

play_img = PhotoImage(file='Button(1).png')
play_button = Button(playframe, image=play_img, bd=0, command=play,highlightcolor='black',activeforeground='white',
                         activebackground='black',
                         highlightthickness=0)
pause_button =Button()
play_button.place(x=712,y=47,width=15.11, height =18.39)
window.resizable(False, False)
window.mainloop()
