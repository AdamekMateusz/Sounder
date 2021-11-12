import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')

plik = None

def select_files():
    filetypes = (
        ('mp3', '*.mp3'),
        ('wav', '*.wav')
    )

    filenames = fd.askopenfilenames(
        title='Open audio files',
        initialdir='~/dwhelper',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected Files',
    #     message=filenames
    #
    global plik
    plik = filenames
    return filenames


# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)

open_button.pack(expand=True)


root.mainloop()

print(plik)