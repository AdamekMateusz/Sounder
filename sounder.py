#from App_interface.app_interface import *
from main_menu.main import *

#if __name__ == '__sounder__':
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