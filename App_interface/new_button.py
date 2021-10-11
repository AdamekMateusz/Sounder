from tkinter import *

root = Tk()
root.geometry("400x400")
Photoshop = Button(root, text = 'Photoshop',
                      fg = '#37d3ff',
                      bg = '#001d26',
                      bd =  1,
                      highlightthickness=7,
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff",
                      borderwidth=1)
Photoshop.place(x=100,y=100,width=200,height=100)

root.mainloop()
