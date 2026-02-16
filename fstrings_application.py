print("=== F-STRINGS - MY INFO ===")
print()

# My variables
first_name = "Duy"
last_name = "Doan"
age = 29
city = "Ho Chi Minh"
country = "Vietnam"

current_job = "Manual Tester"
current_salary = 25 #million VND
company = "Simpson Strong-Tie"

dream_job = "Automation tester "
target_salary = 1500 # USD per month
target_vnd = target_salary * 25 # Convert to VND
months_to_goal = 12

# Introduction using f-strings
intro = f"""
{'='*50}
    PROFESSIONAL PROPFILE
{'='*50}
Name: {first_name} {last_name}
Age: {age} years old
Location: {city}, {country}

CURRENT POSITION:
- Company: {company}
- Role: {current_job}
- Salary: {current_salary} million VND/month

GOAL (12 months):
- Target Role: {dream_job}
- Target Salary: ${target_salary} USD/month ({target_vnd:.0f} million VND)
- Increase: {target_vnd - current_salary:.0f} million VND/month

COMMITMENT:
I am studing {2 * months_to_goal} hours per month
for {months_to_goal} months to achieve this goal.

{'='*50}
"""

print(intro)

# Progress calculation
days_passed = 2
days_total = 365
progress = (days_passed / days_total) * 100

print(f"\n PROGRESS UPDATE:")
print(f"Days into juorney: {days_passed}/{days_total}")
print(f"Progress: {progress:.2f}%")
print(f"Days remaining: {days_total - days_passed}")
print(f"\nLet's keep going!\n")