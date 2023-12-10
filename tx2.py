import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import csv

#Đo?n code này d? gi?i h? phuong tŕnh tuy?n tính Ax = B b?ng cách s? d?ng ma tr?n ngh?ch d?o c?a A và tích vô hu?ng c?a A1 và B
A = np.array([(1, 2), (3, 4)])
B = np.array([5, 6])
A1 = np.linalg.inv(A)  # tao ma tran nghich dao
print(A)
print(B)
print(A1)
X = np.dot(A1, B)
print('Nghiem cua he:', X)
# C?i ti?n có th? ch?n tru?c s? phuong tŕnh trong h?,xóa d? li?u v?a du?c nh?p, luu k?t qu? tính toán h? phuong tŕnh và k?t qu?,hi?n th? l?ch s? tính toán.
# Hàm t?o h? các phuong tŕnh
history = []
def add_to_history(coefficients, results, solution):
    history.append({'coefficients': coefficients, 'results': results, 'solution': solution})

def create(entry):
    delete_fields()
    num_equations = int(entry.get())
    for i in range(num_equations):
        frame = tk.Frame(window)
        frame.pack(side=tk.TOP, padx=10, pady=5)
        equation_frames.append(frame)

        equation_entries = []
        label = tk.Label(frame, text=f"Phuong tŕnh {i + 1}:")
        label.pack(side=tk.LEFT)

        for j in range(num_equations + 1):
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            equation_entries.append(entry)

        equation_entries_list.append(equation_entries)


# Hàm xóa các h? phuong tŕnh
def delete_fields():
    result.delete(1.0, tk.END)
    equation_entries_list.clear()
    for frame in equation_frames:
        frame.destroy()

# Ki?m tra d? li?u h?p l?
def validate_input(entry):
    try:
        num_equations = entry.get()

        # Ki?m tra xem d?u vào có ph?i là s? nguyên hay không
        if not num_equations.isdigit():
            raise ValueError("Nh?p s? nguyên h?p l?.")

        num_equations = int(num_equations)

        if num_equations <= 0 or num_equations > 10:
            raise ValueError("Nh?p l?i s? phuong tŕnh h?p l?.")

        return True
    except ValueError:
        messagebox.showerror("Error", "Nh?p dúng d? li?u (s? nguyên t? 1 d?n 10).")
        return False
# Gi?i h? phuong tŕnh v?a t?o
def solve(entry):
    try:
        coefficients = []
        results = []

        for entry_list in equation_entries_list:
            equation_coefficients = []
            for entry in entry_list[:-1]:
                val = float(entry.get())
                equation_coefficients.append(val)
            coefficients.append(equation_coefficients)

            result_val = float(entry_list[-1].get())
            results.append(result_val)

        a = np.array(coefficients)
        b = np.array(results)

        # Ki?m tra xem h? phuong tŕnh có nghi?m hay không
        if np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) == a.shape[1]:
            # H? phuong tŕnh có nghi?m duy nh?t
            x = np.linalg.solve(a, b)

            result.delete(1.0, tk.END)
            result.insert(tk.END, "K?t qu?:\n")
            for i, val in enumerate(x):
                result.insert(tk.END, f"x{i + 1} = {round(val, 2)}\n")

            # Hi?n th? k?t qu? ra c?a s? l?nh
            print("K?t qu?:")
            for i, val in enumerate(x):
                print(f"x{i + 1} = {round(val, 2)}")

            # Luu vào l?ch s?
            add_to_history(coefficients, results, x)

        elif np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) < a.shape[1]:
            # H? phuong tŕnh có vô s? nghi?m
            result.delete(1.0, tk.END)
            result.insert(tk.END, "H? phuong tŕnh có vô s? nghi?m")

            # Hi?n th? thông báo ra c?a s? l?nh
            print("H? phuong tŕnh có vô s? nghi?m")

        else:
            # H? phuong tŕnh vô nghi?m
            result.delete(1.0, tk.END)
            result.insert(tk.END, "H? phuong tŕnh vô nghi?m")

            # Hi?n th? thông báo ra c?a s? l?nh
            print("H? phuong tŕnh vô nghi?m")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm d? ch?n file CSV và c?p nh?t d? li?u t? giao di?n
