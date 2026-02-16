# String methods from LinkIn Learning
message = "Python for Automation"

# Method 1: strip() - remove whitespace
clean = message.strip()
print("Original:", message)
print("Cleaned:", clean)

# Method 2: lower() - lower case
lower = clean.lower()
print("Lowercase:", lower)

# Method 3: upper() - uppercase
upper = clean.upper()
print("Uppercase:", upper)

# Method 4: title() - Title Case
title = clean.title()
print("Title:", title)

# Method 5: title() - swap text
replaced = clean.replace("Automation", "Testing")
print("Replaced:", replaced)

# Method 6: find() - find position
position = clean.find("Automation")
print("Position:", position)

# String formatting from LinkedIn

# Old way: % formatting (instructor might show)
name = "Duy"
age = 29
print("My name is %s and I'm %d year old" % (name, age))

# Better way: .format()
print("My name is {} and I'm {} years old".format(name, age))

# BEST way: f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age} years old")

# F-strings with expressions
current_salary = 25
target_salary = 37.5
print(f"Current: {current_salary}M, Target: {target_salary}M")
print(f"Need to increase: {target_salary - current_salary}M")

# F-strings with formatting
pi = 3.1459265
print(f"Pi = {pi:.2f}") # 2 decimal places

# Multi-line f-strings
message = f"""
Hello, my name is {name}.
I am {age} years old.
I am learning Python for automation testing
"""
print(message)