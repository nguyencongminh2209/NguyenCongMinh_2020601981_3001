import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd

# Đọc file CSV
df = pd.read_csv('Student_Performance.csv')

# Trích xuất cột cần thiết cho dữ liệu x và y
x1 = df['Hours Studied']
x2 = df['Previous Scores']
x3 = df['Extracurricular Activities']
x4 = df['Sleep Hours']
x5 = df['Sample Question Papers Practiced']
y = df['Performance Index']

#Biểu đồ dữ liệu huấn luyện cho cả 5 biến
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs[0, 0].scatter(x1, y)
axs[0, 0].set_xlabel('Hours Studied')
axs[0, 0].set_ylabel('Performance Index')
axs[0, 1].scatter(x2, y)
axs[0, 1].set_xlabel('Previous Scores')
axs[0, 1].set_ylabel('Performance Index')
axs[0, 2].scatter(x3, y)
axs[0, 2].set_xlabel('Extracurricular Activities')
axs[0, 2].set_ylabel('Performance Index')
axs[1, 0].scatter(x4, y)
axs[1, 0].set_xlabel('Sleep Hours')
axs[1, 0].set_ylabel('Performance Index')
axs[1, 1].scatter(x5, y)
axs[1, 1].set_xlabel('Sample Question Papers Practiced')
axs[1, 1].set_ylabel('Performance Index')

#Ẩn trục thừa
axs[1, 2].axis('off')
plt.tight_layout()
plt.show()
# Tạo model cho tập dữ liệu
X = np.column_stack((x1, x2, x3, x4, x5))
Y = np.array(y).reshape(-1, 1)

# Khởi tạo biến
W = tf.Variable(tf.random.normal([5, 1], dtype=tf.float32), name="W")
b = tf.Variable(tf.random.normal([1], dtype=tf.float32), name="b")

# Thiết lập tốc độ học và số vòng lặp
learning_rate = 0.01
training_epochs = 100

# Hàm dự đoán của mô hình
def linear_regression(X):
    return tf.matmul(tf.cast(X, tf.float32), W) + b

# Hàm mất mát Mean Squared Error
def mean_squared_error(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))

# Tối ưu hóa bằng Gradient Descent
optimizer = tf.optimizers.SGD(learning_rate)

# Huấn luyện mô hình
for epoch in range(training_epochs):
    with tf.GradientTape() as tape:
        y_pred = linear_regression(X)
        loss = mean_squared_error(y_pred, Y)

    gradients = tape.gradient(loss, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))

    if (epoch + 1) % 10 == 0:
        print("Epoch", (epoch + 1), ": loss =", loss.numpy())
        # Lấy giá trị cuối cùng của trọng số và độ lệch
weight = W.numpy()
bias = b.numpy()
#thêm chức năng lan truyền ngược
class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # áp dụng quy tắc dây chuyền để tìm đạo hàm của hàm mất mát theo trọng số2 và trọng số1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # cập nhật các trọng số với đạo hàm (độ dốc) của hàm mất
        self.weights1 += d_weights1
        self.weights2 += d_weights2
# Tính toán dự đoán cho tất cả 5 biến
predictions = np.dot(X, weight) + bias

# Vẽ biểu đồ kết quả cho tất cả 5 biến
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs[0, 0].scatter(x1, y)
axs[0, 0].plot(x1, predictions, 'r', label='Dự đoán')
axs[0, 0].set_xlabel('Số giờ học')
axs[0, 0].set_ylabel('Chỉ số thành tích')
axs[0, 0].legend()
axs[0, 1].scatter(x2, y)
axs[0, 1].plot(x2, predictions, 'r', label='Dự đoán')
axs[0, 1].set_xlabel('Điểm trước đó')
axs[0, 1].set_ylabel('Chỉ số thành tích')
axs[0, 1].legend()
axs[0, 2].scatter(x3, y)
axs[0, 2].plot(x3, predictions, 'r', label='Dự đoán')
axs[0, 2].set_xlabel('Hoạt động ngoại khóa')
axs[0, 2].set_ylabel('Chỉ số thành tích')
axs[0, 2].legend()
axs[1, 0].scatter(x4, y)
axs[1, 0].plot(x4, predictions, 'r', label='Dự đoán')
axs[1, 0].set_xlabel('Giờ ngủ')
axs[1, 0].set_ylabel('Chỉ số thành tích')
axs[1, 0].legend()
axs[1, 1].scatter(x5, y)
axs[1, 1].plot(x5, predictions, 'r', label='Dự đoán')
axs[1, 1].set_xlabel('Lượng đề luyện tập')
axs[1, 1].set_ylabel('Chỉ số thành tích')
axs[1, 1].legend()
plt.tight_layout()
plt.show()
#Ẩn trục thừa
axs[1, 2].axis('off')
plt.tight_layout()
