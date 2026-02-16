# Arithmetic operators from LinkedIn Learning

print("=== ARITHMETIC OPERATORS ===")
print()

# Basic operators
print("Addition: 10 + 3 =", 10 + 3)
print("Subtraction: 10 - 3 =", 10 - 3)
print("Multiplication: 10 * 3 =", 10 * 3)
print("Division: 10 / 3 =", 10 / 3) #Float result
print()

# Special operators (LinkedIn will show these)
print("Floor Division: 10 // 3 =", 10 // 3) # Integer result
print("Modulus (remainder): 10 % 3 =", 10 % 3)
print("Exponent (power): 10 ** 3 =", 10 ** 3)
print()

# Order of operations (PEMDAS)
result = 10 + 3 * 2
print("10 + 3 * 2 =", result) # Multiplication first!

result = (10 + 3) * 2
print("(10 + 3) * 2 =", result) # Parenthese first!

print("=== COMPARISION OPERATORS ===")
print()

x = 10
y = 5

print(f"x = {x}, y = {y}")
print()
print(f"x == y: {x == y}")  # Equal
print(f"x != y: {x != y}")  # Not equal
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater or equal
print(f"x <= y: {x <= y}")  # Less or equal
print()

print("=== LOGICAL OPERATORS ===")
print()

# AND, OR, NOT
a = True
b = False

print(f"a = {a}, b = {b}")
print()
print(f"a and b: {a and b}")    # Both must be True
print(f"a or b: {a or b}")      # At least one True
print(f"not a: {not a}")        # Opposite
print()

# Practical example
current_salary = 25
target_salary = 37.5
months_studied = 2
months_needed = 12

ready = (months_studied >= months_needed) and (current_salary >= target_salary)
print(f"Am I ready? {ready}")

making_progress = (months_studied > 0) or (current_salary > 20)
print(f"Making progress? {making_progress}")