# usr/bin
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO
from urllib.request import urlopen
import io
import base64
from forms.principal_design import frmPrincipal


def main():
    frm = frmPrincipal()
    frm.show()
    """window = tkinter.Tk()
    window.title('Inicial')
    window.geometry("640x480")
    window.wm_iconbitmap('favicon.ico')
    Label(window, text='Qual filme deseja ?').pack(anchor=NW, padx=20, pady=5)
    Entry(window).pack(anchor=NW, padx=20, fill=X, pady=2)
    Button(window, text='Buscar').pack(side=TOP, fill=X, padx=20, pady=15)
    window.mainloop()"""


if __name__ == '__main__':
    main()


""" get working
url = "http://imgs.xkcd.com/comics/python.png"
img = Image.open(BytesIO(requests.get(url).content))
image = ImageTk.PhotoImage(img)
label = Label(window, image=image)
label.pack(fill=X)"""
