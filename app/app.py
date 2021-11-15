import os
from functools import partial
#from playsound import playsound
#from tkinter import ttk
#from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import hashlib
from tkinter import font
from entry_box import *
from paramiko2 import *
from connect import *
from ssh import *
from pydub import AudioSegment
from utilities import Md5, SendMail











# class Add_playlist_window():
#     def __init__(self,window):

class Playlist_Menu():
    def __init__(self,frame, canvas, app_interface=None):
        self.app = app_interface
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

        self.render_playlist_button()
        # self.btn1= Button(self.window,text ='btn1')
        # self.canvas.create_window(0,60,anchor='nw',window=self.btn1)
        #
        # self.btn2= Button(self.window,text ='btn2')
        # self.canvas.create_window(0,600,anchor='nw',window=self.btn2)

    def render_playlist_button(self):
        for item in self.app.playlist:
            self.create_playlist_button(item)


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

        self.entry_add_playlist = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47, "/home/mateusz/PycharmProjects/TkinterProj/inz/main_menu/Resore_Mail.png",
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

    # def create_playlist(self,dir_name):
    #
    #     path = os.path.join(self.playlist_path,dir_name)
    #
    #     if not os.path.exists(path):
    #         os.makedirs(path)



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

        elif self.entry_add_playlist.get() in self.app.playlist:
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
        elif  len(self.app.playlist) >=20:
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
            self.app.conn.execute_update("""INSERT INTO playlist (playlist_name,user_id) VALUES (%s, %s)""",(self.entry_add_playlist.get(),self.app.user_id) )
            self.app.playlist.append(self.entry_add_playlist.get())

            self.create_playlist_button(self.entry_add_playlist.get())
            temp_label = str(self.entry_add_playlist.get())
            # self.temp_button = Button(self.window,
            #                    text=self.entry_add_playlist.get(),
            #                    activebackground="green",
            #                    bg="black",
            #                    fg='white',
            #                    highlightbackground='black',
            #                    bd=0,
            #                    command=partial(self.btn_playlist_press,len(self.button_identities)),
            #                    relief="groove")
            #
            # self.canvas.create_window(0,self.app.left.playlist_menu.last_postion, width=283 - int(self.vertibar['width']), height=47,anchor='nw',window=self.temp_button)
            # self.canvas.config(scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height'])+self.last_postion))
            # print(type(self.temp_button))
            # self.button_identities.append(self.temp_button)
            #
            # self.app.left.playlist_menu.last_postion = self.app.left.playlist_menu.last_postion + 47
            self.top.destroy()
            self.background_canvas.destroy()

            # self.create_playlist(temp_label)

    def btn_playlist_press(self,n):
        self.bname = self.button_identities[n]
        print(type(self.bname))
        # print('Button', n)
        playlist_name = self.bname['text']

        list_of_track = self.app.conn.execute_get("""SELECT * FROM playlist_content WHERE playlist_id = (SELECT id FROM playlist WHERE playlist_name=(%s))""",(playlist_name,))
        print(list_of_track)

        # music_path = os.path.join(self.playlist_path, playlist_name)
        # if os.path.exists(music_path):
        #     list_file = os.listdir(music_path)
        #     list_file = [extension for extension in list_file if extension.endswith(".mp3")]
        #
        #     for music in list_file:
        #         print(f"{music}")

    def create_playlist_button(self,button_name):
        self.temp_button = Button(self.window,
                                  text=button_name,
                                  activebackground="green",
                                  bg="black",
                                  fg='white',
                                  highlightbackground='black',
                                  bd=0,
                                  command=partial(self.btn_playlist_press, len(self.button_identities)),
                                  relief="groove")

        self.canvas.create_window(0, self.last_postion, width=283 - int(self.vertibar['width']),
                                  height=47, anchor='nw', window=self.temp_button)
        self.canvas.config(
            scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height']) + self.last_postion))
        print(type(self.temp_button))
        self.button_identities.append(self.temp_button)

        self.last_postion = self.last_postion + 47


#tutaj ewentualnie dodac to window
class Upload_Muisc():
    def __init__(self, window, app_interface):
        self.app = app_interface
        #self.window = window
        self.top =Toplevel()
        #self.top = Toplevel(self.window, takefocus=True)
        self.filename = None
        # self.window.withdraw()
        # self.window.deiconify()
        self.top.geometry("478x302")
        self.top.title("Upload Music")
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

        self.label_music_name = self.background_canvas.create_text(61, 122, anchor='nw',text="")


        self.img_cancel = PhotoImage(file=f"image/cancel.png")
        self.but_cancel = Button(self.top,
                                 image=self.img_cancel,
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 activebackground="black",
                                 bg="black",
                                 command=self.btn_cancel_clicked,
                                 relief='flat')
        self.but_cancel_window = self.background_canvas.create_window(349, 247, window=self.but_cancel, anchor='nw')

        self.img_open = PhotoImage(file=f"image/open.png")
        self.but_open = Button(self.top,
                                  image=self.img_open,
                                  bd=0,
                                  activebackground="black",
                                  bg="black",
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief='flat',
                                  command=self.btn_open_clicekd)
        self.but_open_window = self.background_canvas.create_window(59, 247, window=self.but_open,
                                                                       anchor='nw')

        self.img_send = PhotoImage(file=f"image/send.png")
        self.but_send = Button(self.top,
                                  image=self.img_send,
                                  bd=0,
                                  activebackground="black",
                                  bg="black",
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief='flat',
                                  command=self.btn_send_clicked)
        self.but_send_window = self.background_canvas.create_window(201, 247, window=self.but_send,
                                                                       anchor='nw')


        self.upload_label = self.background_canvas.create_text(23, 17,
                                                                         anchor='nw',
                                                                         text="Upload Muisc",
                                                                         font=font.Font(family='Ubuntu-Regular',
                                                                                        size=28), fill="white")

        self.message_label = self.background_canvas.create_text(59, 127,
                                                                anchor='nw',
                                                                text='',
                                                                font=font.Font(
                                                                    family='Ubuntu-Regular',
                                                                    size=14,
                                                                    weight='bold',
                                                                    slant='italic'),
                                                                fill="white")
    def select_files(self):
        filetypes = (
            ('mp3', '*.mp3'),
            ('wav', '*.wav')
        )

        filenames = fd.askopenfilenames(
            title='Open audio files',
            initialdir='~/dwhelper/ROCK',
            filetypes=filetypes)

        self.filename = filenames
        return filenames

    def btn_open_clicekd(self):
        self.select_files()
        if self.filename is not None:
            path_file = str(self.filename[0])
            path_dir = os.path.dirname(path_file)
            filename = path_file.replace(path_dir,'')
            filename = filename.replace('/','')

            self.background_canvas.delete(self.message_label)
            self.message_label = self.background_canvas.create_text(59, 127,
                                                                    anchor='nw',
                                                                    text=filename,
                                                                    font=font.Font(
                                                                        family='Ubuntu-Regular',
                                                                        size=14,
                                                                        weight='bold',
                                                                        slant='italic'),
                                                                    fill="white")
            print(path_file)
            if path_file.endswith(".mp3"):
                sound = AudioSegment.from_mp3(path_file)
                self.path_wav = path_file[:-3] + 'wav'
                sound.export(self.path_wav, format="wav")
                self.filename_convert = filename[:-3]+'wav'
                print(self.filename_convert)
            elif path_file.endswith(".wav"):
                self.path_wav = str(path_file)
            else:
                print('cannot convert to wav file')

            self.md5sum_track = Md5.md5sum_file(self.path_wav)
            print(self.md5sum_track)


        else:
            self.message_label.configure("Do not chooise file, try again")



    def btn_send_clicked(self):
        self.background_canvas.delete(self.message_label)
        self.message_warn_label = self.background_canvas.create_text(59, 100,
                                                                anchor='nw',
                                                                text="Wait for moment",
                                                                font=font.Font(
                                                                    family='Ubuntu-Regular',
                                                                    size=10,
                                                                    weight='bold',
                                                                    slant='italic'),
                                                                fill="white")
        time.sleep(2)
        ssh = SSH()
        ssh_session = ssh.connect()
        scp = ssh.scp_client(ssh_session)
        remote_path = os.path.join('/home/pi/app/Users',self.app.nick,'MY_MUSIC')
        scp.put(self.path_wav, remote_path=remote_path)
        scp.close()

        filepath_server = os.path.join(remote_path,self.filename_convert)
        print(filepath_server)
        # stdin, stdout, stderr = self.app.session.exec_command(f"md5sum {filepath_server}")
        ssh2 = SSH()
        ssh2_session = ssh2.connect()
        stdin, stdout, stderr = ssh2_session.exec_command(f"md5sum {filepath_server}")
        out = string = stdout.read().decode('ascii').strip("\n")
        if isinstance(out,str):
            if len(out) >= 32:
                out = out[:32]
            #dodac nalezy handlowanie


        if self.md5sum_track == out:
            self.background_canvas.delete(self.message_warn_label)
            self.message_warn_label = self.background_canvas.create_text(59, 100,
                                                                         anchor='nw',
                                                                         text="Upload correctly, close window",
                                                                         font=font.Font(
                                                                             family='Ubuntu-Regular',
                                                                             size=10,
                                                                             weight='bold',
                                                                             slant='italic'),
                                                                         fill="white")
            #self.app.conn.execute_update("""INSERT INTO userdata (my_music) VALUES ((%s) WHERE nick=(%s))""",(filepath_server,self.app.nick))
            #tutaj w my_music trzab stworzy cdruga tabelke
            self.app.conn.execute_update("""INSERT INTO my_music (track_name, track_path,user_id) VALUES (%s, %s,%s)""",(self.filename_convert,filepath_server,self.app.user_id))
            os.remove(self.path_wav)
            #select * from my_music where user_id=(select id from userdata where nick='sounder')





    def btn_cancel_clicked(self):
        self.top.destroy()

class Left_menu():
    def __init__(self,frame,canvas, app_interface=None):
        self.app = app_interface
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


        self.playlist_menu = Playlist_Menu(self.playlist_frame, self.playlist_frame_canvas,self.app)





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
            command=self.btn_all_music_clicked,
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
            command=self.btn_my_music_clicked,
            relief="groove")

        self.btn_myMusic.place(
            x = 0, y = 151,
            width = 283,
            height = 47)

        self.img_sharing_me= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/shareDOWN.png")
        self.btn_sharing_me = Button(
            text="Sharing ME"+18*" ",
            compound='right',
            image=self.img_sharing_me,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_sharing_me_clicked,
            relief="groove")

        self.btn_sharing_me.place(
            x = 0, y = 198,
            width = 283,
            height = 47)

        self.img_my_sharing= PhotoImage(file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/shareUP.png")
        self.btn_my_sharing = Button(
            text="MY Sharing" + 18 * " ",
            compound='right',
            image=self.img_my_sharing,
            activebackground="green",
            bg="black",
            fg='white',
            highlightbackground='black',
            bd=0,
            command=self.btn_my_sharing_clicked,
            relief="groove")

        self.btn_my_sharing.place(
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
            command=self.favourite_clicked,
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
            command=self.btn_upload_clicked,
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
        self.button_nickname = Button(self.window,text=self.app.nick,font=self.font_nickname,
                                 fg='white',bg='black',relief='flat',
                                 highlightcolor='black',activeforeground='white',
                                 activebackground='black',
                                 bd=0,
                                 command = self.btn_nickname_clicked,
                                 highlightthickness=0, anchor="w")
        self.button_nickname.place(x=79,y=46,width=150,height=25)


    def btn_nickname_clicked(self):
        #content
        self.app.content.__del__()
        self.app.setting.__init__(self.app.contentframe, self.app.contentframe_canvas,self.app)
        print('btn nickname clicked')
        # content.__del__()
        # Setting_menu(contentframe, contentframe_canvas)

    def btn_all_music_clicked(self):
        all_music = self.app.conn.execute_get("""SELECT track_name FROM my_music WHERE user_id=(%s)""",(self.app.user_id,))
        all_music.extend(self.app.conn.execute_get("""SELECT track_name FROM my_sharing WHERE tenant=(%s)""",(self.app.nick,)))
        print(all_music)
        for item in all_music:
            if not str(item[0]) in self.app.all_music:
                self.app.all_music.append(str(item[0]))
        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.all_music)
        #tutja to sie zobaczy czy to tak bedzie dzialac

    def btn_my_music_clicked(self):
        my_music = self.app.conn.execute_get("""SELECT track_name FROM my_music WHERE user_id=(%s)""",(self.app.user_id,))
        # self.my_music_dict = {}
        # for item in my_music:
        #     self.my_music_dict.update({item[2]:{'track_id':item[0],'user_id':item[1],'track_path':item[3]}})
        # print(self.my_music_dict)
        #print(my_music)
        for item in my_music:
            if not str(item[0]) in self.app.my_music:
                self.app.my_music.append(str(item[0]))
        #print(self.app.my_music)
        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.my_music)

    def btn_my_sharing_clicked(self):
        my_sharing = self.app.conn.execute_get("""SELECT track_name FROM my_sharing WHERE user_id=(SELECT id FROM userdata WHERE nick=(%s))""",(self.app.nick,))
        print(my_sharing)
        for item in my_sharing:
            if not str(item[0]) in self.app.my_sharing:
                self.app.my_sharing.append(str(item[0]))

        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.my_sharing)

    def btn_sharing_me_clicked(self):
        sharing_me = self.app.conn.execute_get("""SELECT track_name FROM my_sharing WHERE tenant=(%s)""",(self.app.nick,))
        print(sharing_me)
        for item in sharing_me:
            if not str(item[0]) in self.app.sharing_me:
                self.app.sharing_me.append(str(item[0]))
        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.sharing_me)

    def favourite_clicked(self):
        favourite = self.app.conn.execute_get("SELECT track_name FROM favourite WHERE user_id=(%s)",(self.app.user_id,))
        print(favourite)
        for item in favourite:
            if not str(item[0]) in self.app.favourite:
                self.app.favourite.append(str(item[0]))
        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.favourite)

    def btn_clicked(self):
        print("Button Clicked")

    def btn_upload_clicked(self):
        Upload_Muisc(self.window,self.app)

