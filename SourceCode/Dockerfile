# 1. Chọn hệ điều hành nền (Base Image) là Python siêu nhẹ
FROM python:3.9-slim

# 2. Thiết lập biến môi trường để Python in log ngay lập tức (không bị delay)
ENV PYTHONUNBUFFERED=1

# 3. Tạo thư mục làm việc bên trong Container
WORKDIR /app

# 4. Copy toàn bộ code từ máy thật vào trong Container
COPY . /app

# 5. Lệnh chạy chương trình khi Container khởi động
CMD ["python", "main.py"]