# the smart recording module

import cv2
import numpy as np
from datetime import datetime

def smart_record():
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Video Reading

    win_name = 'Onicam'  # Kernel_Name
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # to get frame height
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # to get frame width
    fps = video.get(cv2.CAP_PROP_FPS)  # to get frames per second
    time = datetime.now()
    date = time.date()
    print(date)
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    rec_name = "My Files/My Recordings/SmartRec@" + str(date) + " " + str(hours) + str(minutes) + str(seconds) + ".avi"
    # print(rec_name)
    # print(type(rec_name))
    # print(type(rec_name))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # fourcc is a 4 char code used to define extension for videos input.
    output = cv2.VideoWriter(rec_name, fourcc, fps, (int(width), int(height)))
    # width, height should be in same order and type-casted
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # Total Frames

    motion_frame = None
    open = video.isOpened()  # if Opened Successfully
    if open:
        while video.isOpened():
            it, frame = video.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
            if motion_frame is None:
                motion_frame = gray_frame
                continue
            difference = cv2.absdiff(motion_frame, gray_frame)
            _, threshold = cv2.threshold(difference, 75, 255, cv2.THRESH_BINARY)
            # print(type(threshold))
            threshold = cv2.dilate(threshold, None, iterations=2)
            (cntr, _) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            print(cntr)
            # print(cntr.len())
            print(type(cntr))
            for contour in cntr :
                if cv2.contourArea(contour) < 1000 :
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, 'Motion Captured', (50, 55), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255, 0, 0), 2)
            cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 450), cv2.FONT_HERSHEY_TRIPLEX,
                        0.6, (0, 0, 255), 2)
            if not cntr :
                cv2.putText(frame, 'Live Feed', (450, 55), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255, 0, 0), 2)
                # print('not recording')
                # print(cntr)
            else :
                cv2.putText(frame, 'Recording', (450, 55), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (255, 0, 0), 2)
                # print(cntr)
                output.write(frame)  # video writing

            cv2.imshow("Smart Record", frame)
            key = cv2.waitKey(1)
            if key == 27 :
                break
    output.release()  # release output instance
    video.release()  # release video instance
    cv2.destroyAllWindows()  # destroy all windows


