import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askinteger


start_x, start_y, end_x, end_y = -1, -1, -1, -1
is_drawing = False
selected_region = None
smoothing_value = 5  

def select_region(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, is_drawing, img, selected_region

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            end_x, end_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        end_x, end_y = x, y

        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

  
        selected_region = img[start_y:end_y, start_x:end_x]

def open_image():
    global img, selected_region
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tif")])
    if file_path:
        img = cv2.imread(file_path)
        if img is not None:
            cv2.namedWindow('Portrait')
            cv2.setMouseCallback('Portrait', select_region)
            selected_region = None
            cv2.imshow('Portrait', img)

def on_ok_button_click():
    global img, selected_region, smoothing_value
    if selected_region is not None:
      
        kernel = np.ones((smoothing_value, smoothing_value), np.float32) / (smoothing_value ** 2)
        smoothed_region = cv2.filter2D(selected_region, -1, kernel)
        img[start_y:end_y, start_x:end_x] = smoothed_region

      
        cv2.imshow('Portrait', img)

def set_smoothing_value():
    global smoothing_value
    new_value = askinteger("Độ mịn", "Nhập giá trị(integer):", parent=root)
    if new_value is not None:
        smoothing_value = new_value


root = tk.Tk()
root.title("Image Smoothing")


open_button = tk.Button(root, text="Mở ảnh", command=open_image)
open_button.pack()


ok_button = tk.Button(root, text="Làm mịn", command=on_ok_button_click)
ok_button.pack()

set_smoothing_button = tk.Button(root, text="Độ mịn", command=set_smoothing_value)
set_smoothing_button.pack()

root.mainloop()
