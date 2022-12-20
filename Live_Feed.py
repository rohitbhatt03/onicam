# Live Feed Module

import ctypes
import cv2
import numpy as np
from datetime import datetime

def live_feed() :
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Video Reading

    win_name = 'Onicam'  # Kernel_Name
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # to get frame height
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # to get frame width
    fps = video.get(cv2.CAP_PROP_FPS)  # to get frames per second
    # width, height should be in same order and type-casted
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # Total Frames
    # print(root)
    # print(type(root))
    open = video.isOpened()  # if Opened Successfully
    if open:
        while video.isOpened():
            it, frame = video.read()  # Reading frames
            if it:  # 'it' is a Boolean type
                cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 450), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (0, 0, 255), 2)
                cv2.rectangle(frame, (45,45),(55,55),(250,0,0),-1)  # rectangle(image_name,((diagonal:1) x1,y1),((diagonal:2) x2,y2), (B,G,R), fill/thickness)
                cv2.putText(frame, '  Live Feed', (50, 55), cv2.FONT_HERSHEY_TRIPLEX,
                            0.6, (255, 255, 255), 2)
                cv2.imshow(win_name, frame)  # Show Frames
                time = datetime.now()
                date = time.date()
                hours = time.hour
                minutes = time.minute
                seconds = time.second
                sc_name = "ScreenCapture@" + str(date) + " " + str(hours) + str(minutes) + str(seconds) + ".png"
                if cv2.waitKey(1) == ord(' '):
                    x = ctypes.windll.user32.MessageBoxW(0, "Screen Captured successfully", "OniCam", 6)
                    # print(type(x))
                    # print(x)
                    if x == 10 or x == 2 :
                        continue
                    cv2.imwrite("My Files/ScreenCaptures/" + sc_name, frame)
                if cv2.waitKey(1) == 27 :
                    break  # Break on pressing ECS key

    video.release()  # release video instance
    cv2.destroyAllWindows()  # destroy all windows

