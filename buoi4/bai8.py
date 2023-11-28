import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk

selected_image1 = None
selected_image2 = None

def select_image():
    global selected_image1
    global selected_image2
    file_path = filedialog.askopenfilename()
    if file_path:
        img1 = cv2.imread(file_path)
        selected_image1 = img1
        img2 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        selected_image2 = img2

        image = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

def zoom_image(x, y):
    if selected_image1 is not None:
        zoomed = cv2.resize(selected_image1, (x, y))
        Titles = ["Original", "Zoomed"]
        images = [selected_image1, zoomed]
        plt.figure(1)
        for i in range(2):
            plt.subplot(2, 1, i + 1)
            plt.title(Titles[i])
            plt.imshow(images[i])
        plt.show()

def rotate_image(degrees):
    if selected_image1 is not None:
        img1 = selected_image1
        height, width = img1.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degrees, 1)
        rotated = cv2.warpAffine(img1, rotation_matrix, (width, height))

        Titles = ["Original", "Rotated"]
        images = [selected_image1, rotated]
        plt.figure(2)
        for i in range(2):
            plt.subplot(2, 1, i + 1)
            plt.title(Titles[i])
            plt.imshow(images[i])
        plt.show()

def normalize_image():
    if selected_image1 is not None and selected_image2 is not None:
        img1 = selected_image1
        normalized_img1 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX)
        img2 = selected_image2
        normalized_img2 = cv2.normalize(img2, None, 0, 255, cv2.NORM_MINMAX)

        # Convert images for display in Tkinter
        image1 = cv2.cvtColor(normalized_img1, cv2.COLOR_BGR2RGB)
        image1 = Image.fromarray(image1)
        image1 = ImageTk.PhotoImage(image1)
        image2 = cv2.cvtColor(normalized_img2, cv2.COLOR_BGR2RGB)
        image2 = Image.fromarray(image2)
        image2 = ImageTk.PhotoImage(image2)

        original_label1 = tk.Label(normalize_tab, image=image_label)
        original_label1.image = image_label
        original_label2 = tk.Label(normalize_tab, image=image_label)
        original_label2.image = image_label
        normalized_label1 = tk.Label(normalize_tab, image=image1)
        normalized_label1.image = image1
        normalized_label2 = tk.Label(normalize_tab, image=image2)
        normalized_label2.image = image2

        original_label1.grid(row=1, column=1)
        original_label2.grid(row=1, column=2)
        normalized_label1.grid(row=2, column=1)
        normalized_label2.grid(row=2, column=2)

def edge_detection(ed1, ed2):
    if selected_image1 is not None:
        img = selected_image1
        edges = cv2.Canny(img, ed1, ed2)
        plt.figure(3)
        plt.imshow(edges, cmap='gray')
        plt.title("Edge Detection")
        plt.show()

def get_values1():
    x = int(x_entry.get())
    y = int(y_entry.get())
    zoom_image(x, y)

def get_values2():
    ed1 = int(ed1_entry.get())
    ed2 = int(ed2_entry.get())
    edge_detection(ed1, ed2)

def rotate_from_keyboard():
    degrees = int(rotation_entry.get())
    rotate_image(degrees)

root = tk.Tk()
root.title("ỨNG DỤNG CHỈNH SỬA ẢNH")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

zoom_tab = tk.Frame(notebook)
rotate_tab = tk.Frame(notebook)
normalize_tab = tk.Frame(notebook)
edge_tab = tk.Frame(notebook)

notebook.add(zoom_tab, text="Zoom")
notebook.add(rotate_tab, text="Xoay")
notebook.add(normalize_tab, text="Làm nét")
notebook.add(edge_tab, text="Tách biên")

frame_zoom = tk.Frame(zoom_tab)
frame_zoom.pack()

frame_rotate = tk.Frame(rotate_tab)
frame_rotate.pack()

frame_normalize = tk.Frame(normalize_tab)
frame_normalize.pack()

frame_edge = tk.Frame(edge_tab)
frame_edge.pack()

x_label = tk.Label(frame_zoom, text="Nhập x:")
x_label.pack()
x_entry = tk.Entry(frame_zoom)
x_entry.pack()

y_label = tk.Label(frame_zoom, text="Nhập y:")
y_label.pack()
y_entry = tk.Entry(frame_zoom)
y_entry.pack()

ed1_label = tk.Label(frame_edge, text="Nhập ed1:")
ed1_label.pack()
ed1_entry = tk.Entry(frame_edge)
ed1_entry.pack()

ed2_label = tk.Label(frame_edge, text="Nhập ed2:")
ed2_label.pack()
ed2_entry = tk.Entry(frame_edge)
ed2_entry.pack()

rotation_label = tk.Label(frame_rotate, text="Nhập góc xoay:")
rotation_label.pack()
rotation_entry = tk.Entry(frame_rotate)
rotation_entry.pack()

select_button = tk.Button(frame_zoom, text="chọn ảnh", command=select_image)
select_button.pack()

image_label = tk.Label(zoom_tab)
image_label.pack()

zoom_button = tk.Button(frame_zoom, text="Zoom ảnh", command=get_values1)
zoom_button.pack()

rotate_button = tk.Button(frame_rotate, text="Xoay ảnh", command=rotate_from_keyboard)
rotate_button.pack()

normalize_button = tk.Button(frame_normalize, text="Làm nét ảnh", command=normalize_image)
normalize_button.pack()

edge_button = tk.Button(frame_edge, text="Tách biên ảnh", command=get_values2)
edge_button.pack()

root.mainloop()
