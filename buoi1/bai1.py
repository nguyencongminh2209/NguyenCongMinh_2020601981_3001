import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

n = 0  # Initialize n

def update_n():
    global n
    try:
        n = int(input_n.get())
        initialize_input_fields()
    except ValueError:
        messagebox.showerror("Error", "Vui lòng nhập một số tự nhiên.")

def initialize_input_fields():
    global entry_A, entry_B
    entry_A = []
    entry_B = []
    for i in range(n):
        row_A = []
        row_B = []
        for j in range(n):
            entry_Aij = Entry(window)
            entry_Aij.pack()
            row_A.append(entry_Aij)
        entry_A.append(row_A)
        entry_Bi = Entry(window)
        entry_Bi.pack()
        entry_B.append(entry_Bi)

def solve_linear_equations():
    global n  # Declare n as a global variable within this function
    try:
        A = np.zeros((n, n))
        B = np.zeros(n)

        for i in range(n):
            for j in range(n):
                A[i][j] = float(entry_A[i][j].get())

            B[i] = float(entry_B[i].get())

        if np.all(A == 0) and np.all(B == 0):
            messagebox.showinfo("Result", "Hệ phương trình vô số nghiệm.")
        else:
            rref_A, _ = np.linalg.qr(A)
            num_independent_columns = np.sum(np.abs(np.diag(rref_A)) > 1e-10)
            num_free_variables = n - num_independent_columns

            if num_free_variables > 0:
                messagebox.showinfo("Result", "Hệ phương trình có vô số nghiệm.")
            elif num_free_variables == 0:
                X = np.linalg.solve(A, B)
                result = "Nghiệm của hệ phương trình:\n"
                for i in range(n):
                    result += f"x[{i + 1}] = {X[i]}\n"
                messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Vui lòng nhập các giá trị hợp lệ.")
    except np.linalg.LinAlgError:
        messagebox.showinfo("Result", "Hệ phương trình vô nghiệm.")

# Create a Tkinter window
window = tk.Tk()
window.title("Linear Equation Solver")

# Create input fields for n
label_n = Label(window, text="Nhập số phương trình và số ẩn (n):")
label_n.pack()
input_n = Entry(window)
input_n.pack()

# Create a button to update n
update_n_button = Button(window, text="Cập nhật n", command=update_n)
update_n_button.pack()

initialize_input_fields()  # Initialize input fields initially

# Create a Solve button
solve_button = Button(window, text="Giải", command=solve_linear_equations)
solve_button.pack()

# Start the GUI main loop
window.mainloop()