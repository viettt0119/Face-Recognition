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

## 📂 4. Cấu trúc thư mục dự án
```text
├── Anh/                   # Thư mục lưu ảnh mẫu (.jpg)
├── FaceBase.db            # Cơ sở dữ liệu SQLite
├── trainingData.yml       # Dữ liệu sau khi huấn luyện
├── haarcascade_frontalface_default.xml # File cấu hình nhận diện
├── Laymau.py              # Thu thập ảnh và lưu SQL
├── Training.py            # Huấn luyện Model
└── Nhandien.py            # Chạy ứng dụng thực tế
```
## 🚀 5. Hướng dẫn thiết lập và vận hành

### Bước 1: Cài đặt môi trường

Mở **Terminal** và chạy lệnh:

```bash
pip install opencv-python opencv-contrib-python numpy Pillow
```
### Bước 2: Quy trình thực hiện (Quan trọng)
* **Chạy Laymau.py:
* Nhập ID (dạng số) và Tên của bạn vào console khi được yêu cầu.
* Camera sẽ tự động mở, hãy nhìn thẳng vào camera. Máy sẽ chụp khoảng 20 tấm ảnh mẫu và lưu vào thư mục Anh/.
* **Chạy Huan_luyen.py:
* Chương trình sẽ quét toàn bộ ảnh trong thư mục Anh/ để trích xuất đặc trưng khuôn mặt.
Sau khi quá trình huấn luyện hoàn tất, file trainingData.yml sẽ được khởi tạo trong thư mục dự án.
* **Chạy Nhan_dang.py:
* Đây là bước cuối cùng để mở camera nhận diện.
* Tên và thông tin cá nhân của bạn sẽ hiển thị ngay trên khung chữ nhật bao quanh khuôn mặt nếu nhận diện thành công.


