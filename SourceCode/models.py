# Mục đích: Định nghĩa khuôn mẫu cho các đối tượng (Object) trong hệ thống
class User:
    """Class đại diện cho Người dùng (bao gồm Admin và Member)"""
    def __init__(self, account_id, username, email, fullname, role="Member", phone="", address="", dob="", gender="", is_blocked=False):
        self.account_id = account_id
        self.username = username
        self.email = email
        self.fullname = fullname
        self.role = role            # Vai trò: "Member" hoặc "Librarian"
        self.phone = phone
        self.address = address
        self.dob = dob              # Ngày sinh
        self.gender = gender        # Giới tính
        self.is_blocked = is_blocked # Trạng thái: True = Bị chặn

class Book:
    """Class đại diện cho Sách"""
    def __init__(self, isbn, title, author, publisher, year, quantity, location, category="General"):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = int(year)       # Năm xuất bản
        self.quantity = int(quantity) # Số lượng thực tế trong kho
        self.location = location    # Vị trí kệ
        self.category = category    # Thể loại

    def __str__(self):
        return f"[{self.isbn}] {self.title} - {self.author} (SL: {self.quantity})"