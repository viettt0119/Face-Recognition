import cv2
import sqlite3
import os

# Khởi động camera
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Hàm insert/update dữ liệu vào SQLite
def insertOrUpdate(Ids, Name):
    conn = sqlite3.connect("FaceBase.db")
    cursor = conn.execute("SELECT * FROM People WHERE ID = ?", (Ids,))
    isRecordExist = cursor.fetchone() is not None  # Kiểm tra xem có dữ liệu chưa

    if isRecordExist:
        conn.execute("UPDATE People SET Name = ? WHERE ID = ?", (Name, Ids))
    else:
        conn.execute("INSERT INTO People (ID, Name) VALUES (?, ?)", (Ids, Name))

    conn.commit()
    conn.close()


# Nhập thông tin người dùng
idt = input("Nhập ID: ")
tent = input("Nhập Tên: ")

insertOrUpdate(idt, tent)

# Tạo thư mục "Anh" nếu chưa có
if not os.path.exists("Anh"):
    os.makedirs("Anh")

sampleNum = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("Không thể mở camera. Kiểm tra thiết bị!")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        sampleNum += 1
        face_img_path = f"Anh/user.{idt}.{sampleNum}.jpg"
        cv2.imwrite(face_img_path, gray[y:y + h, x:x + w])

        cv2.imshow("Frame", img)

    # Nhấn 'q' để thoát hoặc chụp đủ 20 ảnh
    if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum >= 20:
        break

# Giải phóng camera và đóng cửa sổ
cam.release()
cv2.destroyAllWindows()
