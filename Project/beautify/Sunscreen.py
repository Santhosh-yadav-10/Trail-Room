from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def ContrastEnhancement(contrast,filepath):
    image = Image.open(filepath)
    enh_con = ImageEnhance.Contrast(image)
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()

def Filter(image,filepath):
    image =cv2.imread(filepath)
    Remove=cv2.bilateralFilter(image,0,0,10)
    cv2.imshow('filter',Remove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def def_apply(filepath):
    contrast=1.3
    ContrastEnhancement(contrast,filepath)
    image =cv2.imread(filepath)
    Filter(image,filepath)

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")

        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.configure(text = self.filename)
        filepath  = self.filename
        def_apply(filepath)

def applySunscreen():
    print("Sunscreen")
    root = Root()
    root.geometry("300x200")
    root.mainloop()