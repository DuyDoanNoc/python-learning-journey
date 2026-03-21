# ==== Type Casting ====
# Ép kiểu (explicit)
age = int("25")     # 25
# int("abc")        # ValueError
# int("25.5")       # ValueError    # Phải chuyển từ string > float > int như bên dưới mới không có lỗi 

age_from_float = int(float("25.5"))     # 25 (cắt phần thập phân)

# str > float
price = float("19.99")          # 19.99
also_float = float("100")       # 100.0

# number > str
text = str(100)         # "100"
text2 = str(3.14)       # "3.14"
text3 = str(True)       # "True"

# number > bool
print(bool(0))          # False
print(bool(1))          # True
print(bool(-1))         # True (bất kì số khác 0 đều trả về True)

# str > bool
print(bool(""))         # False
print(bool("False"))    # True  # Vì không rỗng nên kết quả là True

# Ép kiểu ngầm (Implicit)
# Python tự ép kiểu trong một số trường hợp

print(1 + 2.0)              # 3.0 (int + float >> float)
print(True + 5)             # 6 (bool >> int)   # Vì bool là subclass of int nên True = 1
print("age: " + str(25))    # age: 25   # Vì đã ép thủ công

# Cách kiểm tra kiểu an toàn
value = "123"
if isinstance(value, str) and value.isdigit():
    number = int(value)
    print(f"Converted: {number}")

"""
# isinstance(value, str): đảm bảo value đúng là chuỗi.
# # value.isdigit(): trả về True nếu tất cả ký tự trong chuỗi là chữ số.
"""

"""
Từ  >>  Đến     Hàm         Ví dụ           Kết quả         Lỗi có thể

str >> int      int()       int("42")       42              ValueError nếu không phải số
str >> float    float()     float("3.14)"   3.14            ValueError
int >> str      str()       str(42)         "42"            Không
float >> int    int()       int(3.7)        3               Cắt phần thập phân (Không làm tròn)
any >> bool     bool        bool(0)         False           Không
list >> set     set()       set([1,1,2])    {1, 2}          Không
str >> list     list()      list("abc")     ['a', 'b', 'c'] Không
"""

# ==== F-string ====

name = "Tester"
age = 28
print(f"Name: {name}, Age: {age}")      # Name: Tester, Age: 28

# Biểu thức trong {}
print(f"Next year: {age + 1}")
print(f"Uppercase: {name.upper()}")
print(f"Length: {len(name)}")

# Định dạng số
price = 1234567.891

# Số thập phân
print(f"Price: {price:.2f}")        # Price: 1234567.89         # Lấy 2 chữ số sau thập phân
print(f"Price: {price:.0f}")        # Price: 1234567            # Bỏ phần thập phân

# Dấu phân cách hàng nghìn
print(f"Price: {price:,.2f}")       # Price: 1,234,567.89
print(f"Price: {price:_.2f}")       # Price: 1_234_567.89

# Phần trăm
ratio = 0.856
print(f"Pass rate: {ratio:.1%}")    # Pass rate: 85.6%          # Lấy giá trị hiện tại nhân 100
print(f"Pass rate: {ratio:.0%}")    # Pass rate: 86%            # Làm tròn lên

# === Padding / Căn chỉnh ===
"""
Cú pháp: {value:fill align width type}

    fill → ký tự dùng để lấp khoảng trống
    align → < trái, > phải, ^ giữa
    width → tổng độ rộng
    type → chỉ dành cho số (d, f, x, b…)
        → với string, không có type
        → default: space ' '
        → Int thập phân: {x:d}
        → Nhị phân/hex: {x:b}, {x:x} (thêm # nếu muốn 0b/0x)
        → Float cố định: {x:.2f}
        → Khoa học: {x:.3e}
        → Phần trăm: {ratio:.1%}
        → Nhóm nghìn: {x:,d} hoặc {x:,.2f}
        → Căn lề & padding: {:*^10}, {:0>8d}, {:>10.2f}
"""

