# 📚 Library Management System (LMS) - Group 12

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Status](https://img.shields.io/badge/Status-Completed-success)

Chào mừng đến với dự án **Hệ thống Quản lý Thư viện** (Console-based) của Nhóm 12. Đây là ứng dụng quản lý quy trình mượn trả sách, quản lý độc giả và kho sách, được xây dựng theo kiến trúc MVC, sử dụng **Python** và lưu trữ dữ liệu bền vững bằng **JSON**.

---

## 🚀 Tính năng nổi bật

Hệ thống được phân quyền chặt chẽ giữa **Khách (Guest)**, **Thành viên (Member)** và **Thủ thư (Librarian/Admin)**.

### 1. 👮 Dành cho Thủ thư (Librarian/Admin)
* **Quản lý Kho sách:** Thêm sách mới, cập nhật số lượng tồn kho.
* **Quản lý Độc giả:** Xem danh sách thành viên, **Chặn (Block)** hoặc **Mở khóa (Unblock)** tài khoản vi phạm.
* **Lưu thông (Circulation):**
    * **Check-out:** Mượn sách hộ thành viên tại quầy (Admin có quyền duyệt ngoại lệ).
    * **Check-in:** Nhận trả sách, hệ thống tự động tính ngày quá hạn và hiển thị số tiền phạt (nếu có).
* **Giám sát:** Xem danh sách tất cả các phiếu mượn đang kích hoạt (Active Loans).

### 2. 👤 Dành cho Thành viên (Member)
* **Tìm kiếm thông minh:** Tìm sách theo Tên hoặc Năm xuất bản. Xem chi tiết số lượng tồn kho/khả dụng.
* **Giỏ sách (Book Bag):** Thêm sách vào giỏ với số lượng tùy chọn trước khi mượn chính thức.
* **Quản lý cá nhân:** Xem lịch sử giao dịch (Transaction History), Cập nhật thông tin cá nhân.
* **Quy tắc mượn:** Tự động bị chặn mượn mới nếu đang giữ sách quá hạn (Overdue).

### 3. 🌐 Tính năng chung
* **Bảo mật:** Mật khẩu được mã hóa an toàn (SHA-256).
* **Quên mật khẩu:** Tính năng giả lập gửi mã OTP qua email để lấy lại mật khẩu.
* **Dữ liệu bền vững:** Tự động lưu trữ vào file `library_data.json`, không mất dữ liệu khi tắt ứng dụng.

---

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.9+
* **Kiến trúc:** MVC (Model-View-Controller)
* **Cơ sở dữ liệu:** JSON (File-based storage)
* **Đóng gói:** Docker
* **Công cụ:** VS Code, Git

---

## ⚙️ Hướng dẫn Cài đặt & Chạy

### Cách 1: Chạy trực tiếp bằng Python (Local)

1.  **Clone dự án về máy:**
    ```bash
    git clone [https://github.com/VDucThinh166/LIBRARY-MANAGEMENT-SYSTEM.git](https://github.com/VDucThinh166/LIBRARY-MANAGEMENT-SYSTEM.git)
    ```

2.  **Di chuyển vào thư mục chứa code:**
    ```bash
    cd LIBRARY-MANAGEMENT-SYSTEM
    cd SourceCode
    ```

3.  **Chạy ứng dụng:**
    ```bash
    python main.py
    ```
    *(Lưu ý: Hệ thống sẽ tự động tạo file `library_data.json` và tài khoản Admin mặc định trong lần chạy đầu tiên).*

---

### Cách 2: Chạy bằng Docker (Khuyên dùng)

Đảm bảo bạn đang đứng ở thư mục `SourceCode` (nơi chứa file `Dockerfile`).

1.  **Build Image:**
    ```bash
    docker build -t group12-lms .
    ```

2.  **Chạy Container (Interactive Mode):**
    * **Windows (PowerShell):**
        ```powershell
        docker run -it -v ${PWD}:/app group12-lms
        ```
    * **Mac / Linux / Git Bash:**
        ```bash
        docker run -it -v $(pwd):/app group12-lms
        ```

    *⚠️ **Lưu ý:** Tham số `-it` là bắt buộc để nhập liệu bàn phím. Tham số `-v` giúp dữ liệu JSON được lưu lại trên máy thật.*

---

## 🔑 Tài khoản Mặc định

Ngay sau khi khởi chạy lần đầu, bạn có thể đăng nhập bằng tài khoản Admin quản trị:

| Vai trò | Username | Password |
| :--- | :--- | :--- |
| **Admin (Librarian)** | `admin` | `123456` |

*Để test chức năng Member, vui lòng chọn **"3. Register"** từ menu chính để tạo tài khoản sinh viên mới.*

---

## 📂 Cấu trúc dự án

```text
LIBRARY-MANAGEMENT-SYSTEM/
└── SourceCode/
    ├── controllers.py      # Xử lý Logic nghiệp vụ (Business Logic)
    ├── models.py           # Định nghĩa cấu trúc User, Book
    ├── database.py         # Xử lý Đọc/Ghi file JSON
    ├── main.py             # Giao diện Console (Entry Point)
    ├── library_data.json   # Database (Tự sinh ra khi chạy)
    ├── Dockerfile          # Cấu hình Docker
    └── README.md           # Hướng dẫn sử dụng