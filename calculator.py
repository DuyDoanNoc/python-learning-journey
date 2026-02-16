print("=== SIMPLE CALCULATOR ===")
print()

# Addition
num1 = 10
num2 = 5
result = num1 + num2
print(num1, "+", num2, "=", result)

# Subtraction
result = num1 - num2
print(num1, "-", num2, "=", result)

# Multiplication
result = num1 * num2
print(num1, "*", num2, "=", result)

# Division
result = num1 / num2
print(num1, "/", num2, "=", result)

# Power
result = num1 ** 2
print(num1, "^ 2 =", result)

print()
print("=== DEBT CALCULATOR ===")
debt = 615 # million VND
monthly_interest = debt * 0.09 / 12 # 9% per year
print("Total debt:", debt, "million")
print("Monthly interest:", round(monthly_interest, 2), "million") # round to only print 2 number behind the dot

print()
print("=== SAVINGS PROJECTION ===")
monthly_save = 6.4
months = 12
total_saved = monthly_save * months
print("Save", monthly_save, "million/month")
print("After", months, "months:", round(total_saved, 2), "million")