class Play_menu():
    def __init__(self,frame, canvas, app_interface=None):
        self.app = app_interface
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
                               command=self.btn_favourite_clicked,
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

    def btn_favourite_clicked(self):
        pass

    def btn_share_clicked(self):
        self.top = Toplevel( takefocus=True)
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

        self.entry_add_playlist = Entry_Box(self.top, self.background_canvas, 61, 122, 355, 47, "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/Resore_Mail.png",
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
                                                                      text="User",
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


    def __init__(self, frame, canvas, app_interface=None):
        #self.content_menu = content_menu
        self.app = app_interface
        self.window = frame
        self.canvas = canvas


        self.entry_search = Entry_Box(self.window, self.canvas, 141, 31, 758, 30,
                                      "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/Wyszukiwarka.png",
                                      90, "#C4C4C4")
        self.entry_search.background_canvas_image()
        self.entry_search.Place()
        self.entry_search.bind("<Return>", self.entry_search_focus)

        self.img_setting = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/setting_icon.png")
        self.but_setting = Button(self.window,
                                  image=self.img_setting,
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  activebackground=self.canvas['bg'],
                                  bg=self.canvas['bg'],
                                  command=self.btn_setting_clicked,
                                  relief='flat')
        # self.but_setting_window = self.canvas.create_window(1080, 15, window=self.but_setting, anchor='nw')
        self.but_setting_window = self.canvas.create_window(1080, 15, anchor='nw', window=self.but_setting)

    def btn_setting_clicked(self):
        # app.content.__del__()
        # self.__del__()
        # app.content.content_search.__del__()
        # app.content.content_play.__del__()
        self.app.content.__del__()
        self.app.setting.__init__(self.app.contentframe, self.app.contentframe_canvas, self.app)

    def __del__(self):

        # self.canvas.delete("all")
        # self.entry_search.Destroy()
        pass

    def entry_search_focus(self, event):
        keyword = str(self.entry_search.get())
        keyword ='%' + keyword + '%'
        findall_track = self.app.conn.execute_get("""SELECT track_name FROM my_music WHERE user_id=(%s) and track_name ILIKE (%s)""",(self.app.user_id, keyword))
        findall_track.extend(self.app.conn.execute_get("""SELECT track_name FROM my_sharing WHERE tenant=(%s) and track_name ILIKE (%s)""", (self.app.nick, keyword)))

        self.app.findall_track.clear()
        for item in findall_track:
            self.app.findall_track.append(str(item[0]))
        self.app.content.content_play.canvas.delete('all')
        self.app.content.content_play.last_postion = 0
        self.app.content.content_play.render_button(self.app.findall_track)



class Content_play():
    def __init__(self,frame, canvas, app_interface=None, content_menu=None):
        self.app = app_interface
        self.content_menu = content_menu
        self.window = frame
        self.canvas = canvas

        self.last_postion = 0
        self.button_identities = []
        self.play_label_press = False

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
        # self.vertibar.place(x=1157-16,y=75)
        # self.vertibar.grid(row=0, column=0, sticky='ns')
        self.vertibar.config(command=self.canvas.yview)
        self.canvas.config(
            yscrollcommand=self.vertibar.set
        )

        self.img_track_pause = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/pause_label.png")
        self.img_track_play = PhotoImage(
            file=f"/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/play_label.png")
        self.btn_track_play = Button(self.window,
                                     text="Chłopcy z Placu Broni - Kocham wolność - YouTube.mp3",
                                     compound='left',
                                     image=self.img_track_play,
                                     activebackground="green",
                                     bg=self.canvas['bg'],
                                     fg='white',
                                     highlightbackground='black',
                                     bd=0,
                                     command=self.thread,
                                     anchor="w",
                                     relief="groove")

        self.btn_track_play_window = self.canvas.create_window(0, 0, window=self.btn_track_play, anchor='nw',
                                                               width=1157 - int(self.vertibar['width']), height=38)

        self.podstwowy = Button(self.window, image=self.img_track_pause, command = self.btn_podstawowy_clicked)
        self.canvas.create_window(40,400, anchor='nw', window= self.podstwowy)

    def play_local(self):
        self.play_local_pid = os.system("python3 /home/mateusz/PycharmProjects/TkinterProj/inz/app/client2.py")
        #exec(open('client2.py').read())

    def thread(self):
        self.btn_track_play.configure(image= self.img_track_pause)
        
        self.tt =Thread(target=self.play).start()
        #time.sleep(0.5)
        time.sleep(1)
        self.mm = Thread(target=self.play_local).start()
    def play(self):

        self.conn = Connection(host='192.168.1.4')
        time.sleep(0.01)
        print(self.conn.ssh_run_remote_command(f'python3 ~/app/server2.py {self.track_play}'))
        print('musztarda')
        self.play_label_press = True

            #self.conn.close()

    # def btn_track_clicked(self):
    #     print("label track clicked")
    #     #print(self.btn_track_play['image'])
    #
    #     if self.play_label_press == False:
    #         x = Thread(target=self.play)
    #         x.start()
    #         #os.system('python3 /home/mateusz/PycharmProjects/TkinterProj/inz/app/paramiko2.py')
    #         print('slon')
    #         #os.system('python3 /home/mateusz/PycharmProjects/TkinterProj/inz/client2.py')
    #         self.play_label_press = True
    #     else:
    #         self.play_label_press = False
    #         #self.conn.close()
    #
    #
    #
    #     if self.btn_track_play['image'] == "pyimage13":
    #         self.btn_track_play.config(image=self.img_track_pause)
    #         # playsound(os.path.join("/home/mateusz/dwhelper/ROCK",str(self.btn_track_play['text'])))
    #         print('piuropusz')
    #     else:
    #         self.btn_track_play.config(image=self.img_track_play)
    #         print('balwan')

    def btn_podstawowy_clicked(self):
        print('Content_paly pressed button')
        self.btn_track_play.configure(image=self.img_track_pause)
        #kill -9 $(ps aux |grep -i client2|gawk '{if ($8 == "Sl+") {print $2}}')
        os.system('pkill -9 client2.py')
        self.conn.exit_stream()
        if self.tt is not None:
            self.tt.join()

##################################################3

    def btn_press(self,n):
        self.bname = self.button_identities[n]
        print(type(self.bname))
        # print('Button', n)
        button_name = self.bname['text']
        #get_play_path = \
        if int(self.app.conn.execute_get("""SELECT count(*) FROM my_music WHERE track_name=(%s) and user_id =(%s)""",(button_name,self.app.user_id))[0][0]) == 1:
            get_play_path = self.app.conn.execute_get("""SELECT track_path FROM my_music WHERE track_name=(%s)""",(button_name,))
        elif int(self.app.conn.execute_get("""SELECT count(*) FROM my_music WHERE track_name=(%s) and user_id = (%s)""",(button_name,self.app.user_id))[0][0]) == 0:
            if int(self.app.conn.execute_get("""SELECT count(*) FROM my_sharing WHERE track_name=(%s) and tenant=(%s)""",(button_name,self.app.nick))[0][0]) == 1:
                get_play_path = self.app.conn.execute_get("""SELECT track_path FROM my_sharing WHERE track_name=(%s) and tenant=(%s)""",(button_name,self.app.nick))
            elif int(self.app.conn.execute_get("""SELECT count(*) FROM my_sharing WHERE track_name=(%s) and tenant=(%s)""",(button_name,self.app.nick))) > 1:
                get_play_path = self.app.conn.execute_get("""SELECT track_path FROM my_sharing WHERE track_name=(%s) and tenant=(%s)""",(button_name, self.app.nick))
                get_play_path = get_play_path[0]
            else:
                print('Cannot find track')
                return None
        get_play_path = get_play_path[0][0]
        print(get_play_path)
        print(button_name)
        self.track_play = get_play_path
        self.thread()
        #TUTAJ NALEZY WYWOLAC PLAY STRAMING funkcje

    def create_button(self,button_name):
        self.temp_button = Button(self.window,
                                  text=button_name,
                                  activebackground="green",
                                  compound='left',
                                  image=self.img_track_play,
                                  anchor = 'w',
                                  bg="black",
                                  fg='white',
                                  highlightbackground='black',
                                  bd=0,
                                  command=partial(self.btn_press, len(self.button_identities)),
                                  relief="groove")

        self.canvas.create_window(0, self.last_postion, width=1157 - int(self.vertibar['width']),
                                  height=38, anchor='nw', window=self.temp_button)
        self.canvas.config(
            scrollregion=(0, 0, int(self.canvas['width']), int(self.canvas['height']) + self.last_postion))
        print(type(self.temp_button))
        self.button_identities.append(self.temp_button)

        self.last_postion = self.last_postion + 38

    def render_button(self,button_list):
        for item in button_list:
            self.create_button(item)

#######################################################################################################

    def __del__(self):
        self.vertibar.destroy()
        self.button_identities.clear()



class Content_menu():
    def __init__(self, frame, canvas, app_interface=None):
        self.app = app_interface
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
            height=910 - 75)

        self.content_play_canvas = Canvas(
            self.content_play_frame,
            bg="#0F0F0E",
            width=1157,
            height=910 - 75,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.content_play_canvas.place(x=0, y=0)
        #on tu tworzy now ainstacje tego za kazdym razem jak wyjdziemy z Setting menu , a my mamy sie wrocic do starej
        #w App interaface trzeb autworzyc tego instancje i tutu wywlaoc
        self.content_search = Content_search(self.content_search_frame, self.content_search_canvas,self.app)
        self.content_play = Content_play(self.content_play_frame, self.content_play_canvas,self.app)

    def __del__(self):
        self.content_play.__del__()
        self.content_search.__del__()
        self.content_search_canvas.destroy()
        self.content_play_canvas.destroy()
        self.content_search_frame.destroy()
        self.content_play_frame.destroy()




class Setting_menu():
    def __init__(self,frame,canvas, app_interface=None):
        self.app = app_interface
        self.window = frame
        self.canvas = canvas
        print(self.app.mail)
        print(self.app.nick)
        #self.canvas = canvas


        # self.canvas = Canvas(
        #     self.window,
        #     bg="#0F0F0E",
        #     height=912,
        #     width=1157,
        #     bd=0,
        #     highlightthickness=0,
        #     relief="ridge")
        # self.canvas.place(x=0, y=0)
        #
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
                                                          text=self.app.nick,
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=24,
                                                              weight='normal',
                                                              slant='italic'),
                                                          fill="white")

        self.your_mail_label = self.canvas.create_text(275, 260,
                                                          anchor='nw',
                                                          text=self.app.mail,
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
                                     state=NORMAL,
                                     font=font.Font(
                                         family='Ubuntu-Regular',
                                         size=10,
                                         weight='normal',
                                         slant='roman'))


        quote = self.app.conn.execute_get("""SELECT description FROM userdata WHERE nick=(%s)""", (self.app.nick, ))
        if quote[0][0]:
            self.text_describeBox.insert(END, quote[0][0])
        self.text_describeBox.config(state=DISABLED)
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

        self.entry_old_password = Entry_Box(self.window, self.canvas, 145, 845, 445, 59, "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/entryBox_setting.png",
                                            5, "#3C3838")
        self.entry_old_password.background_canvas_image()
        self.entry_old_password.Place()

        self.your_change_password_label = self.canvas.create_text(145, 925,
                                                          anchor='nw',
                                                          text="New Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=18,
                                                              weight='normal',
                                                              slant='roman'),
                                                          fill="#3C3838")



        self.entry_new_password = Entry_Box(self.window, self.canvas, 145, 951, 445, 59, "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/entryBox_setting.png",
                                            5, "#3C3838")
        self.entry_new_password.background_canvas_image()
        self.entry_new_password.Place()

        self.your_change_password_label = self.canvas.create_text(145, 1032,
                                                          anchor='nw',
                                                          text="Re-type Password",
                                                          font=font.Font(
                                                              family='Ubuntu-Regular',
                                                              size=18,
                                                              weight='normal',
                                                              slant='roman'),
                                                          fill="#3C3838")

        self.entry_retype_password = Entry_Box(self.window, self.canvas, 145, 1058, 445, 59, "/home/mateusz/PycharmProjects/TkinterProj/inz/App_interface/entryBox_setting.png",
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
                                 command=self.btn_change_password_clicked,
                                 relief='flat')
        self.but_change_window = self.canvas.create_window(514, 1164, window=self.but_change, anchor='nw')

        self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw', text='')

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
        #self.canvas.delete(self.setting_label)

        self.canvas.delete("all")
        #self.canvas.configure(yscrollcommand=-1)

    def btn_change_password_clicked(self):
        new_password = self.entry_new_password.get()
        retype_new_password = self.entry_retype_password.get()
        print('changer_pressed')

        if self.entry_old_password.get() == self.app.conn.execute_get("""SELECT password FROM userdata WHERE nick=(%s)""",(self.app.nick,))[0][0]:
            #check = [True]
            #self.canvas.delete(self.comunicat_label)
            if len(new_password) < 8 and len(retype_new_password) < 8:
                self.canvas.delete(self.comunicat_label)
                self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw', text='Password is too short, Minimum 8 sign',fill="#AB3131")
                #self.comunicat_label.config(text='Password is too short, Minimum 8 sign')
                #check.append(False)
            else:
                if new_password != retype_new_password:
                    self.canvas.delete(self.comunicat_label)
                    self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw', text='Passowrd is not the same',fill="#AB3131")
                    #self.comunicat_label.config(text='Passowrd is not the same')
                else:
                    str2hash = self.app.nick + self.app.mail + new_password
                    hash_string = str(hashlib.md5(str2hash.encode()).hexdigest())

                    self.app.conn.execute_update("""UPDATE userdata SET password=(%s) WHERE nick =(%s)""",(new_password,self.app.nick))
                    self.app.conn.execute_update("""UPDATE userdata SET hash=(%s) WHERE nick =(%s)""",(hash_string, self.app.nick))
                    if str(self.app.conn.execute_get("""SELECT password FROM userdata WHERE nick=(%s)""", (self.app.nick,))[0][0]) == new_password:
                        self.canvas.delete(self.comunicat_label)
                        self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw', text='Password changed succesfully',fill="#159C2B")
                        #self.comunicat_label.config(text='Password changed succesfully')
                    else:
                        self.canvas.delete(self.comunicat_label)
                        self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw', text='Something goes wrong',fill="#AB3131")
                        #self.comunicat_label.config(text='Something goes wrong')
        else:
            self.canvas.delete(self.comunicat_label)
            self.comunicat_label = self.canvas.create_text(145, 803, anchor='nw',text='Wrong Password', fill="#AB3131")

                    
                    #check.append(False)


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
        description = str(self.text_describeBox.get("1.0", END))
        if len(description) > 900:
            description = description[:899]
        sql = """UPDATE userdata SET description=(%s) WHERE nick=(%s)"""
        vars = description,self.app.nick
        self.app.conn.execute_update(sql,vars)
        print(description.index)



    def btn_back_clicked(self):
        self.__del__()
        #Content_menu(self.window,self.canvas,self.app)
        #self.app.content = Content_menu(self.window,self.canvas, self.app)
        #tu wczesniej bylo to wyzej
        self.app.content.__init__(self.window, self.canvas,self.app)

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
    def __init__(self,window,nick,mail):
        self.window = window


        self.nick = nick
        self.mail = mail
        self.conn = Connect('192.168.1.4', 'pi', 'inz178', 'sounder')

        ssh = SSH()
        self.session = ssh.connect()
        self.user_update()
        self.playlist = []
        self.get_playlist()

        self.all_music = []
        self.my_music = []
        self.my_sharing = []
        self.sharing_me = []
        self.favourite = []
        self.findall_track = []

        print(self.playlist)
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

        self.left = Left_menu(self.leftframe, self.leftframe_canvas,self)

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

        self.setting = Setting_menu(self.contentframe, self.contentframe_canvas, self)
        self.setting.__del__()

        self.content = Content_menu(self.contentframe, self.contentframe_canvas, self)


    def user_update(self):
        if self.mail == None:
            self.mail = str(self.conn.execute_get("""SELECT mail FROM userdata WHERE nick=(%s)""", (self.nick,))[0][0])
            self.user_id = int(self.conn.execute_get("""SELECT id FROM userdata WHERE nick=(%s)""", (self.nick,))[0][0])
        if self.nick == None:
            self.nick = str(self.conn.execute_get("""SELECT nick FROM userdata WHERE mail=(%s)""", (self.mail,))[0][0])
            self.user_id = int(self.conn.execute_get("""SELECT id FROM userdata WHERE mail=(%s)""", (self.mail,))[0][0])

    def get_playlist(self):
        playlist_parametr =  self.conn.execute_get("""SELECT playlist_name FROM playlist WHERE user_id=(%s)""",(self.user_id,))
        for item in playlist_parametr:
            self.playlist.append(str(item[0]))





"""
def test_target():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    print('Current TimeStamp is : %d:%d:%d' % (timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))
    time.sleep(2)

mytread = Thread(target=test_target)
mytread.start()
"""
