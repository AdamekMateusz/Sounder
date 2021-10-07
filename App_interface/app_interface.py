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


canvas_button_img = PhotoImage(file=f"home_alt_fill.png")
b0 = Button(
    image=canvas_button_img,
    activebackground="black",
    bg="black",
    command=btn_clicked,
    relief="groove")

b0.place(
    x = 489, y = 330,
    width = 50,
    height = 50)

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
