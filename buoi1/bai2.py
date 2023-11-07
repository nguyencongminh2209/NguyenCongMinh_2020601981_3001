import sympy as sym
import tkinter as tk
from tkinter import ttk

def xoa_du_lieu():
    # Xóa dữ liệu nhập vào các trường văn bản
    bieu_thuc_tich_phan_entry.delete(0, 'end')
    bien_tich_phan_entry.delete(0, 'end')
    gioi_han_start_entry.delete(0, 'end')
    gioi_han_end_entry.delete(0, 'end')
    bieu_thuc_gioi_han_entry.delete(0, 'end')
    bien_gioi_han_entry.delete(0, 'end')
    diem_gioi_han_entry.delete(0, 'end')
    bieu_thuc_dao_ham_entry.delete(0, 'end')
    bien_dao_ham_entry.delete(0, 'end')
    bieu_thuc_khai_trien_entry.delete(0, 'end')
    bieu_thuc_rut_gon_entry.delete(0, 'end')

def tinh_tich_phan():
    bieu_thuc = bieu_thuc_tich_phan_entry.get()
    bien = bien_tich_phan_entry.get()
    gioi_han_start = float(gioi_han_start_entry.get())
    gioi_han_end = float(gioi_han_end_entry.get())

    x = sym.symbols(bien)
    try:
        ket_qua_tich_phan = sym.integrate(bieu_thuc, (x, gioi_han_start, gioi_han_end))
        ket_qua_tich_phan_label.config(text="Kết quả tích phân: " + str(ket_qua_tich_phan))
    except Exception as e:
        ket_qua_tich_phan_label.config(text="Lỗi: " + str(e))

def tinh_gioi_han():
    bieu_thuc = bieu_thuc_gioi_han_entry.get()
    bien = bien_gioi_han_entry.get()
    diem_gioi_han = float(diem_gioi_han_entry.get())

    x = sym.symbols(bien)
    try:
        gioi_han = sym.limit(bieu_thuc, x, diem_gioi_han)
        gioi_han_label.config(text="Giới hạn tại điểm {}: {}".format(diem_gioi_han, gioi_han))
    except Exception as e:
        gioi_han_label.config(text="Lỗi: " + str(e))

def tinh_dao_ham():
    bieu_thuc = bieu_thuc_dao_ham_entry.get()
    bien = bien_dao_ham_entry.get()

    x = sym.symbols(bien)
    try:
        dao_ham = sym.diff(bieu_thuc, x)
        dao_ham_label.config(text="Đạo hàm: " + str(dao_ham))
    except Exception as e:
        dao_ham_label.config(text="Lỗi: " + str(e))

def khai_trienn():
    bieu_thuc = bieu_thuc_khai_trien_entry.get()
    try:
        bieu_thuc_khai_trien = sym.expand(bieu_thuc)
        bieu_thuc_khai_trien_label.config(text="Biểu thức khai triển: " + str(bieu_thuc_khai_trien))
    except Exception as e:
        bieu_thuc_khai_trien_label.config(text="Lỗi: " + str(e))

def rut_gon_bieu_thuc():
    bieu_thuc = bieu_thuc_rut_gon_entry.get()
    try:
        bieu_thuc_rut_gon = sym.simplify(bieu_thuc)
        bieu_thuc_rut_gon_label.config(text="Biểu thức rút gọn: " + str(bieu_thuc_rut_gon))
    except Exception as e:
        bieu_thuc_rut_gon_label.config(text="Lỗi: " + str(e))
# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Tính Tích Phân, Giới Hạn, Đạo Hàm, Khai Triển và Rút Gọn Biểu Thức")

# Phần tính tích phân
frame_tich_phan = ttk.Frame(root)
frame_tich_phan.grid(row=0, column=0, padx=10, pady=10, sticky="w")

bieu_thuc_tich_phan_label = ttk.Label(frame_tich_phan, text="Biểu thức:")
bieu_thuc_tich_phan_label.grid(row=0, column=0)
bieu_thuc_tich_phan_entry = ttk.Entry(frame_tich_phan)
bieu_thuc_tich_phan_entry.grid(row=0, column=1)

bien_tich_phan_label = ttk.Label(frame_tich_phan, text="Biến:")
bien_tich_phan_label.grid(row=1, column=0)
bien_tich_phan_entry = ttk.Entry(frame_tich_phan)
bien_tich_phan_entry.grid(row=1, column=1)

gioi_han_start_label = ttk.Label(frame_tich_phan, text="Giới hạn bắt đầu:")
gioi_han_start_label.grid(row=2, column=0)
gioi_han_start_entry = ttk.Entry(frame_tich_phan)
gioi_han_start_entry.grid(row=2, column=1)

gioi_han_end_label = ttk.Label(frame_tich_phan, text="Giới hạn kết thúc:")
gioi_han_end_label.grid(row=3, column=0)
gioi_han_end_entry = ttk.Entry(frame_tich_phan)
gioi_han_end_entry.grid(row=3, column=1)

