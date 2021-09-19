from tkinter import *

password_visibility = False

def btn_clicked():
    print("Button Clicked")

def show_password():
    global password_visibility
    if password_visibility == False:
        password_visibility = True
        entry_password.config(show="")
        but_show_password.config(image=img_unshow_password)
    else:
        password_visibility = False
        entry_password.config(show="*")
        but_show_password.config(image = img_show_password)


def btn_register_clicked():
    entry_login.destroy()
    entry_password.destroy()
    but_login.destroy()
    canvas.delete(canvas_password)
    canvas.delete(canvas_login)
    but_show_password.destroy()
    print('button destroy')


def show_register(event):
    #password_text = StringVar(window, value='')
    if entry_password.get() == "Password":
        entry_password.config(textvariable=StringVar(window,value=""))
    if password_visibility == False:
        if entry_password.get() != "Password" or entry_password.get() == "":
             entry_password.config(show="*")
        # else:
        #     password_text = StringVar(window, value='')
        #     entry_password.config(textvariable=password_text)
        else:
            entry_password.config(show="*")


def unshow_register(event):
    #password_text = StringVar(window, value='Password')
    # if entry_password.get()=="":
    #     entry_password.config(textvariable=password_text)
    print(entry_password.get())
    if entry_password.get() == "Password" or entry_password.get() == "":
        #password_text = StringVar(window, value='Password')

        entry_password.config(textvariable=StringVar(window,value="Password"))
        entry_password.config(show="")
        #entry_password.config(show="*")
        #entry_password.config(textvariable=password_text)
    else:
        if password_visibility == False:
            entry_password.config(show="*")



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

background_img = PhotoImage(file = f"other.png")
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





img_register = PhotoImage(file = f"register_button.png")
but_register = Button(window,
    image = img_register,
    activebackground = canvas['background'],
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_register_clicked,
    relief = "flat")

but_register.place(
    x = 489,
    y = 330,
    width = 260,
    height = 58)

img_password_entry = PhotoImage(file = f"img_textBox0.png")
canvas_password = canvas.create_image(
    621.5, 185.5,
    image = img_password_entry)

#password_text = StringVar(window, value='Password')
entry_password = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0,
    textvariable=StringVar(window, value='Password'),
    )
entry_password.bind("<FocusIn>",show_register)
entry_password.bind("<FocusOut>",unshow_register)


entry_password.place(
    x = 494, y = 162,
    width = 255,
    height = 45)

img_login_entry = PhotoImage(file = f"img_textBox1.png")
canvas_login = canvas.create_image(
    621.5, 115.5,
    image = img_login_entry)

entry_login = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0,
    textvariable='Nickname')

entry_login.place(
    x = 494, y = 92,
    width = 255,
    height = 45)

img_login = PhotoImage(file = f"login_button.png")
but_login = Button(
    image = img_login,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

but_login.place(
    x = 489, y = 273,
    width = 260,
    height = 51)

img_show_password = PhotoImage(file = f"close_eye_bg.png")
img_unshow_password = PhotoImage(file = f"open_eye_bg.png")
but_show_password = Button(canvas,
    image = img_show_password,
    borderwidth=0,
    highlightthickness=0,
    command=show_password,
    relief="flat")
but_show_password.place(
    x = 755, y = 169,
    width = 31,
    height = 31)

window.resizable(False, False)
window.mainloop()
