import tkinter
from tkinter import *

class frmPrincipal(object):
    """docstring for frmPrincipal."""


    def __init__(self):
        super(frmPrincipal, self).__init__()
        self.title = 'Inicial'
        self.form = tkinter.Tk()
        self.size = '640x480'
        self.icon = 'favicon.ico'
        self.lblWhichMovie = Label
        self.txtWhichMovie = Entry
        self.btnSearch = Button

        self.form.title(self.title)
        self.form.geometry(self.size)
        self.form.wm_iconbitmap(self.icon)
        self.lblWhichMovie = Label(self.form, text='Qual filme deseja ?')
        self.lblWhichMovie.pack(anchor=NW, padx=20, pady=5)
        self.txtWhichMovie = Entry(self.form)
        self.txtWhichMovie.pack(anchor=NW, padx=20, fill=X, pady=2)
        self.btnSearch = Button(self.form, text='Busca')
        self.btnSearch.pack(side=TOP, fill=X, padx=20, pady=15)

    def show(self):
        self.form.mainloop()