tinh_tich_phan_button = ttk.Button(frame_tich_phan, text="Tính Tích Phân", command=tinh_tich_phan)
tinh_tich_phan_button.grid(row=4, columnspan=2)

ket_qua_tich_phan_label = ttk.Label(frame_tich_phan, text="")
ket_qua_tich_phan_label.grid(row=5, columnspan=2)

# Phần tính giới hạn
frame_gioi_han = ttk.Frame(root)
frame_gioi_han.grid(row=0, column=1, padx=10, pady=10, sticky="e")

bieu_thuc_gioi_han_label = ttk.Label(frame_gioi_han, text="Biểu thức:")
bieu_thuc_gioi_han_label.grid(row=0, column=0)
bieu_thuc_gioi_han_entry = ttk.Entry(frame_gioi_han)
bieu_thuc_gioi_han_entry.grid(row=0, column=1)

bien_gioi_han_label = ttk.Label(frame_gioi_han, text="Biến:")
bien_gioi_han_label.grid(row=1, column=0)
bien_gioi_han_entry = ttk.Entry(frame_gioi_han)
bien_gioi_han_entry.grid(row=1, column=1)

diem_gioi_han_label = ttk.Label(frame_gioi_han, text="Điểm giới hạn:")
diem_gioi_han_label.grid(row=2, column=0)
diem_gioi_han_entry = ttk.Entry(frame_gioi_han)
diem_gioi_han_entry.grid(row=2, column=1)

tinh_gioi_han_button = ttk.Button(frame_gioi_han, text="Tính Giới Hạn", command=tinh_gioi_han)
tinh_gioi_han_button.grid(row=3, columnspan=2)

gioi_han_label = ttk.Label(frame_gioi_han, text="")
gioi_han_label.grid(row=4, columnspan=2)

# Phần tính đạo hàm
frame_dao_ham = ttk.Frame(root)
frame_dao_ham.grid(row=0, column=2, padx=10, pady=10, sticky="e")

bieu_thuc_dao_ham_label = ttk.Label(frame_dao_ham, text="Biểu thức:")
bieu_thuc_dao_ham_label.grid(row=0, column=0)
bieu_thuc_dao_ham_entry = ttk.Entry(frame_dao_ham)
bieu_thuc_dao_ham_entry.grid(row=0, column=1)

bien_dao_ham_label = ttk.Label(frame_dao_ham, text="Biến:")
bien_dao_ham_label.grid(row=1, column=0)
bien_dao_ham_entry = ttk.Entry(frame_dao_ham)
bien_dao_ham_entry.grid(row=1, column=1)

tinh_dao_ham_button = ttk.Button(frame_dao_ham, text="Tính Đạo Hàm", command=tinh_dao_ham)
tinh_dao_ham_button.grid(row=2, columnspan=2)

dao_ham_label = ttk.Label(frame_dao_ham, text="")
dao_ham_label.grid(row=3, columnspan=2)

# Phần khai triển biểu thức
frame_khai_trien = ttk.Frame(root)
frame_khai_trien.grid(row=1, column=0, padx=10, pady=10, sticky="w")
bieu_thuc_khai_trien_label = ttk.Label(frame_khai_trien, text="Biểu thức cần khai triển:")
bieu_thuc_khai_trien_label.grid(row=0, column=0)
bieu_thuc_khai_trien_entry = ttk.Entry(frame_khai_trien)
bieu_thuc_khai_trien_entry.grid(row=0, column=1)

tinh_khai_trien_button = ttk.Button(frame_khai_trien, text="Khai Triển", command=khai_trienn)
tinh_khai_trien_button.grid(row=1, columnspan=2)

bieu_thuc_khai_trien_label = ttk.Label(frame_khai_trien, text="")
bieu_thuc_khai_trien_label.grid(row=2, columnspan=2)

# Phần rút gọn biểu thức
frame_rut_gon = ttk.Frame(root)
frame_rut_gon.grid(row=1, column=1, padx=10, pady=10, sticky="e")

bieu_thuc_rut_gon_label = ttk.Label(frame_rut_gon, text="Biểu thức cần rút gọn:")
bieu_thuc_rut_gon_label.grid(row=0, column=0)
bieu_thuc_rut_gon_entry = ttk.Entry(frame_rut_gon)
bieu_thuc_rut_gon_entry.grid(row=0, column=1)

tinh_rut_gon_button = ttk.Button(frame_rut_gon, text="Rút Gọn", command=rut_gon_bieu_thuc)
tinh_rut_gon_button.grid(row=1, columnspan=2)

bieu_thuc_rut_gon_label = ttk.Label(frame_rut_gon, text="")
bieu_thuc_rut_gon_label.grid(row=2, columnspan=2)

# Thêm nút xóa dữ liệu
xoa_du_lieu_button = ttk.Button(root, text="Xóa Dữ Liệu", command=xoa_du_lieu)
xoa_du_lieu_button.grid(row=2, column=3)
root.mainloop()