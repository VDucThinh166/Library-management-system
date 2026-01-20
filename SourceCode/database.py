# Mục đích: Thay thế SQL, dùng để đọc/ghi dữ liệu xuống file JSON
import json
import os

DB_FILE = "library_data.json"

# Cấu trúc dữ liệu mặc định
DEFAULT_DATA = {
    "users": [],
    "books": [],
    "loans": []
}

def load_data():
    """Đọc dữ liệu từ file. Nếu chưa có thì tạo mới kèm Admin mặc định."""
    if not os.path.exists(DB_FILE):
        init_data = DEFAULT_DATA.copy()
        
        # Tạo Admin mặc định: admin / 123456
        init_data["users"].append({
            "account_id": 1,
            "username": "admin",
            "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", # Hash của 123456
            "email": "admin@library.com",
            "fullname": "Administrator",
            "role": "Librarian",
            "phone": "0909000111",
            "address": "Library HQ",
            "dob": "01/01/1990",
            "gender": "Other",
            "is_blocked": False
        })
        
        # Tạo sách mẫu
        init_data["books"].append({
            "isbn": "978-1", "title": "Introduction to Python", "author": "Guido van Rossum",
            "publisher": "O'Reilly", "year": 2024, "quantity": 10, "location": "Shelf A1", "category": "IT"
        })
        init_data["books"].append({
            "isbn": "978-2", "title": "Clean Code", "author": "Robert C. Martin",
            "publisher": "Prentice Hall", "year": 2008, "quantity": 5, "location": "Shelf B2", "category": "IT"
        })
        
        save_data(init_data)
        return init_data
        
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return DEFAULT_DATA

def save_data(data):
    """Lưu dữ liệu xuống file JSON"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)