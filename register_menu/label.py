from tkinter import *
from tkinter import font as tkfont
from PIL import Image, ImageTk

def clicker(event):
    print('clicker')

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x400")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "green",
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

"""
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 489, y = 330,
    width = 260,
    height = 58)
"""


# canvas_button= Canvas(
#     window,
#     bg = "#141213",
#     height = 58,
#     width = 260,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge")
# canvas_button.place(x = 489, y =330)

def RBGAImage(path):
    return Image.open(path).convert("RGBA")

canvas_button_img = RBGAImage("Button.png")

CC_canvas_button_img = ImageTk.PhotoImage(canvas_button_img)

    
#141213

bb =Button(text ='slon',borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bb_window = canvas.create_window(100,100,anchor='nw',window=bb)

b0 = Button(
    image = CC_canvas_button_img,
    # activebackground = "#141213",
    #bg = "#141213",
    #bg='systemTransparent',
    border = 0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0_window = canvas.create_window(489,330,anchor='nw',window=b0)

#Canvas Button
"""
reg_button = canvas.create_image(489,330, anchor='nw', image=CC_canvas_button_img, tags="reg_button")
canvas.tag_bind("reg_button","<Button-1>",clicker)
"""





# b0 = Button(
#     image = canvas_button_img,
#     activebackground = canvas_button['background'],
#     bg = canvas_button['background'],
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = btn_clicked,
#     relief = "flat")

# b0.place(
#     x = 489, y = 330,
#     width = 260,
#     height = 58)


entry0_img = PhotoImage(file = f"TextBox.png")
"""
entry0_bg = canvas.create_image(
    621.5, 283.5,
    image = entry0_img)
"""

entry0 = Entry(
    bd = 0,
    bg = "white",
    highlightthickness = 0)
    
entry0.image = entry0_img

entry0.place(
    x = 494, y = 260,
    width = 255,
    height = 45)

entry1_img = PhotoImage(file = f"TextBox.png")
entry1_bg = canvas.create_image(
    621.5, 213.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0)

entry1.place(
    x = 497.75, y = 192.5,
    width = 247.5,
    height = 43.25)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 755, y = 268,
    width = 31,
    height = 31)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    621.5, 143.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0)

entry2.place(
    x = 494, y = 120,
    width = 255,
    height = 45)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    621.5, 73.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#3c3838",
    highlightthickness = 0)

entry3.place(
    x = 494, y = 50,
    width = 255,
    height = 45)

label1 = Label(window,text="Nicknamessss", font=('Helvetica',12), fg='#3c3838')
label1.place(x = 494, y = 28)
"""
canvas.create_text(
    533, 43.5,
    text = "Nickname",
    fill = "#3c3838",
    font = ("Ubuntu-Regular", int(12.0)),
    justify=)
"""
canvas.create_text(
    508.5, 113.5,
    text = "Mail",
    fill = "#3c3838",
    font = ("Ubuntu-Regular", int(12.0)))

canvas.create_text(
    530.5, 183.5,
    text = "Password",
    fill = "#3c3838",
    font = ("Ubuntu-Regular", int(12.0)))

canvas.create_text(
    544, 253.5,
    text = "Re-Password",
    fill = "#3c3838",
    font = ("Ubuntu-Regular", int(12.0)))

window.resizable(False, False)
window.mainloop()
