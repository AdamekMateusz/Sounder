from tkinter import *
import tkinter.font as font

playlist = []

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
        self.place(
            x=self.x_position + self.__distance_radius_calculator() + 2,
            y=self.y_position + 2,
            width=self.size_width - (self.__distance_radius_calculator() * 2) - (2) * 2,
            height=self.size_height - 2)

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





# class Add_playlist_window():
#     def __init__(self,window):





class Left_menu():
    def __init__(self,frame,canvas):
        self.window = frame
        self.canvas = canvas


        self.img_allMusic= PhotoImage(file=f"HOME.png")
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

        self.img_myMusic= PhotoImage(file=f"SONG.png")
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

        self.img_shareDown= PhotoImage(file=f"shareDOWN.png")
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

        self.img_shareUP= PhotoImage(file=f"shareUP.png")
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

        self.img_Favourite= PhotoImage(file=f"HEART.png")
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

        self.img_Upload= PhotoImage(file=f"UPLOAD_small.png")
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

        self.playlist_label = Label(text='   Playlist', font=font.Font(family='Helvetica',
                size=10), bg='black',activebackground='black',fg='white', anchor='w')
        self.playlist_label.place(x=0,y=396, width=200, height=47)

        self.last_postion = 396
        self.img_add_playlist = PhotoImage(file=f'ADD2.png')
        self.btn_add_playlist = Button(
            image=self.img_add_playlist,
            activebackground='green',
            bg='black',
            command=self.btn_add_playlist_clicked)
        self.btn_add_playlist.place(
            x=230,y=405,
            width=30,
            height=30)

        self.image_default_user = PhotoImage(file = f"Rectangle 1.png")
        self.default_user = Label(leftframe,
            image = self.image_default_user,bg='black')
        self.default_user.place(x=21,y=21,width=50,height=50)

        #to jest do poprawienia nie tak definiujemy czcionke,
        self.font_nickname = font.Font(family='Helvetica',size=18, underline=1)
        self.button_nickname = Button(leftframe,text='tojama4',font=self.font_nickname,
                                 fg='white',bg='black',relief='flat',
                                 highlightcolor='black',activeforeground='white',
                                 activebackground='black',
                                 bd=0,
                                 highlightthickness=0, anchor="w")
        self.button_nickname.place(x=79,y=46,width=150,height=25)

    def btn_clicked(self):
        print("Button Clicked")

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

        self.img_cancel = PhotoImage(file=f"cancel_playlist.png")
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

        self.img_add = PhotoImage(file=f"ADD_playlist.png")
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

    def btn_add_clicked(self):
        global playlist
        # Jesli jakis email wystepuje w bazie danych to wyswielt, zielony komunikat, resstore massage was send
        if self.entry_add_playlist.get() in playlist:
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
        else:
            self.background_canvas.delete(self.message_label)
            playlist.append(self.entry_add_playlist.get())
            temp = str(self.entry_add_playlist.get())
            self.temp = Button(self.window,
                               text=self.entry_add_playlist.get(),
                               activebackground="green",
                               bg="black",
                               fg='white',
                               highlightbackground='black',
                               bd=0,
                               command=self.btn_press,
                               relief="groove").place(x=0, y=left.last_postion + 47, width=283, height=47)

            left.last_postion = left.last_postion + 47
            self.top.destroy()
            self.background_canvas.destroy()
            # .place(x=0,y=443,width=283,height=47)

    def btn_press(self):
        print("Button name: ")



class Play_menu():
    def __init__(self,frame, canvas):
        self.play_img = PhotoImage(file='Button(1).png')
        self.play_button = Button(playframe, image=self.play_img, bd=0, command=self.play,highlightcolor='black',activeforeground='white',
                                 activebackground='black',
                                 highlightthickness=0)
        pause_button =Button()
        self.play_button.place(x=712,y=47,width=15.11, height =18.39)

    def play(self):
        #play_button.destroy()
        self.pause_img=PhotoImage(file='Pause.png')
        self.play_button.configure(image=self.pause_img)
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



window = Tk()
window.geometry("1440x1024")
window.configure(bg="#ffffff")
window.resizable(False, False)

leftframe = Frame(window,bg='black', relief='flat')
leftframe.place(
    x=0,
    y=0,
    width=283,
    height=910)

leftframe_canvas = Canvas(
    leftframe,
    bg = "black",
    height = 283,
    width = 910,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
leftframe_canvas.place(x = 0, y = 0)

left = Left_menu(leftframe, leftframe_canvas)

playframe = Frame(window,bg='black',relief='flat')
playframe.place(x=0,y=913, width=1440,height=112)

playframe_canvas = Canvas(
    playframe,
    bg = "black",
    height = 112,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
playframe_canvas.place(x = 0, y = 913)

Play_menu(playframe, playframe_canvas)

linelabel = Label(window, bg='#3c3838',relief='flat')
linelabel.place(x=0,y=910,width=1440, height=3)


window.mainloop()
