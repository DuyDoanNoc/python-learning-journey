# Variables
name = "Tester"
age = 28
salary = 15.5 # million
is_active = True # still working

# Python allows assign multiple variables at the same time
x, y, z = 1, 2, 3
a = b = c = 0       # assign 0 for 3 variables at the same time

del x # delete variable

# Rules_name_a_variable 
"""
- Only start with 'text' and '_'
- Only including 'text', 'number', '_'
- Uppercase differs lowercase
- Do not use Python keyword such as 'class', 'for', 'if' but can use 'my_class'
"""

# Convention of variable
"""
snake_case for variables and define
    test_result = 'Pass'
    max_retry_count = 3
UPPER_SNAKE_CASE for CONTAINS
    BASE_URL = 'https://strongtie.com'
    TIMEOUT = 30
"""

# INTERGER
"""
count = 100
negative = -50
big_number = 1_000_000  # use '_' to easy to read, Python will ignore it

# Python always support big interger
    huge = 10 ** 100    # 10^100, still exact

# Difference styles
    binary = 0b1010     # nhị phân = 10
    octal = 0o16        # bát phân = 15
    hexa = 0xFF         # thập lục phân = 255

# Way how to check type of interger
    type(count)
    print(type(count))              # <class 'int'>
    print(isinstance(count, int))   # True
"""
count = 100
type(count)
print(type(count))
print(isinstance(count, int))