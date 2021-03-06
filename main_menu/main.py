from tkinter import *
from tkinter import font

#from ..App_interface import app_interface




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
    def __init__(self,window):
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

        self.entry_restore_mail = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/Resore_Mail.png",
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
    def __init__(self,window, canvas):
        self.window = window
        self.canvas = canvas
        self.password_visibility = False
        self.comunicat_label = canvas.create_text(0, 0, text='')

        self.entry_nickname = Entry_Box(self.window,self.canvas,494, 50, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
        self.entry_nickname.background_canvas_image()
        self.entry_nickname.Place()

        self.entry_mail = Entry_Box(self.window,self.canvas,494, 120, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
        self.entry_mail.background_canvas_image()
        self.entry_mail.Place()

        self.entry_password = Entry_Box(self.window,self.canvas,494, 190, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
        self.entry_password.background_canvas_image()
        self.entry_password.config(show="*")
        self.entry_password.Place()

        self.entry_repassword = Entry_Box(self.window,self.canvas,494, 260, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
        self.entry_repassword.background_canvas_image()
        self.entry_repassword.config(show="*")
        self.entry_repassword.Place()

        self.nickname_label = self.canvas.create_text(494,33, anchor='nw', text="Nickname", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838")

        self.mail_label = self.canvas.create_text(494,103, anchor='nw', text="Mail", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838")

        self.password_label = self.canvas.create_text(494,173, anchor='nw', text="Password", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838")

        self.repassword_label = self.canvas.create_text(494,243, anchor='nw', text="Re-Password", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838")

        self.img_register = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/buttonBox_register.png")
        self.but_register = Button(self.window,
                              image=self.img_register,
                              activebackground="#141213",
                              bg="#141213",
                              borderwidth=0,
                              highlightthickness=0,
                              command=self.registerclick,
                              relief="flat")

        self.but_register.place(x=489, y=330, width=260, height=58)

        self.but_backTologin = Button(self.window, text="Back to the login page", font="Verdana 10 underline", relief='flat',
                                     fg="#3c3838", bg="#141213",
                                     activebackground="#141213", bd=0, highlightbackground="#141213", command=self.back_to_login_page)

        # but_forgot = canvas.create_window(569,212, width=106,height=14, anchor='nw', window=but_forgot_password )
        self.but_backTologin.place(
            x=491, y=384,
            width=255,
            height=16)

        self.img_show_password = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/close_eye.png")
        self.img_unshow_password = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/open_eye.png")
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
        #global password_visibility
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
    def __init__(self,window, canvas):
        self.window = window
        self.canvas = canvas
        self.password_visibility = False
        self.comunicat_label = canvas.create_text(0,0,text='')

        self.entry_password = Entry_Box(self.window,self.canvas,494, 162, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
        self.entry_password.background_canvas_image()
        self.entry_password.config(textvariable=StringVar(self.window, value="Password"))
        self.entry_password.Place()
        self.entry_password.bind("<FocusIn>", self.show_register_password)
        self.entry_password.bind("<FocusOut>", self.unshow_register_password)

        self.entry_login = Entry_Box(self.window, self.canvas, 494, 92, 255, 45, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/entryBox.png", 5, "#3c3838")
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

        self.img_register = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/buttonBox_register.png")
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

        self.but_forgot_password = Button(self.window, text="Forgot Password", font="Verdana 10 underline", relief='flat',
                                     fg="#3c3838", bg="#141213",
                                     activebackground="#141213", bd=0, highlightbackground="#141213", command=self.btn_forgot_clicked)

        # but_forgot = canvas.create_window(569,212, width=106,height=14, anchor='nw', window=but_forgot_password )
        self.but_forgot_password.place(
            x=569, y=212,
            width=106,
            height=16)

        self.img_show_password = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/close_eye.png")
        self.img_unshow_password = PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/open_eye.png")
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

        self.nickname_label = self.canvas.create_text(494,75, anchor='nw', text="Nickname", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838")
        
        self.password_label = self.canvas.create_text(494,145,anchor='nw', text="Password", font=font.Font(family='Ubuntu-Regular',
        size=10, weight='bold', slant='italic'), fill="#3c3838" )

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
        #global password_visibility
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
            self.comunicat_label = self.canvas.create_text(491,12,anchor='nw', text="This user not exsist", justify='center', fill="#AB3131")

        if self.entry_login.get() == 'admin' and self.entry_password.get() != 'admin':
            self.comunicat_label = self.canvas.create_text(491, 12, anchor='nw', text="Incorrect nickname or password ", fill="#AB3131")
        if self.entry_login.get() == 'admin' and self.entry_password.get() == 'admin':
            #self.window.destroy()
            from ..App_interface import app_interface

    def show_register_password(self,event):
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

    def unshow_register_password(self,event):
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

    def show_register_login(self,event):
        if self.entry_login.get() == 'Nickname' or self.entry_login.get() == "":
            self.entry_login.config(textvariable=StringVar(self.window, value=''))

    def unshow_register_login(self,event):
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




""""
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




Login_menu(window,canvas)
window.resizable(False, False)
window.mainloop()
"""