# Padding interger
num = 42
print(f"{num:05d}")                 # 00042         # print ra tổng 5 ký tự     # padding 0
print(f"{num:>10d}")                # '        42'  # print ra 10 ký tự         # '>' căn phải num
print(f"{num:<10d}")                # '42        '  # print ra 10 ký tự         # '<' căn trái num
print(f"{num:^10d}")                # '    42    '  # print ra 10 ký tự         # '^' căn giữa num

# Padding string
status = "PASS"
print(f"|{status:<10}|")            # |PASS      |  # căn trái
print(f"|{status:>10}|")            # |      PASS|  # căn phải
print(f"|{status:^10}|")            # |   PASS   |  # căn giữa
print(f"|{status:*^10}|")           # |***PASS***|  # căn giữa, fill *

# Áp dụng vào Testing
test_name = "Login Test"
actual = 401
expected = 200
result = "FAIL"

# Log message
print(f"[{result:^6}] {test_name:<20} | Expected: {expected} | Actual: {actual}")
# [FAIL  ] Login Test            | Expected: 200 | Actual: 401

# == Nâng cao ==
# In ra cả giá trị trong {}
print(f"Dict syntax: {{'key': 'value'}}")       # Dict syntax: {'key': 'value'}

# Multi-line f-string
report = (
    f"Test: {test_name}\n"
    f"Result: {result}\n"
    f"Details: Expected {expected}, got {actual}"
)
print(report)

# Debug mode - In cả tên biến
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")        # x=10, y=20, x+y=30'



# ==== Data type ===
# List
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]     # cho phép nhiều kiểu
nested = [[1, 2], [3, 4], [5, 6]]       # list lồng list
from_range = list(range(1, 11))         # [1, 2, 3, ..., 10]
from_string = list("hello")             # ['h', 'e', 'l', 'l', 'o']

# Indexing (truy cập)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#           0          1        2        3           4
#           -5         -4       -3       -2          -1

print(fruits[0])    # "apple"
print(fruits[-1])   # "elderberry" (item cuối cùng)
print(fruits[-2])   # "date" (kế cuối)

# Slicing (cắt) -   list[start:stop:step]
print(fruits[1:3])      # ["banana", "cherry"]  (index 1 đến 2)
print(fruits[:3])       # ["apple", "banana", "cherry"] (từ đầu đến index 2)
print(fruits[2:])       # ["cherry", "date", "elderberry"] (từ index 2 đến hết)
print(fruits[::2])      # ["apple", "cherry", "elderberry"] (mỗi phần tử thứ 2)
print(fruits[::-1])     # đảo ngược list

# slicing tạo bản sao (shallow copy)
copy = fruits[:]        # copy riêng, sửa copy không ảnh hưởng fruits

# thêm phần tử
fruits.append("fig")                # Thêm "fig" vào cuối list
fruits.insert(1, "blueberry")       # Chèn "blueberry" vào vị trí index 1
fruits.extend(["grape", "kiwi"])    # Nối thêm nhiều phần tử vào cuối list
# Hoặc fruits += ["grape", "kiwi"]

# Xóa phần tử
fruits.remove("banana")         # Xóa phần tử đầu tiên có giá trị "banana" (ValueError nếu không có)
popped = fruits.pop()           # Xóa và trả về phần tử cuối
popped2 = fruits.pop(0)         # Xóa và trả về phần tử tại index 0
del fruits[1]                   # Xóa phần tử tại index 1 (không trả về)
fruits.clear()                  # Xóa tất cả

# Tìm kiếm phần tử
nums = [10, 20, 30, 20, 40]
print(20 in nums)               # True
print(nums.index(20))           # 1 (vị trí đầu tiên, ValueError nếu không có)
print(nums.count(20))           # 2 (đếm số lần xuất hiện)

# Sắp xếp phần tử
scores = [85, 92, 78, 95, 88]
scores.sort()                   # Sắp xếp tại chỗ (thay đổi list gốc): [78, 85, 88, 92, 95]
scores.sort(reverse=True)       # Giảm dần: [95, 92, 88, 85, 78]
sorted_scores = sorted(scores)  # Tạo list mới đã sắp xếp (không đổi list gốc)

