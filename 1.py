# Công thức tính diện tích hình tròn
ban_kinh = 7
dien_tich = 3.14 * ban_kinh
print(dien_tich)

# Công thức tính BMI
weight = 70
height = 1.75
Tinh_BMI = weight * (height ** 2)
print(Tinh_BMI)

# Công thức đổi độ C sang độ F
c_degrees = 37
f_degrees = c_degrees * 9/5 + 32
print(f_degrees)


# 5 biểu thức dùng and, or, not
a = 10
b = 15
c = 0
d = "vodanghocbai"
print((a == 10 and b < 20) or (c != 0))                     # True
print((a != 10) or ((b == 15) and ("vodang" not in d)))     # False
print((a == 10) or ((b != 10) and ("vodang" in d)))         # True
print((a >= 10 and b <= 20) or (c != d))                    # True
print((a == 20) or (b >= 10) or ("f" not in d))             # True

# Thử "==" và "is" với list
a = [2, 100, "abc", 500, "cba"]
b = [2, 100, "abc", 500, "cba"]
c = a

print(a == b)
print(a is c)
print("abc" is c)