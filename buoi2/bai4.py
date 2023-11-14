import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
from tkinter import filedialog


def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir="/", title="Chọn file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if file_path:
        display_csv_data(file_path)

def display_csv_data(file_path):
    # Clear existing widgets in the frame
    for widget in frame_data.winfo_children():
        widget.destroy()

    # Read CSV data using pandas
    df = pd.read_csv(file_path)
    global in_data
    in_data = pd.read_csv(file_path, index_col = 0).values

    # Display header
    for col, header_value in enumerate(df.columns):
        label = Label(frame_data, text=header_value, padx=10, pady=5)
        label.grid(row=0, column=col)

    # Display data
    for row, (_, data) in enumerate(df.iterrows(), start=1):
        for col, value in enumerate(data):
            label = Label(frame_data, text=value, padx=10, pady=5)
            label.grid(row=row, column=col)

def create_repost():
    sv = in_data[:,1]
    tongsv = sv.sum()

    svF = in_data[:,10]
    svDat = np.subtract(sv,svF)
    svTruot = np.subtract(sv,svDat)
    sumDat = svDat.sum()
    sumTruot = svTruot.sum()
    tyle_dat = np.divide(np.sum(svDat),np.sum(sv))*100
    tyle_truot = 100 - tyle_dat

    svA_B = in_data[:,2:5+1]
    sumA_B = np.sum(svA_B)
    svC_D = in_data[:,6:9+1]
    sumC_D = np.sum(svC_D)
    sumF = np.sum(svF)

    svA = in_data[:,3]
    maxA = svA.max()
    i1 = np.where(svA == maxA)
    maxF = svF.max()
    minF = svF.min()
    i2 = np.where(svF == minF)
    i3 = np.where(svF == maxF)

    svBp = in_data[:,4]
    svB = in_data[:,5]
    svCp = in_data[:,6]
    svC = in_data[:,7]
    svDp = in_data[:,8]
    svD = in_data[:,9]

    label_result.config(text="-Tổng sinh viên dự thi: "+f"{tongsv} sinh viên\n"
                        + "-Số sinh viên đạt: "+f"{sumDat} sinh viên\n"
                        + "-Số sinh viên trượt: "+f"{sumTruot} sinh viên\n"
                        + "-Tỷ lệ sinh viên đạt: "+f"{tyle_dat} %\n"
                        + "-Tỷ lệ sinh viên trượt: "+f"{tyle_truot} %\n"
                        + "-Số sinh viên có điểm khá/giỏi là: "+f"{sumA_B} sinh viên\n"
                        + "-Số sinh viên có điểm TB/yếu là: "+f"{sumC_D} sinh viên\n"
                        + "-Số sinh viên có điểm kém (trượt) là: "+f"{sumF} sinh viên\n"
                        + "-Lớp có nhiều điểm A nhất là: {0} có {1} sinh viên đạt điểm A\n".format(in_data[i1,0],maxA)
                        + "-Lớp có ít điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i2,0],minF)
                        + "-Lớp có nhiều điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i3,0],maxF))
    plt.plot(range(len(svA)), svA, 'r-', label="Diem A")
    plt.plot(range(len(svBp)), svBp, 'o-', label="Diem B+")
    plt.plot(range(len(svB)), svB, 'y-', label="Diem B")
    plt.plot(range(len(svCp)), svCp, 'g-', label="Diem C+")
    plt.plot(range(len(svC)), svC, 'b-', label="Diem C")
    plt.plot(range(len(svDp)), svDp, 'p-', label="Diem D+")
    plt.plot(range(len(svD)), svD, 'm-', label="Diem D")
    plt.plot(range(len(svF)), svF, 'k-', label="Diem F")
    plt.xlabel('Lớp')
    plt.ylabel('Số sv đạt điểm')
    plt.legend(loc='upper right')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


w = Tk()
w.title("Báo cáo học phần môn học")

button_file = Button(w, text="Chọn file", command=open_file_dialog)
button_file.pack()

frame_data = Frame(w)
frame_data.pack()

button_cre = Button(w, text="Tạo báo cáo", command=create_repost)
button_cre.pack()

frame_result = Frame(w)
frame_result.pack()

label_result = Label(frame_result, text="", justify='left', font=('Helvetica', 10, 'bold'))
label_result.pack(side=LEFT)

plot_frame = Frame(frame_result)
plot_frame.pack(side=LEFT)

w.mainloop()