# Sắp xếp theo tiêu chí tùy chỉnh
names = ["Charlie", "Alice", "Bob"]
name.sort(key=len)              # Sắp xếp theo độ dài: ["Bob", "Alice", "Charlie"]
names.sort(key=str.lower)       # ['Alice', 'Bob', 'Charlie']   # chuyển tất cả giá trị thành chữ thường theo thứ tự ASCII "A" < "B" < "a" < "b", sau đó sắp xếp lại và trả về kết quả 

# Các hàm hữu ích
nums = [10, 20, 30, 40, 50]
print(len(nums))        # 5     # tổng độ dài của list
print(sum(nums))        # 150   # tổng giá trị của nums
print(min(nums))        # 10    # lấy giá trị nhỏ nhất
print(max(nums))        # 50    # lấy giá trị lớn nhất

# enumerate - lặp với index (rất hay dùng)
for i, num in enumerate(nums):
    print(f"Index {i}: {num}")

# zip - ghép nhiều list lại
names = ["TC001", "TC002", "TC003"]
results = ["PASS", "FAIL", "PASS"]
for name, result in zip(names, results):
    print(f"{name}: {results}")

"""
TC001: ['PASS', 'FAIL', 'PASS']
TC002: ['PASS', 'FAIL', 'PASS']
TC003: ['PASS', 'FAIL', 'PASS']
"""

# List Comprehension (Tạo list ngắn gọn)
# Cú pháp: [biểu_thức for biến in iterable if điều_kiện]

squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

even_nums = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Ứng dụng testing: lọc TC failed
all_results = [
    {"name": "TC001", "status": "PASS"},
    {"name": "TC002", "status": "FAIL"},
    {"name": "TC003", "status": "PASS"},
    {"name": "TC004", "status": "FAIL"}
]
failed = [tc["name"] for tc in all_results if tc["status"] == "FAIL"]
# ["TC002", "TC004"]


# ==== LƯU Ý QUAN TRỌNG VỀ LIST ====
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()           # hoặc original[:] hoặc list(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print(shallow[0][0])        # 99    # shallow chỉ copy tham chiếu của original nên khi original thay đổi, shallow bị ảnh hưởng
print(deep[0][0])           # 1     # deep copy và tạo bản sao hoàn toàn, và không bị ảnh hưởng khi original thay đổi

# Tránh lỗi phổ biến: thay đổi list trong khi đang lặp
nums = [1, 2, 3, 4, 5]
# SAI
for n in nums:
    if n % 2 == 0:
        nums.remove(n)      # kết quả không đoán được!
"""
Khi bạn remove(2), danh sách bị co lại:

[1, 3, 4, 5]

Phần tử 3 bị trượt lên vị trí của 2, nhưng vòng lặp đã tăng chỉ số → thế là 3 bị bỏ qua.

Kết quả có thể không như mong đợi (đặc biệt nếu dữ liệu phức tạp hơn).
"""

# ĐÚNG (List Comprehension)
nums = [n for n in nums if n % 2 != 0]

# Default mutable argument
# Sai - list mặc định được share giữa các lần gọi
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))      # [1]
print(add_item(2))      # [1, 2]    
"""
Expected result nên là [2] thay vì [1, 2] nhưng với python thì Default argument được evaluate một lần duy nhất khi:
    - Hàm được định nghĩa
    - Không phải khi hàm được gọi
""" 

# Đúng
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

"""
Vì sao cách này đúng?
None là immutable (bất biến) và an toàn
Mỗi lần gọi nếu không truyền lst thì list mới (lst = []) được tạo bên trong hàm

Diễn biến:

1.  add_item(1)
    lst là None → tạo []
    append → [1]

2.  add_item(2)
    lst là None → tạo []
    append → [2]
>> Không còn bị share nữa.
"""