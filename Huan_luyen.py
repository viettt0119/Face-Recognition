import cv2
import os
import numpy as np
from PIL import Image

# Kiểm tra OpenCV hỗ trợ nhận diện không
if not hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
    raise Exception("OpenCV không hỗ trợ LBPHFaceRecognizer! Hãy cài đặt opencv-contrib-python")

# Khởi tạo bộ nhận diện khuôn mặt
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Anh'

def getImagesAndLabels(path):
    # Lấy danh sách file ảnh trong thư mục
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]
    faces = []
    IDs = []

    # Kiểm tra nếu thư mục không có ảnh
    if len(imagePaths) == 0:
        print("Không tìm thấy ảnh trong thư mục 'Anh'. Hãy chạy chương trình lấy mẫu trước!")
        return None, None

    for imagePath in imagePaths:
        try:
            faceImg = Image.open(imagePath).convert('L')  # Chuyển sang ảnh grayscale
            faceNp = np.array(faceImg, 'uint8')

            # Lấy ID từ tên file (user.<ID>.<Số thứ tự>.jpg)
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)

            print(f"Đang xử lý ID: {ID}")

            cv2.imshow("Training", faceNp)
            cv2.waitKey(10)
        except Exception as e:
            print(f"Lỗi khi xử lý file {imagePath}: {e}")

    return IDs, faces

# Lấy dữ liệu ảnh và ID
Ids, faces = getImagesAndLabels(path)

# Kiểm tra nếu có dữ liệu hợp lệ trước khi huấn luyện
if Ids is None or faces is None or len(Ids) == 0:
    print("Không có dữ liệu để huấn luyện!")
else:
    print("Bắt đầu huấn luyện mô hình...")
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainningData.yml')
    print("Huấn luyện hoàn tất! Dữ liệu được lưu trong trainningData.yml")

cv2.destroyAllWindows()
