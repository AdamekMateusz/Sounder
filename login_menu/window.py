from tkinter import *


def btn_clicked():
    print("Button Clicked")

def btn_login_clicked():
    but_register.destroy()
    print('button destroy')
    but_login.place(
    x = 489,
    y = 330)

def show_register(event):
    if entry_password.get() != "Password" or entry_password.get() != "":
        entry_password.config(show="*")
    else:
        password_text = StringVar(window, value='')
        entry_password.config(textvariable=password_text)


def unshow_register(event):
    #password_text = StringVar(window, value='Password')
    # if entry_password.get()=="":
    #     entry_password.config(textvariable=password_text)
    if entry_password.get() == "Password" or entry_password.get() == "":
        password_text = StringVar(window, value='Password')

        entry_password.config(show="*")
        entry_password.config(textvariable=password_text)
    else:
        entry_password.config(show="")



window = Tk()

window.geometry("800x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    400.0, 200.0,
    image=background_img)

# menu_rectangle = canvas.create_rectangle(400,800,0,400, fill= canvas["background"])
# canvas.pack()

# menu_canvas = Canvas(
#     window,
#     bg=canvas['background'],
#     #bg='systemTransparent',
#     height=400,
#     width=800,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge")
# menu_canvas.attributes("-topmost", False)
# menu_canvas.place(x=400,y=0)





img_register = PhotoImage(file = f"img0.png")
but_register = Button(window,
    image = img_register,
    activebackground = canvas['background'],
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

but_register.place(
    x = 489,
    y = 330,
    width = 260,
    height = 58)

img_password = PhotoImage(file = f"img_textBox0.png")
canvas_password = canvas.create_image(
    621.5, 185.5,
    image = img_password)

password_text = StringVar(window, value='Password')
entry_password = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0,
    textvariable=password_text,
    )
entry_password.bind("<Button-1>",show_register)
entry_password.bind("<Return>",unshow_register)


entry_password.place(
    x = 494, y = 162,
    width = 255,
    height = 45)




img_login = PhotoImage(file = f"img_textBox1.png")
canvas_login = canvas.create_image(
    621.5, 115.5,
    image = img_login)

entry_login = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0,
    textvariable='Nickname')

entry_login.place(
    x = 494, y = 92,
    width = 255,
    height = 45)

img_login = PhotoImage(file = f"img1.png")
but_login = Button(
    image = img_login,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_login_clicked,
    relief = "flat")

but_login.place(
    x = 489, y = 273,
    width = 260,
    height = 51)



window.resizable(False, False)
window.mainloop()