def choose_csv_file():
    global equation_entries_list
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        delete_fields()
        data = np.genfromtxt(file_path, delimiter=',')
        num_equations, num_columns = data.shape
        for i in range(num_equations):
            frame = tk.Frame(window)
            frame.pack(side=tk.TOP, padx=10, pady=5)
            equation_frames.append(frame)

            equation_entries = []
            label = tk.Label(frame, text=f"Phuong tŕnh {i + 1}:")
            label.pack(side=tk.LEFT)

            for j in range(num_columns - 1):
                entry = tk.Entry(frame)
                entry.pack(side=tk.LEFT)
                entry.insert(tk.END, str(data[i, j]))
                equation_entries.append(entry)

            entry_result = tk.Entry(frame)
            entry_result.pack(side=tk.LEFT)
            entry_result.insert(tk.END, str(data[i, -1]))
            equation_entries.append(entry_result)

            equation_entries_list.append(equation_entries)

# Hàm d? luu k?t qu? vào file CSV
# Hàm d? luu h? phuong tŕnh và k?t qu? vào file CSV
def save_result_to_csv():
    try:
        # Ch?n noi luu file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if file_path:
            coefficients = []
            results = []

            for entry_list in equation_entries_list:
                equation_coefficients = []
                for entry in entry_list[:-1]:
                    val = float(entry.get())
                    equation_coefficients.append(val)
                coefficients.append(equation_coefficients)

                result_val = float(entry_list[-1].get())
                results.append(result_val)

            a = np.array(coefficients)
            b = np.array(results)

            # Ki?m tra xem h? phuong tŕnh có nghi?m hay không
            if np.linalg.matrix_rank(a) == np.linalg.matrix_rank(np.column_stack((a, b))) == a.shape[1]:
                # H? phuong tŕnh có nghi?m duy nh?t
                x = np.linalg.solve(a, b)

                with open(file_path, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)

                    # Ghi h? phuong tŕnh vào file
                    writer.writerow([f'x{i + 1}' for i in range(len(equation_entries_list[0]) - 1)] + ['Result'])
                    for coefficients, result in zip(coefficients, results):
                        writer.writerow(coefficients + [result])

                    # Ghi k?t qu? vào file
                    writer.writerow([''] * (len(equation_entries_list[0]) - 1) + [f'x{i + 1}' for i in range(len(x))])
                    writer.writerow([''] * (len(equation_entries_list[0]) - 1) + [round(val, 2) for val in x])

                messagebox.showinfo("Thông báo", "H? phuong tŕnh và k?t qu? dă du?c luu vào file CSV.")
            else:
                messagebox.showwarning("C?nh báo", "H? phuong tŕnh không có nghi?m duy nh?t.")
    except Exception as e:
        messagebox.showerror("L?i", str(e))
def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("L?ch s? k?t qu?")

    for entry in history:
        tk.Label(history_window, text=f"Coefficients: {entry['coefficients']}, Results: {entry['results']}, Solution: {entry['solution']}").pack()

# T?o c?a s? giao di?n
window = tk.Tk()
window.title("Gi?i h? phuong tŕnh tuy?n tính")

equation_entries_list = []
equation_frames = []

# Nh?p s? phuong tŕnh n
n_level = tk.Label(window, text="Nh?p s? phuong tŕnh (max = 10)")
n_level.pack()
n_entry = tk.Entry(window)
n_entry.pack()

# T?o button t?o h? phuong tŕnh
btn_create = tk.Button(window, text="T?o", command=lambda: validate_input(n_entry) and create(n_entry))
btn_create.pack()

# T?o button xóa h? phuong tŕnh
btn_delete = tk.Button(window, text="Xóa d? li?u", command=delete_fields)
btn_delete.pack()

# T?o button gi?i h? phuong tŕnh
btn_solve = tk.Button(window, text="Gi?i", command=lambda: solve(n_entry))
btn_solve.pack()

# Thêm button ch?n file CSV
btn_choose_csv = tk.Button(window, text="Ch?n File CSV", command=choose_csv_file)
btn_choose_csv.pack()

# Hi?n th? k?t qu?
result_label = tk.Label(window, text="K?t qu?")
result_label.pack()
result = tk.Text(window, height=3, width=30)
result.pack()
# Thêm button luu k?t qu? vào file CSV
btn_save_result = tk.Button(window, text="Luu K?t Qu? (CSV)", command=save_result_to_csv)
btn_save_result.pack()

btn_show_history = tk.Button(window, text="Xem L?ch S?", command=show_history)
btn_show_history.pack()

window.mainloop()
