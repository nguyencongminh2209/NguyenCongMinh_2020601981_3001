import cv2
import numpy as np

def enhance_image_brightness(image_path, output_path, alpha=1.5, beta=30):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)

    # Tăng cường độ sáng của ảnh
    enhanced_image = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

    # Hiển thị và lưu ảnh kết quả
    cv2.imshow('Ảnh sau chỉnh sửa: ', enhanced_image)
    cv2.imwrite(output_path, enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Thay đổi các đường dẫn và tham số tùy thuộc vào ảnh và mức độ tăng cường mong muốn
image_path = 'path/to/your/image.jpg'
output_path = 'path/to/save/enhanced_image.jpg'
enhance_image_brightness(image_path, output_path)
