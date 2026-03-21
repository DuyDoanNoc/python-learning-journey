price = 19.99
scientific = 3.14e2
tiny = 1.5e-3

print(0.1 + 0.2 == 0.3) # False, vì số thập phân của máy tính được lưu dưới dạng nhị phân mà máy tính chỉ lưu được 64 bit (hữu hạn) nên thường bị làm tròn và trả về kết quả sai. Và có thể sử dụng cách bên dưới để đưa ra đáp án đúng

# dùng math
import math
print(math.isclose(0.1 + 0.2, 0.3)) # True

# hoặc dùng round()
print(round(0.1 + 0.2, 1) == 0.3)   # True

# Khi cần chính xác tuyệt đối (tiền, tài chính) -> dùng Decimal
from decimal import Decimal
price = Decimal("19.99")
tax = Decimal("0.1")
price(price * tax)  # 1.999 (chính xác) != 1.9989999999999999 nếu không dùng cách này

print(float('inf'))     # Dương vô cùng
print(float('-inf'))    # Âm vô cùng
print(float('nan'))     # Not a number