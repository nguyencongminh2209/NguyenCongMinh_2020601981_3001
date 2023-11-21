import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AppXuLyTinHieu:
    def __init__(self, master):
        self.master = master
        master.title("Ứng Dụng Xử Lý Tín Hiệu Số")

        self.tan_so_lay_mau = 1000  # Hz
        self.tan_so_tin_hieu = 5  # Hz
        self.amplitude = 1
        self.thoi_gian = 2  # giây

        self.nut_tao_tin_hieu = tk.Button(master, text="Tạo Tín Hiệu", command=self.tao_tin_hieu)
        self.nut_tao_tin_hieu.pack()

        self.nut_loc_tin_hieu = tk.Button(master, text="Áp Dụng Bộ Lọc Thấp", command=self.ap_dung_bo_loc)
        self.nut_loc_tin_hieu.pack()

        self.nut_ve_do_thi = tk.Button(master, text="Vẽ Đồ Thị", command=self.ve_do_thi_va_pho_tan)
        self.nut_ve_do_thi.pack()

    def tao_tin_hieu(self):
        t, tin_hieu = self._tao_tin_hieu()
        self.t = t
        self.tin_hieu = tin_hieu
        print("Tín hiệu đã được tạo.")

    def ap_dung_bo_loc(self):
        if not hasattr(self, 'tin_hieu'):
            print("Tạo tín hiệu trước.")
            return

        tin_hieu_loc = self._ap_dung_bo_loc(self.tin_hieu, tan_so_cat=10, tan_so_lay_mau=self.tan_so_lay_mau)
        self.tin_hieu_loc = tin_hieu_loc
        print("Bộ lọc đã được áp dụng.")

    def ve_do_thi_va_pho_tan(self):
        if not hasattr(self, 'tin_hieu') or not hasattr(self, 'tin_hieu_loc'):
            print("Tạo tín hiệu và áp dụng bộ lọc trước.")
            return

        self._ve_do_thi_va_pho_tan(self.t, self.tin_hieu, "Tín Hiệu Gốc")
        self._ve_do_thi_va_pho_tan(self.t, self.tin_hieu_loc, "Tín Hiệu Đã Lọc")

    def _tao_tin_hieu(self):
        t = np.arange(0, self.thoi_gian, 1/self.tan_so_lay_mau)
        tin_hieu = self.amplitude * np.sin(2 * np.pi * self.tan_so_tin_hieu * t)
        return t, tin_hieu

    def _ap_dung_bo_loc(self, tin_hieu, tan_so_cat, tan_so_lay_mau):
        niquy = 0.5 * tan_so_lay_mau
        tan_so_cat_binh_thuong = tan_so_cat / niquy
        b, a = butter(4, tan_so_cat_binh_thuong, btype='low', analog=False)
        tin_hieu_loc = filtfilt(b, a, tin_hieu)
        return tin_hieu_loc

    def _ve_do_thi_va_pho_tan(self, t, tin_hieu, tieu_de):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

        # Vẽ đồ thị của tín hiệu
        ax1.plot(t, tin_hieu)
        ax1.set_title(tieu_de)
        ax1.set_xlabel('Thời Gian (s)')
        ax1.set_ylabel('Biên Độ')

        # Vẽ phổ tần số của tín hiệu
        ax2.specgram(tin_hieu, Fs=self.tan_so_lay_mau, NFFT=256, cmap='viridis')
        ax2.set_title('Phổ Tần Số của Tín Hiệu')
        ax2.set_xlabel('Thời Gian (s)')
        ax2.set_ylabel('Tần Số (Hz)')

        plt.tight_layout()

        # Nhúng hình matplotlib vào cửa sổ Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppXuLyTinHieu(root)
    root.mainloop()
