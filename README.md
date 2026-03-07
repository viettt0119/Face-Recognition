# Face Recognition App với Python và OpenCV

Dự án này tập trung vào việc xây dựng một hệ thống nhận diện khuôn mặt trong Video thời gian thực, kết hợp sức mạnh của thư viện OpenCV và hệ quản trị cơ sở dữ liệu SQLite để quản lý thông tin người dùng.

## 📌 1. Giới thiệu
Ứng dụng áp dụng thuật toán **LBPH (Local Binary Patterns Histograms)** để giải quyết hai bài toán chính:
* **Identification (Xác định danh tính):** Đối sánh 1-N để tìm ra danh tính.
* **Verification (Xác thực danh tính):** Đối sánh 1-1 để xác thực người dùng.

## 🛠 2. Công nghệ và Thư viện
* **Ngôn ngữ:** Python
* **Thư viện chính:**
    * `opencv-python` & `opencv-contrib-python`: Xử lý hình ảnh và nhận diện.
    * `sqlite3`: Quản lý cơ sở dữ liệu người dùng.
    * `numpy`, `Pillow (PIL)`, `pickle`: Hỗ trợ xử lý mảng và dữ liệu ảnh.

## 📊 3. Cấu trúc Cơ sở dữ liệu (Database Schema)
Dự án sử dụng SQLite (`FaceBase.db`) để lưu trữ thông tin. Cấu trúc bảng `People` như sau:

| Trường (Field) | Kiểu dữ liệu | Mô tả |
| :--- | :--- | :--- |
| **ID** | `INTEGER` | Khóa chính, mã định danh duy nhất cho mỗi khuôn mặt |
| **Name** | `TEXT` | Họ và tên người dùng |
| **Age** | `INTEGER` | Tuổi |
| **Gender** | `TEXT` | Giới tính |

### SQL Query tạo bảng:
```sql
CREATE TABLE "People" (
    "ID" INTEGER NOT NULL,
    "Name" TEXT,
    "Age" INTEGER,
    "Gender" TEXT,
    PRIMARY KEY("ID")
);

## 📂 4. Cấu trúc thư mục dự án
├── Anh/                   # Thư mục lưu trữ các ảnh mẫu chụp từ camera
├── FaceBase.db            # Tệp cơ sở dữ liệu SQLite
├── trainingData.yml       # Tệp chứa dữ liệu sau khi đã huấn luyện
├── haarcascade_frontalface_default.xml # File cấu hình phát hiện khuôn mặt
├── Laymau.py              # Script chụp ảnh mẫu và nhập liệu CSDL
├── Training.py            # Script huấn luyện bộ nhận diện
└── Nhandien.py            # Script thực hiện nhận diện thực tế
