import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
file_path = 'path/to/your/Student_Performance.csv'
data = pd.read_csv(file_path)

# Hiển thị thông tin tổng quan về dữ liệu
print("Thông tin tổng quan về dữ liệu:")
print(data.info())

# Hiển thị các thông số thống kê cơ bản
print("\nCác thông số thống kê cơ bản:")
print(data.describe())

# Tìm giá trị lớn nhất và nhỏ nhất trong từng cột
print("\nGiá trị lớn nhất trong từng cột:")
print(data.max())

print("\nGiá trị nhỏ nhất trong từng cột:")
print(data.min())

# Vẽ biểu đồ phân bố cho một số cột
plt.figure(figsize=(12, 6))

# Vẽ biểu đồ phân bố điểm cho một số môn học
sns.histplot(data['Math'], bins=20, kde=True, color='blue', label='Math')
sns.histplot(data['Reading'], bins=20, kde=True, color='green', label='Reading')
sns.histplot(data['Writing'], bins=20, kde=True, color='orange', label='Writing')

plt.title('Phân bố điểm các môn học')
plt.xlabel('Điểm')
plt.ylabel('Số lượng học sinh')
plt.legend()
plt.show()
