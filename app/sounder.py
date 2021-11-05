from tkinter import *
from login_window import *
from app import *

if __name__ == "__main__":
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
    lm = Login_menu(window, canvas)
    window.resizable(False, False)
    window.mainloop()
    print("witam")
    if lm.is_clicked_properly():
        root = Tk()
        root.geometry("1440x1024")
        root.configure(bg="#ffffff")
        root.resizable(False, False)
        app = App_Interface(root)

        root.mainloop()