# === STRING METHOD ===
name = 'Python'
greeting = "Hello World"

# Multiple strings
description = """
1
2
3
"""

# Raw string - bỏ qua ký tự escape, hữu ích cho regex và đường dẫn
path = r"C:\new_folder\test"    # không escape \n và \t
pattern r"\d{3}-\d{4}"  # regex pattern

# ký tự escape phổ biến
# \n = xuống dòng
# \t = tab
# \\ = dấu \
# \" = dấu "
print("Line1\nLine2")
"""
Output:
Line1
Line2
"""
print("Col1\tCol2")
"""
Output:
Col1    Col2
"""

# === CÁC THAO TÁC CHUỖI QUAN TRỌNG ===

s = "  Hello, Python World!   "
# Truy cập và Cắt (Indexing & Slicing)  
# s[start:stop:step]
print(s[2])         # 'H'               (Output là H vì có 2 spaces)
print(s[-1])        # ' '               (lấy ký tự cuối)
print(s[2:7])       # 'Hello'           (lấy ra từ index 2 đến 6)
print(s[::2])       # ' el,Pto ol! '    (Cách mỗi 2 ký tự lấy 1 lần)
print(s[::-1])      # '  !dlroW nohtyP ,olleH  ' (lấy giá trị đảo ngược của s)

# String methods thường dùng
print(s.strip())            # 'Hello, Python World!' (xóa các khoảng trống 2 đầu)
print(s.lower())            # '  hello, python world!  ' (chuyển tất cả các giá trị về in thường)
print(s.upper())            # '  HELLO, PYTHON WORLD!  ' (chuyển các giá trị về in hoa)
print(s.replace("Python", "Testing"))       # '  Hello, Testing World!  ' (Thay 'Python' bằng 'Testing')
print(s.split(","))         # ['  Hello', 'Python World!  '] (trả về 1 list ký tự bị ngắt bởi dấu phẩy)
print(s.find("Python"))     # 9 (Vị trí đầu tiên tìm thấy cụm 'Python' tức là P ở index 9, trả về -1 nếu không có)
print(s.count("l"))         # 3 (vì trong 's' có 3 lần chữ 'l' xuất hiện)

# Kiểm tra nội dung
print("Python" in s)        # True (trả về True vì có 'Python' trong s)
print(s.strip().startswith("Hello"))        # True (True là vì đã xóa khoảng trắng với strip() và chuỗi 's' bắt đầu bằng 'Hello')
print(s.strip().endswith("!"))              # True (True là vì đã xóa khoảng trắng với strip() và chuỗi 's' kết thúc bằng '!')
print("abc123".isalnum())                   # True (True là vì chuỗi chỉ chứa chữ và số A-Z, a-z, 0-9)
print("abc".isalpha())                      # True (True là vì chuỗi chỉ chứa chữ A-Z, a-z)
print("123".isdigit())                      # True (True là vì chuỗi chỉ chứa số 0-9)

# Nối chuỗi
words = ["Hello", "World"]
print(" ".join(words))                  # "Hello World" ('Hello' và 'World' được nối với nhau bằng space)
print("-".join(["2024", "01", "15"]))   # "2024-01-15" (các ký tự được nối với nhau bằng gạch ngang)

# === Bool Type ===

is_passed = True
is_failed = False

# Boolean là subclass của int
print(True + True)      # 2 (khi sử dụng toán học như + chung với True/False thì True=1, False=0)
print(False + 1)        # 1 
print(int(True))        # 1
print(int(False))       # 0

# == Các giá trị TRUTHLY và FALSY cực kỳ quan trọng ==
"""
Các giá trị FLASY (coi như false):
False
None
0
0.0
""  (chuỗi rỗng)
[]  (list rỗng)
()  (type rỗng)
{}  (dict rỗng)
set()  (set rỗng)

Tất cả các giá trị khác TRUTHY
"""

# Ứng dụng vào testing
response_body = ""
if not response_body:                   # Check xem response_body có rỗng không, đồng nghĩa là respone_body == False không.
    print("Respone body is empty")

results = [{"test": "TC001", "status": "PASS"}]
if results:                             # Check xem results có phần tử không, đồng nghĩa là result == True không.
    print(f"Got {len(results)} results")

# Chuyển đổi sang bool
print(bool(0))          # False
print(bool(42))         # True
print(bool(""))         # False
print(bool("hello"))    # True
print(bool([]))         # False
print(bool([1, 2]))     # True


# === NONE, Giá trị "Không có gì" ===

# None là kiểu riêng (NoneType), đại diện cho không có gì
result = None

# Luôn dùng 'is' để so sánh với None (Không dùng ==)
if result is None:
    print("No result yet")

if result is not None:
    print(f"Result: {result}")

