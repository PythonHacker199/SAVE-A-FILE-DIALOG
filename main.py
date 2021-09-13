# HELLO GUYS
# WELCOME TO MY CHANNEL
# SO LET'S START

from tkinter import*
from tkinter import filedialog

window=Tk()
window.title("Text writer")

def saveFile():
    file=filedialog.asksaveasfile(default='.txt',
                                  filetypes=[
                                      ("Text File",".txt"),
                                      ("Python File",".py"),
                                      ("Html File",".html"),
                                  ])
    filetext=str(text.get(1.0,END))
    file.write(filetext)
    file.close()

button=Button(text='Save file as',command=saveFile)
button.pack()
text=Text(window)
text.pack()

window.mainloop()