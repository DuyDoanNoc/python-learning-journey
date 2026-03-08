# === Create Tuple ===
empty = ()
single = (42,)              # phải có dấu phẩy, (42) chỉ hiểu là số 42
coords = (10.5, 20.3)
mixed = (1, "hello", True)
from_list = tuple([1, 2, 3])

# === Truy cập ===
point = (10, 20, 30)
print(point[0])     # 10
print(point[-1])    # 30
print(point[1:])    # (20, 30)

# === Tuple không thể thay đổi ===
# point[0] = 99     # Báo TypeError!

# === Unpacking (giải nén - rất hữu ích) ===
x, y, z = point
print(x, y, z)      # 10, 20, 30

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)        # 1
print(rest)         # [2, 3, 4, 5]  # kết quả là list

*start, last = (1, 2, 3, 4, 5)
print(start)        # [1, 2, 3, 4]  # kết quả là list
print(last)         # 5

# Swap giá trị (đăc trưng Python)
a, b = 1, 2
a, b = b, a         # a=2, b=1  - không cần biến tạm

# === Các phương thức ===
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))    # 3 # đếm số lần xuất hiện của '2'
print(nums.index(3))    # 2

# === Khi nào dùng tuple thay list? ===
# 1. Dữ liệu cố định, không cần thay đổi
SUPPORTED_BROWSERS = ("chrome", "firefox", "edge")
HTTP_METHODS = ("GET", "POST", "PUT", "DELETE", "PATCH")

# 2. Làm key cho dictionary (list không được)
cache = {}
cache[(200, "OK")] = "Success"      # Tuple làm key được
# cache[ơ200, "OK"] = "Success"     # List không làm key được

# 3. Hàm trả về nhiều giá trị
def run_test(test_name):
    status = "PASS"
    duration = 1.5
    return status, duration         # Thực chất trả về tuple vì hàm luôn trả về một giá trị

result, time = run_test("Login")    # ("PASS", 1.5)


# === Create Set ===
empty = set()               # Không phải {} (đó là dict rỗng)
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])     # {1, 2, 3} - tự loại số trùng

# === Thêm / Xóa ===
s = {1, 2, 3}
s.add(4)                    # {1, 2, 3, 4}
s.update([5, 6, 7])         # {1, 2, 3, 4, 5, 6, 7}
s.remove(7)                 # Xóa 7 (KeyError nếu không có)
s.discard(99)               # Xóa 99 (Không lỗi nếu không có)
popped = s.pop()            # Xóa và trả về phần tử ngẫu nhiên

# === Phép toán tập hợp (Rất mạnh cho testing) ===
expected = {"id", "name", "email", "phone", "address"}
actual = {"id", "name", "email", "role"}

# Giao (có trong cả 2)
print(expected & actual)
# {"id", "name", "email"}       # in ra các giá trị giao của expected & actual

# Hợp (có trong ít nhất một)
print(excepted | actual)
# {"id", "name", "email", "phone", "address", "role"}       # in ra cả giá trị giao và không giao của expected & actual

# Hiệu (có trong expected, KHÔNG có trong actual) - tìm field thiếu
missing = expected - actual
print(f"Missing fiels: {missing}")
# {"phone", "address"}

# Hiệu đối xứng (có trong 1 trong 2, Không có trong cả 2)
diff = expected ^ actual
print(f"Different fields: {diff}")
# {"phone", "address", "role"}

# Kiểm tra tập con / tập cha
required = {"id", "name"}
print(required.issubset(actual))        # True  # Kiểm tra mọi phần tử của required có nằm trong actual không
print(actual.issuperset(required))      # True  # Kiểm tra xem actual có chứa tất cả phần tử của required hay không
print(expected.isdisjoint({99}))        # True  # Trả về True nếu hai tập không có phần tử chung nào. expected chứa toàn string và không chung với '99' nên trả về True

# === Ứng dụng thực tế ===
# Loại bỏ trùng lặp
raw_tags = ["bug", "ui", "bug", "critical", "ui"]
unique_tags = list(set(raw_tags))       # ["bug", "ui", "critical"]     # Tạo list sau khi set loại bỏ trùng lặp

# Kiểm tra response có đủ field không
def validate_respone_fields(response_data, required_fields):
    actual_fields = set(response_data.keys())           # Lấy set các key hiện có trong respone_data
    missing = required_fields - actual_fields           # Lấy set giá trị có trong required_fields mà không có trong actual_fields
    extra = actual_fields - required_fields             # Lấy set giá trị có trong actual_fields mà không có trong required_fields
    return missing, extra

# === Set bất biến (frozenset) ===
# Giống set nhưng không thay đổi được -> có thể dùng làm key dict
immutable = frozenset([1, 2, 3])
# immutable.add(4)          # Lỗi AttributeError