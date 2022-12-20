import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from main import *



class App:

    def __init__(self, window, window_title, image_path="onicam.png"):
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        # self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Button that lets the user blur the image
        self.btn_Enter = tkinter.Button(window, text="Enter", width=50, command=self.call)
        self.btn_Quit = tkinter.Button(window, text='Quit', width=50, command=self.window.destroy)
        self.btn_Display = tkinter.Button(window, text='Display', width =0, command=self.clive_feed())
        self.btn_Enter.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_Quit.pack(anchor=tkinter.CENTER, expand=True)
        self.window.mainloop()

    # Create a window and pass it to the Application object
    def clive_feed(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def call(self):
        self.window.destroy()
        app = Fullscreen_APP()



App(tkinter.Tk(), "OniCam")
