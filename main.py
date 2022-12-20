# OniCam
import tkinter as tk
from Live_Feed import live_feed
from Smart_Record import smart_record
from tkinter import *
import numpy as np
import cv2
from Record_Module import record
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from video import Play_Vid
from Image import Open_Img




class Fullscreen_APP:
    def __init__(self):
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.window.title('OniCam')
        self.Progress_Bar = Progressbar(self.window, orient=HORIZONTAL, length=250, mode='determinate')
        lable = tk.Label(self.window, text='''hey! there User,\n
        I'm OniCam a smart-Cam that works for various purposes.\n
        well I'm still learning and here's some stuff that I can do.\n''',font=("Arial", 15)).pack()
        self.btn_Live = tk.Button(self.window, text="Live Monitoring", width=50, command=self.LiMo)
        self.btn_Record = tk.Button(self.window, text="Record", width=50, command=self.rec)
        self.btn_SmartRec = tk.Button(self.window, text="Smart Record", width=50, command=self.Smrt_rec)
        self.btn_Quit = tk.Button(self.window, text="Quit", width=50, command=self.window.destroy)
        self.btn_Myfile = tk.Button(self.window, text="My Files", width=50, command=self.load_file)
        self.btn_Live.pack(anchor=tk.CENTER, expand=True)
        self.btn_Live.place(x=200, y=220)
        self.btn_Record.pack(anchor=tk.CENTER, expand=True)
        self.btn_Record.place(x=1000, y=220)
        self.btn_SmartRec.pack(anchor=tk.CENTER, expand=True)
        self.btn_SmartRec.place(x=200, y=520)
        self.btn_Quit.pack(anchor=tk.CENTER, expand=True)
        self.btn_Quit.place(x=595, y=350)
        self.btn_Myfile.pack(anchor=tk.CENTER, expand=True)
        self.btn_Myfile.place(x=1000, y=520)
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))

        self.window.mainloop()

    def rec(self):
        self.Progress_Bar.pack(anchor=tk.CENTER, expand=True)
        self.Progress_Bar.place(x=630, y=680)
        self.Slide()
        record()
        self.Progress_Bar.destroy()
        self.window.destroy()
        Fullscreen_APP()

    def Smrt_rec(self):
        self.Progress_Bar.pack(anchor=tk.CENTER, expand=True)
        self.Progress_Bar.place(x=630, y=680)
        self.Slide()
        smart_record()
        self.Progress_Bar.destroy()
        self.window.destroy()
        Fullscreen_APP()

    def LiMo(self):
        self.Progress_Bar.pack(anchor=tk.CENTER, expand=True)
        self.Progress_Bar.place(x=630, y=680)
        self.Slide()
        live_feed()
        self.Progress_Bar.destroy()
        self.window.destroy()
        Fullscreen_APP()

    def Slide(self):
        import time
        self.Progress_Bar['value'] = 20
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 50
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 80
        self.window.update_idletasks()
        time.sleep(1)
        self.Progress_Bar['value'] = 100

    def load_file(self):
        file_name = askopenfilename(filetypes=(("Picture files", "*.png;*.bmp"),
                                               ("All files", "*.*")))
        check = ('.png' in file_name)
        if check:
            Open_Img(file_name)
        else :
            Play_Vid(file_name)
        print(file_name)
        self.window.destroy()
        Fullscreen_APP()

# if __name__ == '__main__':
#     app = Fullscreen_APP()
