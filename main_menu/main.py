from tkinter import *

password_visibility = False

class Entry_Box(Entry):
    def __init__(self, x_position, y_position, size_width, size_height, image_path, round_edge, color):
        self.x_position = x_position
        self.y_position = y_position
        self.size_width = size_width
        self.size_height = size_height
        self.image_path = image_path
        self.round_edge = round_edge
        self.color = color
        super().__init__(
            bd=0,
            bg=self.color,
            highlightthickness=0)
        # self.entry = Entry(
        #     bd=0,
        #     bg=self.color,
        #     highlightthickness=0)

    def __distance_radius_calculator(self):
        return (self.round_edge / 180) * self.size_height * 2

    def background_canvas_image(self):
        self.__entry_image = PhotoImage(file=self.image_path)
        self.__canvas_background = canvas.create_image(
            self.x_position + self.size_width / 2,
            self.y_position + self.size_height / 2,
            image=self.__entry_image)

    def Place(self):
        self.place(
            x=self.x_position + self.__distance_radius_calculator() + 2,
            y=self.y_position + 2,
            width=self.size_width - (self.__distance_radius_calculator() * 2) - (2) * 2,
            height=self.size_height - 2)

    def Destroy(self):
        canvas.delete(self.__canvas_background)
        self.destroy()
    # def Bind(*args):
    #     #print(args)
    #     Entry.bind(args)
    #
    # def get():
    #     return Entry.get()



    def update(self, **kwargs):
        defaultKwargs = {
            'x_position': self.x_position,
            'y_position': self.y_position,
            'size_width': self.size_width,
            'size_height': self.size_height,
            'image_path': self.image_path,
            'round_edge': self.round_edge,
            'color': self.color}
        kwargs = {**defaultKwargs, **kwargs}

        self.x_position = kwargs['x_position']
        self.y_position = kwargs['y_position']
        self.size_width = kwargs['size_width']
        self.size_height = kwargs['size_height']
        self.image_path = kwargs['image_path']
        self.round_edge = kwargs['round_edge']
        self.color = kwargs['color']

        self.config({"background": self.color})
        self.__entry_image = PhotoImage(file=self.image_path)
        self.background_canvas_image()
        self.Place()



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
    entry_login.Destroy()
    entry_password.Destroy()
    but_login.destroy()
    but_show_password.destroy()
    but_forgot_password.destroy()
    print('button destroy')


def show_register_password(event):
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


def unshow_register_password(event):
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

def show_register_login(event):
    if entry_login.get() == 'Nickname' or entry_login.get() == "":
        entry_login.config(textvariable=StringVar(window, value=''))


def unshow_register_login(event):
    if entry_login.get() == 'Nickname' or entry_login.get() == "":
        entry_login.config(textvariable=StringVar(window, value='Nickname'))

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

entry_password = Entry_Box(494,162,255,45,"entryBox.png",5,"#3c3838")
entry_password.background_canvas_image()
entry_password.config(textvariable=StringVar(window, value="Password"))
entry_password.Place()
entry_password.bind("<FocusIn>",show_register_password)
entry_password.bind("<FocusOut>",unshow_register_password)


entry_login = Entry_Box(494,92,255,45,"entryBox.png",5,"#3c3838")
#entry_login.set_default_text("Nickname")
entry_login.config(textvariable=StringVar(window, value="Nickname"))
entry_login.background_canvas_image()
entry_login.Place()
entry_login.bind("<FocusIn>",show_register_login)
entry_login.bind("<FocusOut>", unshow_register_login)

img_login = PhotoImage(file = f"login_button.png")
but_login = Button(
    image = img_login,
    activebackground="#141213",
    bg="#141213",
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

but_login.place(
    x = 489, y = 273,
    width = 260,
    height = 51)

img_register = PhotoImage(file = f"buttonBox_register.png")
but_register = Button(window,
    image = img_register,
    activebackground = "#141213",
    bg = "#141213",
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_register_clicked,
    relief = "flat")

but_register.place(
    x = 489,
    y = 330,
    width = 260,
    height = 58)

but_forgot_password = Button(window,text="Forgot Password", font= "Verdana 10 underline", relief='flat', fg = "#3c3838",bg = "#141213",
    activebackground="#141213",bd=0,highlightbackground="#141213")

#but_forgot = canvas.create_window(569,212, width=106,height=14, anchor='nw', window=but_forgot_password )
but_forgot_password.place(
    x=569, y=212,
    width = 106,
    height = 16)



img_show_password = PhotoImage(file = f"close_eye.png")
img_unshow_password = PhotoImage(file = f"open_eye.png")
but_show_password = Button(
    image = img_show_password,
    borderwidth=0,
    highlightthickness=0,
    bg = "#141213",
    activebackground="#141213",
    command=show_password,
    relief="flat")

but_show_password_window = canvas.create_window(755,169,anchor='nw', window= but_show_password)
# but_show_password.place(
#     x = 755, y = 169,
#     width = 31,
#     height = 31)



window.resizable(False, False)
window.mainloop()
