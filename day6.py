# === Create Dictionary ===
empty = {}
user = {"name": "Tester", "age": 28, "role": "SDET"}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Tester", age=28)
from_keys = dict.fromkeys(["a", "b", "c"], 0)       # {"a": 0, "b": 0, "c": 0}

# === Truy cập ===
print(user["name"])                         # "Tester"  (KeyError nếu key không có)
print(user.get("name"))                     # "Tester"
print(user.get("salary"))                   # None      # salary không tồn tại nên trả về None
print(user.get("salary", 0))                # 0         # hàm dict.get(key, default_value) nên ở đây trả về 0

# === Thêm / Sửa / Xóa ===
user["email"] = "test@mail.com"             # Thêm key mới
user["age"] = 29                            # Sửa value
user.update({"phone": "123", "age": 30})    # Cập nhật nhiều key

del user["phone"]                           # Xóa key (KeyError nếu không có)
email = user.pop("email")                   # Xóa và trả về value
last = user.popitem                         # Xóa và trả về cặp (key, value) cuối

# setdefault - Lấy value nếu có, thêm nếu chưa có
user.setdefault("role", "viewer")           # "SDET" (đã có giá trị > không đổi)
user.setdefault("level", "junior")          # Thêm Level="junior" vì chưa có

# === Duyệt Dict ===
config = {"timeout": 30, "retries": 3, "base_url": "https://api.test.com"}

# Duyệt keys (mặc định)
for key in config:
    print(key)
"""
timeout
retries
base_url
"""

# Duyệt values
for value in config.values():
    print(value)
"""
30
3
https://api.test.com
"""

# Duyệt cả key và value (hay dùng nhất)
for key, value in config.items():
    print(f"{key}: {value}")
"""
timeout: 30
retries: 3
base_url: https://api.test.com
"""

# Kiểm tra key tồn tại
if "timeout" in config:
    print(f"Timeout: {config['timeout']}")          # Timeout: 30

# === Dict lồng nhau - giống Json ===
api_respone = {
    "status": 200,
    "data": {
        "user": {
            "id": 1,
            "name": "John",
            "roles": ["admin", "editor"]
        },
        "token": "abc123"
    },
    "errors": []
}

# Truy cập nested
print(api_respone["data"]["user"]["name"])          # "John"
print(api_respone["data"]["user"]["name"][0])       # "admin"

# An toàn hơn với get
name = api_respone.get("data", {}).get("user", {}).get("name", "Unknow")
"""
api_respone.get("data", {})
    Lấy phần "data" nếu có
    Nếu không có → trả {} (dict rỗng)
.get("user", {})
    Lấy "user" bên trong "data"
    Nếu không có → trả {}
.get("name", "Unknow")
    Lấy "name" bên trong "user"
    Nếu không có → trả "Unknow"
    Ở đây "name" tồn tại và có giá trị "John"
>>>> in ra name = "John"
"""

# === Dict Comprehension ===
# {key_expr: value_expr for item in iterable if condition}

squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Lọc dict
config = {"timeout": 30, "retries": 3, "debug": True, "verbose": False}
bool_configs = {k: v for k, v in config.items() if isinstance(v, bool)}

"""
# config.items()
Lấy hết các cặp trong config
# if isinstance(v, bool)
Chỉ giữ lại các cặp mà value là bool
>>>> {"debug": True, "verbose": False}
"""

# Đảo key-value
status_codes = {200: "OK", 404: "Not Found", 500: "Server Error"}
code_lookup = {v: k for k, v in status_codes.items()}
"""
# config.items()
Lấy hết các cặp trong config
>>>> {200: "OK", 404: "Not Found", 500: "Server Error"}
"""

# === Merge Dict ===
defaults = {"timeout": 30, "retries": 3}
custom = {"timeout": 60, "debug": True}

merged = defaults |  custom             # {"timeout": 60, "retries": 3, "debug": True}
# custom ghi đè defaults nếu trùng key
# merged = {**defaults, **custom}       # Kết quả tương tự

"""
Toán tử | trong Python dùng để gộp hai dictionary.
Các key của hai dict sẽ được kết hợp lại.
Nếu trùng key, giá trị của dict bên phải sẽ ghi đè.
"""