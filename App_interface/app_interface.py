from tkinter import *
import tkinter.font as font
import os
from functools import partial
#from playsound import playsound
#from tkinter import ttk
#from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import time
from tkinter import font


class Entry_Box(Entry):
    def __init__(self, window_place,canvas,x_position, y_position, size_width, size_height, image_path, round_edge, color):
        self.window = window_place
        self.canvas = canvas
        self.x_position = x_position
        self.y_position = y_position
        self.size_width = size_width
        self.size_height = size_height
        self.image_path = image_path
        self.round_edge = round_edge
        self.color = color
        super().__init__(
            self.window,
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
        self.__canvas_background = self.canvas.create_image(
            self.x_position + self.size_width / 2,
            self.y_position + self.size_height / 2,
            image=self.__entry_image)

    def Place(self):
        self.canvas.create_window(self.x_position + self.__distance_radius_calculator() + 2,
                                  self.y_position + 2,
                                  anchor='nw',
                                  width=self.size_width - (self.__distance_radius_calculator() * 2) - (2) * 2,
                                  height=self.size_height - 2,
                                  window=self)
    # def place_warun(self):
    #     self.place(
    #         x=self.x_position + self.__distance_radius_calculator() + 2,
    #         y=self.y_position + 2,
    #         width=self.size_width - (self.__distance_radius_calculator() * 2) - (2) * 2,
    #         height=self.size_height - 2)

    def Destroy(self):
        self.canvas.delete(self.__canvas_background)
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


class Restore_window():
    def __init__(self, window):
        self.window = window
        self.top = Toplevel(self.window, takefocus=True)
        # self.window.withdraw()
        # self.window.deiconify()
        self.top.geometry("478x302")
        self.top.title("Restore Password")
        # self.top.transient(self.window)
        # self.window.deiconify()
        # self.window.transient(self.top)
        self.background_canvas = Canvas(
            self.top,
            bg="black",
            height=302,
            width=478,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.background_canvas.place(x=0, y=0)

        self.entry_restore_mail = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47,
                                            "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/Resore_Mail.png",
                                            5, "#3c3838")
        self.entry_restore_mail.background_canvas_image()
        self.entry_restore_mail.Place()

        self.img_cancel = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/Cancel.png")
        self.but_cancel = Button(self.top,
                                 image=self.img_cancel,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground="black",
                                 bg="black",
                                 command=self.btn_cancel_clicked,
                                 relief='flat')
        self.but_cancel_window = self.background_canvas.create_window(127, 186, window=self.but_cancel, anchor='nw')

        self.img_restore = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/Restore.png")
        self.but_restore = Button(self.top,
                                  image=self.img_restore,
                                  bd=0,
                                  activebackground="black",
                                  bg="black",
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief='flat',
                                  command=self.btn_restore_clicked)
        self.but_restore_window = self.background_canvas.create_window(280, 186, window=self.but_restore,
                                                                       anchor='nw')
        # self.but_restore.place
        # x=280, y=186,
        # width=76, height=37

        self.restore_password_label = self.background_canvas.create_text(23, 17,
                                                                         anchor='nw',
                                                                         text="Restore Password",
                                                                         font=font.Font(family='Ubuntu-Regular',
                                                                                        size=28), fill="white")

        self.restore_mail_label = self.background_canvas.create_text(59, 103,
                                                                     anchor='nw',
                                                                     text="Mail",
                                                                     font=font.Font(
                                                                         family='Ubuntu-Regular',
                                                                         size=10,
                                                                         weight='bold',
                                                                         slant='italic'),
                                                                     fill="#3c3838")

        self.message_label = self.background_canvas.create_text(111, 73,
                                                                anchor='nw',
                                                                text="",
                                                                font=font.Font(
                                                                    family='Ubuntu-Regular',
                                                                    size=10,
                                                                    weight='bold',
                                                                    slant='italic'),
                                                                fill="white")

    def btn_cancel_clicked(self):
        self.top.destroy()

    def btn_restore_clicked(self):
        # Jesli jakis email wystepuje w bazie danych to wyswielt, zielony komunikat, resstore massage was send
        if self.entry_restore_mail.get() == "admin@op.pl":
            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(111, 73,
                                                                    anchor='nw',
                                                                    text="Email was send, check your inbox",
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=10,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="#159C2B")
        else:
            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(111, 73,
                                                                    anchor='nw',
                                                                    text="Email not exsist",
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=10,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="#AB3131")


class Register_menu():
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.password_visibility = False
        self.comunicat_label = canvas.create_text(0, 0, text='')

        self.entry_nickname = Entry_Box(self.window, self.canvas, 494, 50, 255, 45,
                                        "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                        "#3c3838")
        self.entry_nickname.background_canvas_image()
        self.entry_nickname.Place()

        self.entry_mail = Entry_Box(self.window, self.canvas, 494, 120, 255, 45,
                                    "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                    "#3c3838")
        self.entry_mail.background_canvas_image()
        self.entry_mail.Place()

        self.entry_password = Entry_Box(self.window, self.canvas, 494, 190, 255, 45,
                                        "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                        "#3c3838")
        self.entry_password.background_canvas_image()
        self.entry_password.config(show="*")
        self.entry_password.Place()

        self.entry_repassword = Entry_Box(self.window, self.canvas, 494, 260, 255, 45,
                                          "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                          "#3c3838")
        self.entry_repassword.background_canvas_image()
        self.entry_repassword.config(show="*")
        self.entry_repassword.Place()

        self.nickname_label = self.canvas.create_text(494, 33, anchor='nw', text="Nickname",
                                                      font=font.Font(family='Ubuntu-Regular',
                                                                     size=10, weight='bold', slant='italic'),
                                                      fill="#3c3838")

        self.mail_label = self.canvas.create_text(494, 103, anchor='nw', text="Mail",
                                                  font=font.Font(family='Ubuntu-Regular',
                                                                 size=10, weight='bold', slant='italic'),
                                                  fill="#3c3838")

        self.password_label = self.canvas.create_text(494, 173, anchor='nw', text="Password",
                                                      font=font.Font(family='Ubuntu-Regular',
                                                                     size=10, weight='bold', slant='italic'),
                                                      fill="#3c3838")

        self.repassword_label = self.canvas.create_text(494, 243, anchor='nw', text="Re-Password",
                                                        font=font.Font(family='Ubuntu-Regular',
                                                                       size=10, weight='bold', slant='italic'),
                                                        fill="#3c3838")

        self.img_register = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/buttonBox_register.png")
        self.but_register = Button(self.window,
                                   image=self.img_register,
                                   activebackground="#141213",
                                   bg="#141213",
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=self.registerclick,
                                   relief="flat")

        self.but_register.place(x=489, y=330, width=260, height=58)

        self.but_backTologin = Button(self.window, text="Back to the login page", font="Verdana 10 underline",
                                      relief='flat',
                                      fg="#3c3838", bg="#141213",
                                      activebackground="#141213", bd=0, highlightbackground="#141213",
                                      command=self.back_to_login_page)

        # but_forgot = canvas.create_window(569,212, width=106,height=14, anchor='nw', window=but_forgot_password )
        self.but_backTologin.place(
            x=491, y=384,
            width=255,
            height=16)

        self.img_show_password = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/close_eye.png")
        self.img_unshow_password = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/open_eye.png")
        self.but_show_password = Button(self.window,
                                        image=self.img_show_password,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        bg="#141213",
                                        activebackground="#141213",
                                        command=self.show_password,
                                        relief="flat")

        self.but_show_password_window = self.canvas.create_window(755, 268, anchor='nw', window=self.but_show_password)

    def __del__(self):
        self.entry_nickname.Destroy()
        self.entry_mail.Destroy()
        self.entry_password.Destroy()
        self.entry_repassword.Destroy()
        self.but_register.destroy()
        self.but_backTologin.destroy()
        self.canvas.delete(self.nickname_label)
        self.canvas.delete(self.mail_label)
        self.canvas.delete(self.password_label)
        self.canvas.delete(self.repassword_label)
        self.canvas.delete(self.comunicat_label)
        self.but_show_password.destroy()

    def registerclick(self):
        print('register__pressed')
        self.canvas.delete(self.comunicat_label)
        if self.entry_password.get() != self.entry_repassword.get():
            self.canvas.delete(self.comunicat_label)
            self.comunicat_label = self.canvas.create_text(491, 12, text='Passowrd is not the same', fill="#AB3131")
        if self.entry_nickname == "admin":
            self.canvas.delete(self.comunicat_label)
            self.comunicat_label = self.canvas.create_text(491, 12, text='User is exsist', fill="#AB3131")
        if self.entry_mail.get() == "admin@mail.com":
            self.canvas.delete(self.comunicat_label)
            self.comunicat_label = self.canvas.create_text(491, 12, text='User is exist', fill="#AB3131")
        else:
            self.canvas.delete(self.comunicat_label)
            self.comunicat_label = self.canvas.create_text(491, 12, text='Succesfully registrated', fill="#159C2B")

    def back_to_login_page(self):
        self.__del__()
        Login_menu(self.window, self.canvas)

    def show_password(self):
        # global password_visibility
        if self.password_visibility == False:
            self.password_visibility = True
            self.entry_password.config(show="")
            self.entry_repassword.config(show="")
            self.but_show_password.config(image=self.img_unshow_password)
        else:
            self.password_visibility = False
            self.entry_password.config(show="*")
            self.entry_repassword.config(show="*")
            self.but_show_password.config(image=self.img_show_password)


class Login_menu():
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.password_visibility = False
        self.comunicat_label = canvas.create_text(0, 0, text='')

        self.entry_password = Entry_Box(self.window, self.canvas, 494, 162, 255, 45,
                                        "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                        "#3c3838")
        self.entry_password.background_canvas_image()
        self.entry_password.config(textvariable=StringVar(self.window, value="Password"))
        self.entry_password.Place()
        self.entry_password.bind("<FocusIn>", self.show_register_password)
        self.entry_password.bind("<FocusOut>", self.unshow_register_password)

        self.entry_login = Entry_Box(self.window, self.canvas, 494, 92, 255, 45,
                                     "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5,
                                     "#3c3838")
        # entry_login.set_default_text("Nickname")
        self.entry_login.config(textvariable=StringVar(self.window, value="Nickname"))
        self.entry_login.background_canvas_image()
        self.entry_login.Place()
        self.entry_login.bind("<FocusIn>", self.show_register_login)
        self.entry_login.bind("<FocusOut>", self.unshow_register_login)

        self.img_login = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/buttonBox_login.png")
        self.but_login = Button(
            image=self.img_login,
            activebackground="#141213",
            bg="#141213",
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_login_clicked,
            relief="flat")

        self.but_login.place(
            x=489, y=273,
            width=260,
            height=51)

        self.img_register = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/buttonBox_register.png")
        self.but_register = Button(self.window,
                                   image=self.img_register,
                                   activebackground="#141213",
                                   bg="#141213",
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=self.btn_register_clicked,
                                   relief="flat")

        self.but_register.place(
            x=489,
            y=330,
            width=260,
            height=58)

        self.but_forgot_password = Button(self.window, text="Forgot Password", font="Verdana 10 underline",
                                          relief='flat',
                                          fg="#3c3838", bg="#141213",
                                          activebackground="#141213", bd=0, highlightbackground="#141213",
                                          command=self.btn_forgot_clicked)

        # but_forgot = canvas.create_window(569,212, width=106,height=14, anchor='nw', window=but_forgot_password )
        self.but_forgot_password.place(
            x=569, y=212,
            width=106,
            height=16)

        self.img_show_password = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/close_eye.png")
        self.img_unshow_password = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/open_eye.png")
        self.but_show_password = Button(
            image=self.img_show_password,
            borderwidth=0,
            highlightthickness=0,
            bg="#141213",
            activebackground="#141213",
            command=self.show_password,
            relief="flat")

        self.but_show_password_window = self.canvas.create_window(755, 169, anchor='nw', window=self.but_show_password)
        # but_show_password.place(
        #     x = 755, y = 169,
        #     width = 31,
        #     height = 31)

        self.nickname_label = self.canvas.create_text(494, 75, anchor='nw', text="Nickname",
                                                      font=font.Font(family='Ubuntu-Regular',
                                                                     size=10, weight='bold', slant='italic'),
                                                      fill="#3c3838")

        self.password_label = self.canvas.create_text(494, 145, anchor='nw', text="Password",
                                                      font=font.Font(family='Ubuntu-Regular',
                                                                     size=10, weight='bold', slant='italic'),
                                                      fill="#3c3838")

    def btn_clicked(self):
        print("Button Clicked")

    # def btn_cancel_clicked(self):
    #     self.top.destroy()
    #
    # def btn_restore_clicked(self):
    #     #Jesli jakis email wystepuje w bazie danych to wyswielt, zielony komunikat, resstore massage was send
    #     if self.entry_restore_mail.get() == "admin@op.pl":
    #         self.background_canvas.delete(self.message_label)
    #         self.message_label = self.background_canvas.create_text(111, 73,
    #                                                       anchor='nw',
    #                                                       text="Email was send, check your inbox",
    #                                                       font=font.Font(
    #                                                           family='Ubuntu-Regular',
    #                                                           size=10,
    #                                                           weight='bold',
    #                                                           slant='italic'),
    #                                                       fill="#159C2B")
    #     else:
    #         self.background_canvas.delete(self.message_label)
    #         self.message_label = self.background_canvas.create_text(111, 73,
    #                                                       anchor='nw',
    #                                                       text="Email not exsist",
    #                                                       font=font.Font(
    #                                                           family='Ubuntu-Regular',
    #                                                           size=10,
    #                                                           weight='bold',
    #                                                           slant='italic'),
    #                                                       fill="#AB3131")

    def btn_forgot_clicked(self):
        Restore_window(self.window)
        # self.top = Toplevel(self.window,takefocus=True)
        # #self.window.withdraw()
        # #self.window.deiconify()
        # self.top.geometry("478x302")
        # self.top.title("Restore Password")
        # #self.top.transient(self.window)
        # #self.window.deiconify()
        # #self.window.transient(self.top)
        # self.background_canvas = Canvas(
        #     self.top,
        #     bg="black",
        #     height=302,
        #     width=478,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge")
        # self.background_canvas.place(x=0, y=0)
        #
        # self.entry_restore_mail = Entry_Box(self.top,self.background_canvas,61, 122, 355, 47, "Resore_Mail.png", 5, "#3c3838")
        # self.entry_restore_mail.background_canvas_image()
        # self.entry_restore_mail.Place()
        #
        # self.img_cancel = PhotoImage(file=f"Cancel.png")
        # self.but_cancel = Button(self.top,
        #                     image=self.img_cancel,
        #                     bd=0,
        #                     borderwidth=0,
        #                     highlightthickness=0,
        #                     activebackground="black",
        #                     bg="black",
        #                     command=self.btn_cancel_clicked,
        #                     relief='flat')
        # self.but_cancel_window = self.background_canvas.create_window(127, 186, window=self.but_cancel, anchor='nw')
        #
        # self.img_restore = PhotoImage(file=f"Restore.png")
        # self.but_restore = Button(self.top,
        #                           image=self.img_restore,
        #                           bd=0,
        #                           activebackground="black",
        #                           bg="black",
        #                           borderwidth=0,
        #                           highlightthickness=0,
        #                           relief='flat',
        #                           command=self.btn_restore_clicked)
        # self.but_restore_window = self.background_canvas.create_window(280, 186, window=self.but_restore, anchor='nw')
        # # self.but_restore.place
        # # x=280, y=186,
        # # width=76, height=37
        #
        #
        # self.restore_password_label = self.background_canvas.create_text(23,17,
        #                                                                  anchor='nw',
        #                                                                  text="Restore Password",
        #                                                                  font=font.Font(family='Ubuntu-Regular',
        #                                                                  size=28), fill="white")
        #
        # self.restore_mail_label = self.background_canvas.create_text(59, 103,
        #                                                   anchor='nw',
        #                                                   text="Mail",
        #                                                   font=font.Font(
        #                                                       family='Ubuntu-Regular',
        #                                                       size=10,
        #                                                       weight='bold',
        #                                                       slant='italic'),
        #                                                   fill="#3c3838")
        #
        # self.message_label = self.background_canvas.create_text(111, 73,
        #                                                   anchor='nw',
        #                                                   text="",
        #                                                   font=font.Font(
        #                                                       family='Ubuntu-Regular',
        #                                                       size=10,
        #                                                       weight='bold',
        #                                                       slant='italic'),
        #                                                   fill="white")

    def show_password(self):
        # global password_visibility
        if self.password_visibility == False:
            self.password_visibility = True
            self.entry_password.config(show="")
            self.but_show_password.config(image=self.img_unshow_password)
        else:
            self.password_visibility = False
            self.entry_password.config(show="*")
            self.but_show_password.config(image=self.img_show_password)

    def btn_register_clicked(self):
        self.__del__()
        Register_menu(self.window, self.canvas)

    # entry_login.Destroy()
    # entry_password.Destroy()
    # but_login.destroy()
    # but_show_password.destroy()
    # but_forgot_password.destroy()
    # print('button destroy')

    def btn_login_clicked(self):
        self.canvas.delete(self.comunicat_label)
        if self.entry_login.get() != 'admin':
            self.comunicat_label = self.canvas.create_text(491, 12, anchor='nw', text="This user not exsist",
                                                           justify='center', fill="#AB3131")

        if self.entry_login.get() == 'admin' and self.entry_password.get() != 'admin':
            self.comunicat_label = self.canvas.create_text(491, 12, anchor='nw', text="Incorrect nickname or password ",
                                                           fill="#AB3131")
        if self.entry_login.get() == 'admin' and self.entry_password.get() == 'admin':
            self.window.destroy()

    def show_register_password(self, event):
        # password_text = StringVar(window, value='')
        if self.entry_password.get() == "Password":
            self.entry_password.config(textvariable=StringVar(self.window, value=""))
        if self.password_visibility == False:
            if self.entry_password.get() != "Password" or self.entry_password.get() == "":
                self.entry_password.config(show="*")
            # else:
            #     password_text = StringVar(window, value='')
            #     entry_password.config(textvariable=password_text)
            else:
                self.entry_password.config(show="*")

    def unshow_register_password(self, event):
        # password_text = StringVar(window, value='Password')
        # if entry_password.get()=="":
        #     entry_password.config(textvariable=password_text)
        print(self.entry_password.get())
        if self.entry_password.get() == "Password" or self.entry_password.get() == "":
            # password_text = StringVar(window, value='Password')

            self.entry_password.config(textvariable=StringVar(self.window, value="Password"))
            self.entry_password.config(show="")
            # entry_password.config(show="*")
            # entry_password.config(textvariable=password_text)
        else:
            if self.password_visibility == False:
                self.entry_password.config(show="*")

    def show_register_login(self, event):
        if self.entry_login.get() == 'Nickname' or self.entry_login.get() == "":
            self.entry_login.config(textvariable=StringVar(self.window, value=''))

    def unshow_register_login(self, event):
        if self.entry_login.get() == 'Nickname' or self.entry_login.get() == "":
            self.entry_login.config(textvariable=StringVar(self.window, value='Nickname'))

    def __del__(self):
        self.entry_login.Destroy()
        self.entry_password.Destroy()
        self.but_login.destroy()
        self.but_show_password.destroy()
        self.but_forgot_password.destroy()
        self.but_register.destroy()
        self.canvas.delete(self.password_label)
        self.canvas.delete(self.nickname_label)
        print('button destroy')






# class Add_playlist_window():
#     def __init__(self,window):

class Playlist_Menu():
    def __init__(self,frame, canvas):
        self.window = frame
        self.canvas = canvas

        self.last_postion = 0
        self.playlist_path = "/home/mateusz/dwhelper"
        self.button_identities = []
        self.canvas.config(
        scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height'])))
        #scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height'])+self.last_postion-9*47)
        #self.canvas.config(scrollregion=(0, 0, int(self.canvas['height']), int(self.canvas['width']) + 200))

        self.vertibar = Scrollbar(
            self.window,
            bd=0,
            #highlightbackground = 'yellow',
            #highlightcolor="red",
            #highlightthickness=0,
            troughcolor=self.canvas['bg'],
            bg="#3C3838",
            #style='arrowless.Vertical.TScrollbar',
            activebackground="green",
            orient='vertical'
        )

        self.vertibar.pack(side=RIGHT, fill=Y)
        self.vertibar.config(command=self.canvas.yview)

        self.canvas.config(
            yscrollcommand=self.vertibar.set
        )

        self.playlist_label = Label(text='   Playlist', font=font.Font(family='Helvetica',
                size=10), bg='black',activebackground='black',fg='white', anchor='w')
        self.playlist_label.place(x=0,y=396, width=283 - int(self.vertibar['width']), height=47)
        self.last_postion = self.last_postion + 47

        self.img_add_playlist = PhotoImage(file=f'/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/ADD2.png')
        self.btn_add_playlist = Button(
            image=self.img_add_playlist,
            activebackground='green',
            bg='black',
            command=self.btn_add_playlist_clicked)
        self.btn_add_playlist.place(
            x=230,y=405,
            width=30,
            height=30)

        # self.btn1= Button(self.window,text ='btn1')
        # self.canvas.create_window(0,60,anchor='nw',window=self.btn1)
        #
        # self.btn2= Button(self.window,text ='btn2')
        # self.canvas.create_window(0,600,anchor='nw',window=self.btn2)



    def btn_nickname_clicked(self):
        print('btn nickname clicked')
        # content.__del__()
        # Setting_menu(contentframe, contentframe_canvas)


    def btn_add_playlist_clicked(self):
        self.top = Toplevel(self.window, takefocus=True)
        # self.window.withdraw()
        # self.window.deiconify()
        self.top.geometry("478x302")
        self.top.title("Add playlist")
        # self.top.transient(self.window)
        # self.window.deiconify()
        # self.window.transient(self.top)
        self.background_canvas = Canvas(
            self.top,
            bg="black",
            height=302,
            width=478,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.background_canvas.place(x=0, y=0)

        self.entry_add_playlist = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47, "Resore_Mail.png",
                                            5, "#3c3838")
        self.entry_add_playlist.background_canvas_image()
        self.entry_add_playlist.Place()

        self.img_cancel = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/cancel_playlist.png")
        self.but_cancel = Button(self.top,
                                 image=self.img_cancel,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground="black",
                                 bg="black",
                                 command=self.btn_cancel_clicked,
                                 relief='flat')
        self.but_cancel_window = self.background_canvas.create_window(127, 186, window=self.but_cancel, anchor='nw')

        self.img_add = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/ADD_playlist.png")
        self.but_add = Button(self.top,
                              image=self.img_add,
                              bd=0,
                              activebackground="black",
                              bg="black",
                              borderwidth=0,
                              highlightthickness=0,
                              relief='flat',
                              command=self.btn_add_clicked)
        self.but_add_window = self.background_canvas.create_window(280, 186, window=self.but_add,
                                                                   anchor='nw')
        # self.but_restore.place
        # x=280, y=186,
        # width=76, height=37

        self.add_playlist_label = self.background_canvas.create_text(23, 17,
                                                                     anchor='nw',
                                                                     text="Add playlist",
                                                                     font=font.Font(family='Ubuntu-Regular',
                                                                                    size=28), fill="white")

        self.playlist_name_label = self.background_canvas.create_text(59, 103,
                                                                      anchor='nw',
                                                                      text="Playlist Name",
                                                                      font=font.Font(
                                                                          family='Ubuntu-Regular',
                                                                          size=10,
                                                                          weight='bold',
                                                                          slant='italic'),
                                                                      fill="#3c3838")

        self.message_label = self.background_canvas.create_text(111, 73,
                                                                anchor='nw',
                                                                text="",
                                                                font=font.Font(
                                                                    family='Ubuntu-Regular',
                                                                    size=10,
                                                                    weight='bold',
                                                                    slant='italic'),
                                                                fill="white")


    def btn_cancel_clicked(self):
        self.top.destroy()

    def create_playlist(self,dir_name):

        path = os.path.join(self.playlist_path,dir_name)

        if not os.path.exists(path):
            os.makedirs(path)



    def btn_add_clicked(self):
        #global button_identities
        # Jesli jakis email wystepuje w bazie danych to wyswielt, zielony komunikat, resstore massage was send
        if self.entry_add_playlist.get() == " " or self.entry_add_playlist.get() == "":
            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(111, 73,
                                                                    anchor='nw',
                                                                    text="You cannot create an unnamed playlist",
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=10,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="#AB3131")

        elif self.entry_add_playlist.get() in app.playlist:
            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(111, 73,
                                                                    anchor='nw',
                                                                    text="Playlist exsist",
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=10,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="#AB3131")
        elif  len(app.playlist) >=20:
            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(111, 73,
                                                                    anchor='nw',
                                                                    text="Cannot add more playlist\n Maximum number of playlist is 20",
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=10,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="#AB3131")
        else:
            self.background_canvas.delete(self.message_label)
            app.playlist.append(self.entry_add_playlist.get())
            temp_label = str(self.entry_add_playlist.get())
            self.temp_button = Button(self.window,
                               text=self.entry_add_playlist.get(),
                               activebackground="green",
                               bg="black",
                               fg='white',
                               highlightbackground='black',
                               bd=0,
                               command=partial(self.btn_playlist_press,len(self.button_identities)),
                               relief="groove")

            self.canvas.create_window(0,app.left.playlist_menu.last_postion, width=283 - int(self.vertibar['width']), height=47,anchor='nw',window=self.temp_button)
            self.canvas.config(scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height'])+self.last_postion))
            print(type(self.temp_button))
            self.button_identities.append(self.temp_button)

            app.left.playlist_menu.last_postion = app.left.playlist_menu.last_postion + 47
            self.top.destroy()
            self.background_canvas.destroy()

            self.create_playlist(temp_label)

    def btn_playlist_press(self,n):
        #global button_identities
        self.bname = self.button_identities[n]
        print(type(self.bname))
        # print('Button', n)
        playlist_name = self.bname['text']
        music_path = os.path.join(self.playlist_path, playlist_name)
        if os.path.exists(music_path):
            list_file = os.listdir(music_path)
            list_file = [extension for extension in list_file if extension.endswith(".mp3")]

            for music in list_file:
                print(f"{music}")



class Left_menu():
    def __init__(self,frame,canvas):
        self.window = frame
        self.canvas = canvas
        self.playlist_path = "/home/mateusz/dwhelper"
        self.button_identities = []

        self.playlist_frame = Frame(self.window, bg='green', relief='flat')
        self.playlist_frame.place(x=0, y=396, width=283, height=517)

        self.playlist_frame_canvas = Canvas(
            self.playlist_frame,
            bg="black",
            height=517,
            width=283,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.playlist_frame_canvas.place(x=0, y=0)


        self.playlist_menu = Playlist_Menu(self.playlist_frame, self.playlist_frame_canvas)





        self.img_allMusic= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/HOME.png")
        self.btn_allMusic = Button(
            text="ALL Music"+20*" ",
            compound='right',
            image=self.img_allMusic,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_allMusic.place(
            x = 0, y = 104,
            width = 283,
            height = 47)

        self.img_myMusic= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/SONG.png")
        self.btn_myMusic = Button(
            text="MY Music"+20*" ",
            compound='right',
            image=self.img_myMusic,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_myMusic.place(
            x = 0, y = 151,
            width = 283,
            height = 47)

        self.img_shareDown= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/shareDOWN.png")
        self.btn_shareDown = Button(
            text="MY Sharing"+18*" ",
            compound='right',
            image=self.img_shareDown,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_shareDown.place(
            x = 0, y = 198,
            width = 283,
            height = 47)

        self.img_shareUP= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/shareUP.png")
        self.btn_shareUP = Button(
            text="Sharing ME"+18*" ",
            compound='right',
            image=self.img_shareUP,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_shareUP.place(
            x = 0, y = 245,
            width = 283,
            height = 47)

        self.img_Favourite= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/HEART.png")
        self.btn_Favourite = Button(
            text="Favourite"+19*" ",
            compound='right',
            image=self.img_Favourite,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_Favourite.place(
            x = 0, y = 292,
            width = 283,
            height = 47)

        self.img_Upload= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/UPLOAD_small.png")
        self.btn_Upload = Button(
            text="Send Music"+18*" ",
            compound='right',
            image=self.img_Upload,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_clicked,
            relief="groove")

        self.btn_Upload.place(
            x = 0, y = 339,
            width = 283,
            height = 47)

        self.distance_label = Label(bg="#3c3838")
        self.distance_label.place(x=0,y=386,
                             width=283,height=10)

        self.image_default_user = PhotoImage(file = f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/Rectangle 1.png")
        self.default_user = Label(self.window,
            image = self.image_default_user,bg='black')
        self.default_user.place(x=21,y=21,width=50,height=50)

        #to jest do poprawienia nie tak definiujemy czcionke,
        self.font_nickname = font.Font(family='Helvetica',size=18, underline=1)
        self.button_nickname = Button(self.window,text='tojama4',font=self.font_nickname,
                                 fg='white',bg='black',relief='flat',
                                 highlightcolor='black',activeforeground='white',
                                 activebackground='black',
                                 bd=0,
                                 command = self.btn_nickname_clicked,
                                 highlightthickness=0, anchor="w")
        self.button_nickname.place(x=79,y=46,width=150,height=25)

    def btn_nickname_clicked(self):
        print('btn nickname clicked')
        # content.__del__()
        # Setting_menu(contentframe, contentframe_canvas)


    def btn_clicked(self):
        print("Button Clicked")


class Play_menu():
    def __init__(self,frame, canvas):
        self.window = frame
        self.canvas = canvas
        # self.play_img = PhotoImage(file='Button(1).png')
        # self.play_button = Button(self.window, image=self.play_img, bd=0, command=self.play,highlightcolor='black',activeforeground='white',
        #                          activebackground='black',
        #                          highlightthickness=0)
        # pause_button =Button()
        # self.play_button.place(x=712,y=47,width=15.11, height =18.39)
        self.img_music =PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/msuic.png")
        self.music_window = self.canvas.create_image(23,18, anchor='nw', image=self.img_music)

        self.text_labelmusic = self.canvas.create_text(122,18, anchor='nw', text="T.Love - King [Official Music Video] - YouTube.mp3",fill='white')

        self.img_play_once =PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/play_once.png")
        self.but_play_once = Button(self.window,
                                  image=self.img_play_once,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.btn_clicked,
                                  relief='flat')
        self.but_previous_window = self.canvas.create_window(608, 46,width=30, height=30, window=self.but_play_once, anchor='nw')

        self.img_previous =PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/previous.png")
        self.but_previous = Button(self.window,
                                  image=self.img_previous,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.btn_clicked,
                                  relief='flat')
        self.but_previous_window = self.canvas.create_window(664, 46,width=30, height=30, window=self.but_previous, anchor='nw')

        self.img_play =PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/play.png")
        self.but_play = Button(self.window,
                                  image=self.img_play,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.btn_clicked,
                                  relief='flat')
        self.but_play_window = self.canvas.create_window(720, 46,width=30, height=30, window=self.but_play, anchor='nw')

        self.img_next = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/next.png")
        self.but_next = Button(self.window,
                               image=self.img_next,
                               bd=0,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground=self.canvas['bg'],
                               bg=self.canvas['bg'],
                               command=self.btn_clicked,
                               relief='flat')
        self.but_next_window = self.canvas.create_window(776, 46, width=30, height=30, window=self.but_next,anchor='nw')

        self.img_shuffle = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/shuffle.png")
        self.but_shuffle = Button(self.window,
                               image=self.img_shuffle,
                               bd=0,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground=self.canvas['bg'],
                               bg=self.canvas['bg'],
                               command=self.btn_clicked,
                               relief='flat')
        self.but_shuffle_window = self.canvas.create_window(832, 46, width=30, height=30, window=self.but_shuffle,anchor='nw')

        self.img_favourite = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/HEART.png")
        self.but_favourite = Button(self.window,
                               image=self.img_favourite,
                               bd=0,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground=self.canvas['bg'],
                               bg=self.canvas['bg'],
                               command=self.btn_clicked,
                               relief='flat')
        self.but_favourite_window = self.canvas.create_window(1304, 46, width=30, height=30, window=self.but_favourite,anchor='nw')

        self.img_share = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/share.png")
        self.but_share = Button(self.window,
                               image=self.img_share,
                               bd=0,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground=self.canvas['bg'],
                               bg=self.canvas['bg'],
                               command=self.btn_share_clicked,
                               relief='flat')
        self.but_favourite_window = self.canvas.create_window(1344, 46, width=30, height=30, window=self.but_share,anchor='nw')

    def btn_clicked(self):
        print('clicked button')

    def btn_share_clicked(self):
        self.top = Toplevel(self.window, takefocus=True)
        self.top.geometry("478x302")
        self.top.title("Share Music")
        self.background_canvas = Canvas(
            self.top,
            bg="black",
            height=302,
            width=478,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.background_canvas.place(x=0, y=0)

        self.entry_add_playlist = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47, "Resore_Mail.png",
                                            5, "#3c3838")
        self.entry_add_playlist.background_canvas_image()
        self.entry_add_playlist.Place()

        self.img_cancel = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/cancel_playlist.png")
        self.but_cancel = Button(self.top,
                                 image=self.img_cancel,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground="black",
                                 bg="black",
                                 command=self.btn_cancel_clicked,
                                 relief='flat')
        self.but_cancel_window = self.background_canvas.create_window(127, 186, window=self.but_cancel, anchor='nw')

        self.img_add = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/playmenu/share_but.png")
        self.but_add = Button(self.top,
                              image=self.img_add,
                              bd=0,
                              activebackground="black",
                              bg="black",
                              borderwidth=0,
                              highlightthickness=0,
                              relief='flat',
                              command=self.share_music_clicked)
        self.but_add_window = self.background_canvas.create_window(280, 186, window=self.but_add,
                                                                   anchor='nw')
        # self.but_restore.place
        # x=280, y=186,
        # width=76, height=37

        self.add_playlist_label = self.background_canvas.create_text(23, 17,
                                                                     anchor='nw',
                                                                     text="Share music",
                                                                     font=font.Font(family='Ubuntu-Regular',
                                                                                    size=28), fill="white")

        self.playlist_name_label = self.background_canvas.create_text(59, 103,
                                                                      anchor='nw',
                                                                      text="Music Name",
                                                                      font=font.Font(
                                                                          family='Ubuntu-Regular',
                                                                          size=10,
                                                                          weight='bold',
                                                                          slant='italic'),
                                                                      fill="#3c3838")

        self.message_label = self.background_canvas.create_text(111, 73,
                                                                anchor='nw',
                                                                text="",
                                                                font=font.Font(
                                                                    family='Ubuntu-Regular',
                                                                    size=10,
                                                                    weight='bold',
                                                                    slant='italic'),
                                                                fill="white")


    def btn_cancel_clicked(self):
        self.top.destroy()

    def share_music_clicked(self):
        print('clicked')



    def play(self):
        pass
        #play_button.destroy()
        #self.pause_img=PhotoImage(file='/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/Pause.png')
        #self.play_button.configure(image=self.pause_img)
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

class Content_search():
    def __init__(self,frame, canvas):
        self.window = frame
        self.canvas = canvas

        self.entry_search = Entry_Box(self.window, self.canvas, 141, 31, 758, 30, "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/Wyszukiwarka.png",
                                            90, "#C4C4C4")
        self.entry_search.background_canvas_image()
        self.entry_search.Place()
        self.entry_search.bind("<Return>", self.entry_search_focus)

        self.img_setting = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/setting_icon.png")
        self.but_setting = Button(self.window,
                                 image=self.img_setting,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground=self.canvas['bg'],
                                 bg=self.canvas['bg'],
                                 command=self.btn_setting_clicked,
                                 relief='flat')
        #self.but_setting_window = self.canvas.create_window(1080, 15, window=self.but_setting, anchor='nw')
        self.but_setting_window = self.canvas.create_window(1080,15,anchor='nw', window=self.but_setting)

    def __del__(self):
        #self.canvas.delete("all")
        #self.entry_search.Destroy()
        #pass
        pass




    def entry_search_focus(self,event):
        print('pressed Enter')

    def btn_setting_clicked(self):
        #app.content.__del__()
        #self.__del__()
        #app.content.content_search.__del__()
        #app.content.content_play.__del__()
        app.content.__del__()
        app.setting = Setting_menu(app.contentframe, app.contentframe_canvas)

class Content_play():
    def __init__(self,frame,canvas):
        self.window = frame
        self.canvas = canvas

        self.last_record_position = 75
        self.button_list = []

        self.canvas.config(
            scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height']) + 200))
        self.vertibar = Scrollbar(
            self.window,
            bd=0,
            troughcolor=self.canvas['bg'],
            bg="#3C3838",
            activebackground="green",
            orient='vertical'
        )

        self.vertibar.pack(side=RIGHT, fill=Y)
        #self.vertibar.place(x=1157-16,y=75)
        #self.vertibar.grid(row=0, column=0, sticky='ns')
        self.vertibar.config(command=self.canvas.yview)
        self.canvas.config(
            yscrollcommand=self.vertibar.set
        )

        self.img_track_pause = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/pause_label.png")
        self.img_track_play= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/play_label.png")
        self.btn_track_play = Button(self.window,
            text="Chłopcy z Placu Broni - Kocham wolność - YouTube.mp3",
            compound='left',
            image=self.img_track_play,
            activebackground="green",
            bg=self.canvas['bg'],
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_track_clicked,
            anchor = "w",
            relief="groove")

        self.btn_track_play_window = self.canvas.create_window(0, 0, window=self.btn_track_play, anchor='nw',width=1157-int(self.vertibar['width']), height=38)


    def btn_track_clicked(self):
        print("label track clicked")
        print(self.btn_track_play['image'])
        if self.btn_track_play['image'] == "pyimage13":
            self.btn_track_play.config(image=self.img_track_pause)
            #playsound(os.path.join("/home/mateusz/dwhelper/ROCK",str(self.btn_track_play['text'])))
        else:
            self.btn_track_play.config(image=self.img_track_play)

    def  __del__(self):
        self.vertibar.destroy()


class Content_menu():
    def __init__(self,frame,canvas):
        self.window = frame
        self.canvas = canvas

        self.content_search_frame = Frame(self.window, bg='black', relief='flat')
        self.content_search_frame.place(
            x=0,
            y=0,
            width=1157,
            height=75)

        self.content_search_canvas = Canvas(
            self.content_search_frame,
            bg="#0F0F0E",
            width=1157,
            height=75,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.content_search_canvas.place(x=0, y=0)

        self.content_play_frame = Frame(self.window, bg='black', relief='flat')
        self.content_play_frame.place(
            x=0,
            y=75,
            width=1157,
            height=910-75)

        self.content_play_canvas = Canvas(
            self.content_play_frame,
            bg="#0F0F0E",
            width=1157,
            height=910-75,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.content_play_canvas.place(x=0, y=0)

        self.content_search = Content_search(self.content_search_frame,self.content_search_canvas)
        self.content_play = Content_play(self.content_play_frame,self.content_play_canvas)

    def __del__(self):
        #self.content_play.__del__()
        #self.content_search.__del__()
        self.content_search_canvas.destroy()
        self.content_play_canvas.destroy()
        self.content_search_frame.destroy()
        self.content_play_frame.destroy()




class Setting_menu():
    def __init__(self,frame,canvas):
        self.window = frame
        self.canvas = canvas

        self.canvas.config(scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height']) + 400))

        """
        style = ttk.Style(self.window)
        style.theme_use("alt")
        # create new scrollbar layout
        style.element_create("arrowless.Vertical.TScrollbar", "from", "alt")
        style.layout('arrowless.Vertical.TScrollbar',
                     [('Vertical.Scrollbar.trough',
                       {'children': [('Vertical.Scrollbar.thumb',
                                      {'expand': '1', 'sticky': 'nswe'})],
                        'sticky': 'ns'})])
        
        style.configure('arrowless.Vertical.TScrollbar',troughcolor='#0F0F0E',borderwidth=0,bordercolor="#0F0F0E",background='#3C3838')
        self.vertibar = ttk.Scrollbar(self.window,
                                      orient = 'vertical',
                                      style = 'arrowless.Vertical.TScrollbar')
        """

        #Other sposob Create
        self.vertibar = Scrollbar(
            self.window,
            bd=0,
            #highlightbackground = 'yellow',
            #highlightcolor="red",
            #highlightthickness=0,
            troughcolor=self.canvas['bg'],
            bg="#3C3838",
            #style='arrowless.Vertical.TScrollbar',
            activebackground="green",
            orient='vertical'
        )

        self.vertibar.pack(side=RIGHT, fill=Y)
        self.vertibar.config(command=self.canvas.yview)

        self.canvas.config(
            yscrollcommand=self.vertibar.set
        )
        #self.canvas.pack(expand=True, side=LEFT, fill=BOTH)


    #8
        self.setting_label = self.canvas.create_text(71, 21,
                                  text="Settings",
                                  font=font.Font(
                                      family='c',
                                      size=48,
                                      weight='bold',
                                      slant='italic'),
                                  anchor='nw',
                                  fill="white")
        # self.setting_label_window = self.canvas.create_window(71, 30,
        #                           anchor='nw',window = self.setting_label)

        self.your_profile_label = self.canvas.create_text(90, 128,
                                  anchor='nw',
                                  text="Your Profile",
                                  font=font.Font(
                                      family='Ubuntu-Regular',
                                      size=36,
                                      weight='bold',
                                      slant='italic'),
                                  fill="white")

        self.img_proffile =PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/setting_account_image.png")
        self.but_profile = Button(self.window,
                                  image=self.img_proffile,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.select_file,
                                  relief='flat')
        self.but_proffile_window = self.canvas.create_window(145, 193, window=self.but_profile, anchor='nw')

        self.but_change_avatar = Button(self.window,
                                 text="Change",
                                 font=('Ubuntu-Regular', 9, 'underline'),
                                 # font=font.Font(amily='Ubuntu-Regular',
                                 #                size=18,
                                 #                weight='normal',
                                 #                slant='roman',
                                 #                underline=1),
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 foreground = "#3c3838",
                                 activebackground=self.canvas['bg'],
                                 bg=self.canvas['bg'],
                                 command=self.select_file,
                                 relief='flat')
        self.but_save_window = self.canvas.create_window(163, 291, window=self.but_change_avatar, anchor='nw')




        self.img_back = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/back_white_img.png")
        self.but_back = Button(self.window,
                                  image=self.img_back,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.btn_back_clicked,
                                  relief='flat')
        self.but_setting_window = self.canvas.create_window(0, 30, window=self.but_back, anchor='nw')

        self.your_nickname_label = self.canvas.create_text(275, 212,
                                                          anchor='nw',
                                                          text="tojama4",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=24,
                                                              weight='normal',
                                                              slant='italic'),
                                                          fill="white")

        self.your_mail_label = self.canvas.create_text(275, 260,
                                                          anchor='nw',
                                                          text="mateusz20.08.1999@gmail.com",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=24,
                                                              weight='normal',
                                                              slant='italic'),
                                                          fill="white")

        self.your_describe_label = self.canvas.create_text(145, 409,
                                                          anchor='nw',
                                                          text="Describe",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=24,
                                                              weight='bold',
                                                              slant='italic'),
                                                          fill="white")
        self.img_describe = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/describe_rectangle.png")
        self.describe_image = self.canvas.create_image(145,456,image=self.img_describe,anchor='nw')

        self.text_describeBox = Text(self.window,
                                     bg='#C4C4C4',
                                     bd=0,
                                     fg='black',
                                     highlightbackground = "#C4C4C4",
                                     highlightcolor="#C4C4C4",
                                     relief="flat",
                                     state=DISABLED,
                                     font=font.Font(
                                         family='Ubuntu-Regular',
                                         size=10,
                                         weight='normal',
                                         slant='roman'))

        self.text_describeBox_window = self.canvas.create_window(153,458,anchor='nw',width=808,height=165,window=self.text_describeBox)


        self.img_edit = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/edit_setting.png")
        self.but_edit = Button(self.window,
                                 image=self.img_edit,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground=self.canvas['bg'],
                                 bg=self.canvas['bg'],
                                 command=self.btn_edit_clicked,
                                 relief='flat')
        self.but_edit_window = self.canvas.create_window(785, 647, window=self.but_edit, anchor='nw')

        self.img_save = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/save_setting.png")
        self.but_save = Button(self.window,
                                 image=self.img_save,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground=self.canvas['bg'],
                                 bg=self.canvas['bg'],
                                 command=self.btn_save_clicked,
                                 relief='flat')
        self.but_save_window = self.canvas.create_window(890, 647, window=self.but_save, anchor='nw')

        self.your_change_password_label = self.canvas.create_text(145, 754,
                                                          anchor='nw',
                                                          text="Change Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=24,
                                                              weight='bold',
                                                              slant='italic'),
                                                          fill="white")

        self.your_change_password_label = self.canvas.create_text(145, 819,
                                                          anchor='nw',
                                                          text="Old Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=18,
                                                              weight='normal',
                                                              slant='roman'),
                                                          fill="#3C3838")

        self.entry_new_password = Entry_Box(self.window, self.canvas, 145, 845, 445, 59, "entryBox_setting.png",
                                            5, "#3C3838")
        self.entry_new_password.background_canvas_image()
        self.entry_new_password.Place()

        self.your_change_password_label = self.canvas.create_text(145, 925,
                                                          anchor='nw',
                                                          text="New Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=18,
                                                              weight='normal',
                                                              slant='roman'),
                                                          fill="#3C3838")

        self.entry_old_password = Entry_Box(self.window, self.canvas, 145, 951, 445, 59, "entryBox_setting.png",
                                            5, "#3C3838")
        self.entry_old_password.background_canvas_image()
        self.entry_old_password.Place()

        self.your_change_password_label = self.canvas.create_text(145, 1032,
                                                          anchor='nw',
                                                          text="Re-type Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=18,
                                                              weight='normal',
                                                              slant='roman'),
                                                          fill="#3C3838")

        self.entry_retype_password = Entry_Box(self.window, self.canvas, 145, 1058, 445, 59, "entryBox_setting.png",
                                            5, "#3C3838")
        self.entry_retype_password.background_canvas_image()
        self.entry_retype_password.Place()

        self.img_change = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/change_setting.png")
        self.but_change = Button(self.window,
                                 image=self.img_change,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground=self.canvas['bg'],
                                 bg=self.canvas['bg'],
                                 command=self.btn_clicked,
                                 relief='flat')
        self.but_change_window = self.canvas.create_window(514, 1164, window=self.but_change, anchor='nw')

        #self.myThread = Thread(target = self.get_numer_character)
        # if self.text_describeBox.focus_get():
        #     print('traktor')
        # else:
        #     print('musztarda')
        #https://www.geeksforgeeks.org/python-focus_set-and-focus_get-method/
        #sprawdz plik tkinter_thread.py


    def __del__(self):
        self.vertibar.destroy()
        #self.entry_new_password.Destroy()
        #self.entry_old_password.Destroy()
        #self.entry_retype_password.Destroy()
        self.canvas.delete("all")
        #self.canvas.configure(yscrollcommand=-1)




    def btn_clicked(self):
        print('btn clicked')
#Trzeba jakos sprawdzac to ze obietk nie koze miec wiecejniz 900 znakow, monza async libka sprobowac
    # async def get_numer_character(self):
    #     self.state = self.text_describeBox['state']
    #     self.state = str(self.state)
    #     self.state = self.state.lower()
    #     print(self.state)
    #     print(type(self.state))
    #     if self.state == 'normal':
    #         print('slon')
    #     else:
    #         print('pietruszka')
    #
    #     await asyncio.sleep(1)

    #zeby trad dzialal prawdopodobnei trzbe awalanc z glowej petlia nie z tej kalsy iodolwac siedo danej metody
    # setting = Setting_menu(window, canvas)
    #myTread = Thread(target = self.setting.get_count)
    #myTread.start()

    def get_count(self):
        self.state = self.text_describeBox['state']
        self.state = str(self.state)
        self.state = self.state.lower()
        print(self.state)
        print(type(self.state))
        if self.state == 'normal':
            print('slon')
        else:
            print('pietruszka')

        time.sleep(1)

    def btn_edit_clicked(self):
        self.text_describeBox.config(state=NORMAL)
        #self.text_describeBox.focus_set()
        #self.get_numer_character
        #self.myThread.start()


    def btn_save_clicked(self):
        self.text_describeBox.config(state=DISABLED)
        A = self.text_describeBox.get("1.0", END)
        print(A.index)
        print(A)
        print(len(A))

    def btn_back_clicked(self):
        self.__del__()
        app.content = Content_menu(self.window,self.canvas)

    def select_file(self):
        filetypes = (
            ('PNG', '*.png'),
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename)




class App_Interface():
    def __init__(self,window):
        self.window = window

        self.playlist = []
        # button_identities = []

        self.leftframe = Frame(self.window, bg='black', relief='flat')
        self.leftframe.place(
            x=0,
            y=0,
            width=283,
            height=910)

        self.leftframe_canvas = Canvas(
            self.leftframe,
            bg="black",
            height=283,
            width=910,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.leftframe_canvas.place(x=0, y=0)

        self.left = Left_menu(self.leftframe, self.leftframe_canvas)

        self.playframe = Frame(self.window, bg='black', relief='flat')
        self.playframe.place(x=0, y=913, width=1440, height=112)

        self.playframe_canvas = Canvas(
            self.playframe,
            bg="black",
            height=112,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.playframe_canvas.place(x=0, y=0)

        self.play_menu = Play_menu(self.playframe, self.playframe_canvas)

        self.contentframe = Frame(self.window, bg='#0F0F0E', relief='flat')
        self.contentframe.place(
            x=283,
            y=0,
            width=1157,
            height=912)

        self.contentframe_canvas = Canvas(
            self.contentframe,
            bg="#0F0F0E",
            height=912,
            width=1157,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.contentframe_canvas.place(x=0, y=0)


        self.content = Content_menu(self.contentframe, self.contentframe_canvas)

        # setting = Setting_menu(contentframe, contentframe_canvas)




if __name__ == '__main__':
    window = Tk()

    window.geometry("800x400")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=400,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/background.png")
    background = canvas.create_image(
        400.0, 200.0,
        image=background_img)

    Login_menu(window, canvas)
    window.resizable(False, False)
    window.mainloop()


    root = Tk()
    root.geometry("1440x1024")
    root.configure(bg="#ffffff")
    root.resizable(False, False)
    app = App_Interface(root)
    root.mainloop()









"""
def test_target():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    print('Current TimeStamp is : %d:%d:%d' % (timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    time.sleep(2)

mytread = Thread(target=test_target)
mytread.start()
"""
