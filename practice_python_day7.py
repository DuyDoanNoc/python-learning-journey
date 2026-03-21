"""
reponse_body = ""
if reponse_body:
    print("have data")
else:
    print("non-respone")    # print this row

# All things have "empty" or "0" are Falsy
False       # bool 
0           # int zero
0.0         # float zero
""          # empty string
None        # empty value

# Empty collection
[]          # empty list
()          # empty tuple
{}          # empty dict
set()

# Remaining things are Truthy
bool("False")       # True - string có nội dung, dù nội dung là "False"
bool("0")           # True - string có nội dung
bool(-1)            # True - số khác 0
bool([0])           # True - list có 1 phần tử (dù phần tử đó là 0)

# Check API respone có data không - gọn hơn viết == None hoặc == "" hoặc == []
errors = []
if not errors:
    print("No errors found")

response_data = None
if response_data is None:
    print("API trả về null")


# Ép kiểu (type casting)

# str > int
int("123")
int("12.5")         # ValueError: invalid literal for int() with base 10: '12.5' - không thể chuyển thẳng str float sang int
int(float("12.5"))

# str > float
print(float("3.14"))
print(float("inf"))        # inf - vô cực, python chấp nhận
print(float("str"))        # ValueError: could not convert string to float: 'str'

# int/float > str
str(200)        # "200"
str(3.14)       # "3.14"

# > bool (quay lại Truthy / Falsy)
bool("")        # False
bool("False")   # True
bool(0)         # False
bool(1)         # True


# Safe cast

def safe_int(value):
    #Ép sang int an toàn, trả về None nếu không được
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
    
# Test
print(safe_int("42"))       # 42
print(safe_int("abc"))      # None
print(safe_int(3.7))        # 3
print(safe_int(None))       # None


values = [0, 1, -1, 0.0, 0.1, "", "hello", "False", None, True, False, [], [0], {}, {0:0}]
# In dạng: giá_trị → True/False
for i in values:
    print(bool(i))

int("123")          # 123
int("12.5")         # ValueError
int("abc")          # ValueError
float("inf")        # inf
bool("")            # False
bool("False")       # True

def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

value = input("Nhập giá trị muốn thử: ")
print(safe_int(value))

# Cú pháp cơ bản

test_name = "Login Valid"
status = "PASS"
duration = 1.2045

# Cách cũ (chậm, khó đọc)
print("Test: " + test_name + " | Status: " + status)

# f-string (nhanh, gọn, dùng cách này)
print(f"Test: {test_name} | Status:  {status}")

# Format số
price = 1234567.891
rate = 0.8567
test_id = 42

# 2 chữ số thập phân
print(f"{price:.2f}")       # 1234567.89

# Dấu phân cách hàng nghìn + 2 decimal
print(f"{price:,.2f}")      # 1,234,567.89

# Phần trăm
print(f"{rate:.1%}")        # 85.7%

# Zero-padding
print(f"{test_id:05d}")     # 00042

# Kết hợp trong SDET
print(f"Pass rate: {rate:.1%}")     # Pass rate: 85.7%
print(f"Respone: {duration:.2f}s")  # Respone: 1.20s
print(f"TC-{test_id:04d}")          # TC-0042


# Căn chỉnh - Alignment
# < căn trái
# > căn phải
# ^ căn giữa
# Số sau dấu : là độ rộng

name = "Login"
print(f"|{name:<20}|")       # |Login               |
print(f"|{name:>20}|")       # |               Login|
print(f"|{name:^20}|")       # |       Login        |

# Ứng dụng tạo bản test report

tests = [
    ("Login Valid",     "PASS", 1.20),
    ("Login Invalid",   "FAIL", 0.85),
    ("Signup Empty",    "FAIL", 0.32),
    ("Logout",          "PASS", 0.15)
]

# Header
print()
print()
print(f"| {'Test Name':<20} | {'Status':^6} | {'Duration':>10} |")
print(f"|{'-'*22}|{'-'*8}|{'-'*12}|")

# Row
for name, status, dur in tests:
    print(f"| {name:<20} | {status:^6} | {dur:>8.2f}s |")


# Biểu thức trong f-string

status_code = 200
print(f"Result: {'PASS' if status_code == 200 else 'FAIL'}")        # Result: PASS


items = ["a", "b", "c"]
print(f"Count: {len(items)}")       # Count: 3

"""
"""
**Bài 1:** Format số:
- In `1234567.891` với 2 decimal + dấu phân cách hàng nghìn
- In `0.8567` dạng phần trăm 1 decimal
- In số `42` với zero-padding 5 ký tự

**Bài 2 (Tổng hợp):** Viết chương trình "Test Info Printer":
- Khai báo: `test_name`, `tester`, `status_code` (int), `response_time` (float), `is_passed` (bool)
- In ra report dạng:
```
Tester: Duy | Test: Login Valid
Status: 200 (PASS) | Response: 1.20s
Pass rate: 85.7%

# Bài 1
price = 1234567.891
rate = 0.8567
num_id = 42

print(f"{price:,.2f}")
print(f"{rate:.1%}")
print(f"{num_id:05d}")

# Bài 2
tester = "Duy"
test_name = "Login Valid"
status_code = 200
response_time = 1.20
pass_rate = 0.857

result = "PASS" if status_code == 200 else "FAIL"

print(f"Tester: {tester} | Test: {test_name}")
print(f"Status: {status_code} ({result}) | Response: {respone_time:.2f}s")
print(f"Pass rate: {pass_rate:.1%}")
"""
bien_int = 123
bien_float = 0.0
bien_str = "string"
bien_bool = True
bien_bool_2 = False
bien_none = None

a = 15
b = 10

print(a - b)
print(a + b)
print(a * b)
print(a / b)
print(a // b)   # tôi quên dạng này để làm gì, chia lấy nguyên phải không?
print(a ** b)
print(a % b)

False
""
[]
()
{}
0
0.0

cast_int = int("123")
cast_str = str("string")
cast_float = float("15.0")
cast_bool = bool("0")

price = 1234567.891
rate = 0.8567
test_id = 42

print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{rate:.2%}")
price(f"{test_id:04d}")
# Nhớ < căn trái, > căn phải, ^ căn giữa nhưng không nhớ cú pháp chính xác

