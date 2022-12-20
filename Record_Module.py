# it's a recording module.

import cv2
import numpy as np
from datetime import datetime

def record():
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Video Reading

    win_name = 'Onicam'  # Kernel_Name
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # to get frame height
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # to get frame width
    fps = video.get(cv2.CAP_PROP_FPS)  # to get frames per second
    time = datetime.now()
    date = time.date()
    # print(date)
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    rec_name = "My Files/My Recordings/MyRecording@" + str(date) + " " + str(hours) + str(minutes) + str(seconds) + ".avi"
    # print(rec_name)
    # print(type(rec_name))
    # rec_name[23]='@'
    # print(type(rec_name))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # fourcc is a 4 char code used to define extension for videos input.
    output = cv2.VideoWriter(rec_name, fourcc, fps, (int(width), int(height)))
    # width, height should be in same order and type-casted
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # Total Frames
    # move = height - 50
    open = video.isOpened()  # if Opened Successfully
    if open:
        while video.isOpened():
            it, frame = video.read()  # Reading frames
            if it:  # 'it' is a Boolean type
                cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 450), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (0, 0, 255), 2)
                cv2.circle(frame, (45,50), 8, (0, 0, 255), -3)
                cv2.putText(frame, ' Recording', (50, 55), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255, 255, 255), 2)
                cv2.imshow(win_name, frame)  # Show Frames
                output.write(frame)  # video writing

                if cv2.waitKey(3) == 27:
                    break  # Break on pressing ECS key

    output.release()  # release output instance
    video.release()  # release video instance
    cv2.destroyAllWindows()  # destroy all windows
