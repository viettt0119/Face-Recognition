import cv2
import numpy as np
import sqlite3

# Kiểm tra OpenCV hỗ trợ nhận diện không
if not hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
    raise Exception("OpenCV không hỗ trợ LBPHFaceRecognizer! Hãy cài đặt opencv-contrib-python")

# Tải mô hình phát hiện khuôn mặt
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Khởi động camera
cam = cv2.VideoCapture(0)

# Khởi tạo bộ nhận diện khuôn mặt
rec = cv2.face.LBPHFaceRecognizer_create()

# Kiểm tra xem file trainningData.yml có tồn tại không
try:
    rec.read("trainningData.yml")
except Exception as e:
    raise Exception("Không tìm thấy file trainningData.yml. Hãy huấn luyện mô hình trước!")

# Thiết lập thông số hiển thị văn bản
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (203, 23, 252)

# Hàm lấy thông tin từ SQLite dựa vào ID
def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cursor = conn.execute("SELECT * FROM People WHERE ID = ?", (id,))
    profile = cursor.fetchone()
    conn.close()
    return profile

while True:
    # Đọc ảnh từ camera
    ret, img = cam.read()
    if not ret:
        print("Không thể mở camera. Kiểm tra thiết bị!")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Dự đoán khuôn mặt
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        profile = getProfile(id)

        # Nếu độ chính xác cao (confidence thấp), hiển thị thông tin
        if conf < 70 and profile is not None:
            cv2.putText(img, f"Name: {profile[1]}", (x, y + h + 30), font, font_scale, font_color, 2)
        else:
            cv2.putText(img, "Unknown", (x, y + h + 30), font, font_scale, (0, 0, 255), 2)

        print(f"ID: {id}, Độ chính xác: {conf:.2f}")

    # Hiển thị hình ảnh
    cv2.imshow('Face Recognition', img)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng tài nguyên
cam.release()
cv2.destroyAllWindows()
