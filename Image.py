# importing the libraries
import cv2
import numpy as np

def Open_Img(file_name):
    image = cv2.imread(file_name)  # Reading Image

    win_name = 'my application'  # Kernel_Name

    cv2.imshow(win_name, image)  # Show_Image

    cv2.waitKey(0)  # For Terminating the Kernel

    cv2.destroyAllWindows()  # Destroy all windows