# Hàm không return gì -> Trả về None
def do_something():
    return

x = do_something()  
print(x)            # None


# ==== Toán Tử ====

a, b = 17, 5

print(a + b)    # 22    Cộng
print(a - b)    # 12    Trừ
print(a * b)    # 85    Nhân
print(a / b)    # 3.4   Chia (luôn trả về float)
print(a // b)   # 3     Chia lấy phần nguyên
print(a % b)    # 2     Chia lấy phần dư (modulo)
print(a ** b)   # 1419857 Lũy thừa (17^5)

# Chú ý chia số âm
print(-17 // 5) # -4    (Python làm tròn xuống, không phải về 0)
print(-17 % 5)  # 3     (khác với nhiều ngôn ngữ khác)

# Gán kết hợp
count = 0
count += 1      # count = count + 1     # 1
count -= 1      # count = count - 1     # 0
count *= 5      # count = count * 5     # 0
# Không có ++ hay -- trong Python


# ==== Toán so sánh ====

x, y = 10, 20

print(x == y)   # False     # Bằng
print(x != y)   # True      # Không bằng
print(x > y)    # False     # Lớn hơn
print(x < y)    # True      # Nhỏ hơn
print(x >= 10)  # True      # Lớn hơn và bằng
print(x <= 10)  # True      # Nhỏ hơn và bằng

# So sánh chuỗi (theo thứ tự từ điển / Unicode)
print("apple" < "banana")   # True      # Trong bảng mã Unicode (và cũng giống như trong bảng chữ cái), 'a' có giá trị nhỏ hơn 'b'
print("A" < "a")            # True      # (A = 65, a = 97 tring ASCII)
print("abc" < "abcd")       # True      

"""
Cách so sánh diễn ra
So sánh ký tự đầu tiên: 'a' với 'a' → bằng nhau.
So sánh ký tự thứ hai: 'b' với 'b' → bằng nhau.
So sánh ký tự thứ ba: 'c' với 'c' → bằng nhau.
Đến đây, chuỗi "abc" đã hết, nhưng "abcd" vẫn còn ký tự 'd'.
"""

# So sánh chuỗi (chain comparison - đặc trưng Python)
age = 25
print(18 <= age <= 65)      # True (tương đương: 18 <= age and age <= 65)

score = 85
print(80 <= score < 90)     # True - score nằm trong khoảng (80 - 90)



# ==== Toán Logic ====

# and - True khi cả hai True
print(True and True)        # True
print(True and False)       # False

# or - True khi ít nhất một True được đáp ứng
print(True or False)    # True
print(False or False)   # False

# not - Đảo ngược
print(not True)     # False
print(not False)    # True

# Ứng dụng thực tế
username = ""
display_name = username or "Anonymous"  # Anonymous vì "" là falsy

data = {"key": "value"}
result = data and data.get("key")       # "value" sẽ được lấy ra

# Thứ tự ưu tiên: not > and > or
print(True or False and False)      # True (and chạy trước: False and False = False, rồi True or False = True)
print((True or False) and False)    # False (dùng ngoặc để thay đổi thứ tự)



# ==== IDENTITY & MEMBERSHIP ====

# IDENTITY: is / is not
# Kiểm tra 2 biến có trỏ đến cùng một đối tượng trong bộ nhớ không

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True (cùng giá trị)
print(a is b)       # False (khác đối tượng trong bộ nhớ)
print(a is b)       # True (c trỏ đến cùng đối tượng với a)

# Quy tắc vàng: chỉ dùng 'is' với None, True, False
# Dùng '==' cho mọi so sánh giá trị khác
if result is None:      # Cách viết đúng
    pass
if result == None       # Cách viết sai
    pass

# MEMBERSHIP: in / not in
# Kiểm tra phần tử có tồn tại trong collection không

browsers = ["chrome", "firefox", "edge"]
print("chrome" in browsers)         # True
print("safari" not in browsers)     # True

message = "Test case TC001 passed"
print("TC001" in message)           # True
print("FAIL" not in message)        # True

config = {"timeout": 30, "retries": 3}
print("timeout" in config)          # True (kiểm tra KEY, không phải value)
print(30 in config)                 # False (30 là value, không phải key)


# ==== Toán tử Bitwise (tham khảo) ====

a, b = 0b1100, 0b1010   # tương ứng 12 và 10

print(bin(a & b))       # 0b1000    # AND
print(bin(a | b))       # 0b1110    # OR
print(bin(a ^ b))       # 0b0110    # XOR
print(bin(~a))          # -0b1101   # NOT (đảo bit a)
print(bin(a << 2))      # 0b110000  # Dịch trái
print(bin(a >> 2))      # 0b11      # Dịch phải