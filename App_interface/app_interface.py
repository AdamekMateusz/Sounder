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

        self.image_default_user = PhotoImage(file = f"Rectangle 1.png")
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
        self.play_img = PhotoImage(file='Button(1).png')
        self.play_button = Button(self.window, image=self.play_img, bd=0, command=self.play,highlightcolor='black',activeforeground='white',
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

class Content_search():
    def __init__(self,frame, canvas):
        self.window = frame
        self.canvas = canvas

        self.entry_search = Entry_Box(self.window, self.canvas, 141, 31, 758, 30, "Wyszukiwarka.png",
                                            90, "#C4C4C4")
        self.entry_search.background_canvas_image()
        self.entry_search.Place()
        self.entry_search.bind("<Return>", self.entry_search_focus)

        self.img_setting = PhotoImage(file=f"setting_icon.png")
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

        self.img_track_pause = PhotoImage(file=f"pause_label.png")
        self.img_track_play= PhotoImage(file=f"play_label.png")
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

        self.canvas.config(scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height']) + 200))

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

        self.img_proffile =PhotoImage(file=f"setting_account_image.png")
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




        self.img_back = PhotoImage(file=f"back_white_img.png")
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
        self.img_describe = PhotoImage(file=f"describe_rectangle.png")
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


        self.img_edit = PhotoImage(file=f"edit_setting.png")
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

        self.img_save = PhotoImage(file=f"save_setting.png")
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

        self.img_change = PhotoImage(file=f"change_setting.png")
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
        self.playframe_canvas.place(x=0, y=913)

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



window = Tk()
window.geometry("1440x1024")
window.configure(bg="#ffffff")
window.resizable(False, False)

app = App_Interface(window)


window.mainloop()




"""
def test_target():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    print('Current TimeStamp is : %d:%d:%d' % (timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    time.sleep(2)

mytread = Thread(target=test_target)
mytread.start()
"""
