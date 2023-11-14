import tkinter as tk
import numpy as np

def tinh_dien_tich_hinh_tron():
    ban_kinh = float(entry.get())
    dien_tich = np.pi * ban_kinh**2
    chu_vi = 2 * np.pi * ban_kinh
    result_label.config(text=f"Diện tích hình tròn: {dien_tich}, Chu vi hình tròn: {chu_vi}")

def tinh_dien_tich_hinh_chu_nhat():
    chieu_dai = float(chieu_dai_entry.get())
    chieu_rong = float(chieu_rong_entry.get())
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    result_label.config(text=f"Diện tích hình chữ nhật: {dien_tich}, Chu vi hình chữ nhật: {chu_vi}")

def tinh_dien_tich_tam_giac():
    chieu_cao = float(chieu_cao_entry.get())
    canh_day = float(canh_day_entry.get())
    dien_tich = 0.5 * chieu_cao * canh_day
    result_label.config(text=f"Diện tích tam giác: {dien_tich}")

def tinh_the_tich_hinh_cau():
    ban_kinh_hinh_cau = float(ban_kinh_hinh_cau_entry.get())
    the_tich = (4/3) * np.pi * ban_kinh_hinh_cau**3
    result_label.config(text=f"Thể tích hình cầu: {the_tich}")

root = tk.Tk()
root.title("Tính diện tích và chu vi hình học")
# root.geometry("1000x1000")
# Hình tròn
label1 = tk.Label(root, text="Hình tròn")
label1.pack()

label_ban_kinh = tk.Label(root, text="Bán kính:")
label_ban_kinh.pack()
entry = tk.Entry(root)
entry.pack()

calculate_button1 = tk.Button(root, text="Tính", command=tinh_dien_tich_hinh_tron)
calculate_button1.pack()

# Hình chữ nhật
label2 = tk.Label(root, text="Hình chữ nhật")
label2.pack()

label_chieu_dai = tk.Label(root, text="Chiều dài:")
label_chieu_dai.pack()
chieu_dai_entry = tk.Entry(root)
chieu_dai_entry.pack()

label_chieu_rong = tk.Label(root, text="Chiều rộng:")
label_chieu_rong.pack()
chieu_rong_entry = tk.Entry(root)
chieu_rong_entry.pack()

calculate_button2 = tk.Button(root, text="Tính", command=tinh_dien_tich_hinh_chu_nhat)
calculate_button2.pack()

# Tam giác
label3 = tk.Label(root, text="Tam giác")
label3.pack()

label_chieu_cao = tk.Label(root, text="Chiều cao:")
label_chieu_cao.pack()
chieu_cao_entry = tk.Entry(root)
chieu_cao_entry.pack()

label_canh_day = tk.Label(root, text="Cạnh đáy:")
label_canh_day.pack()
canh_day_entry = tk.Entry(root)
canh_day_entry.pack()

calculate_button3 = tk.Button(root, text="Tính", command=tinh_dien_tich_tam_giac)
calculate_button3.pack()

# Hình cầu
label4 = tk.Label(root, text="Hình cầu")
label4.pack()

label_ban_kinh_hinh_cau = tk.Label(root, text="Bán kính hình cầu:")
label_ban_kinh_hinh_cau.pack()
ban_kinh_hinh_cau_entry = tk.Entry(root)
ban_kinh_hinh_cau_entry.pack()

calculate_button4 = tk.Button(root, text="Tính", command=tinh_the_tich_hinh_cau)
calculate_button4.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()