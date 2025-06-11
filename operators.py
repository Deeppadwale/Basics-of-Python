# Operators in Python

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")
print(f"a // b = {a // b}")
print()

# Comparison Operators
print("Comparison Operators:")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")
print()

# Logical Operators
x = True
y = False
print("Logical Operators:")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")
print()

# Assignment Operators
c = 5
print("Assignment Operators:")
c += 2
print(f"c += 2: {c}")
c -= 1
print(f"c -= 1: {c}")
c *= 3
print(f"c *= 3: {c}")
c /= 2
print(f"c /= 2: {c}")
c %= 3
print(f"c %= 3: {c}")
print()

# Bitwise Operators
d = 6  # binary: 110
e = 3  # binary: 011
print("Bitwise Operators:")
print(f"d & e = {d & e}")  # 110 & 011 = 010 -> 2
print(f"d | e = {d | e}")  # 110 | 011 = 111 -> 7
print(f"d ^ e = {d ^ e}")  # 110 ^ 011 = 101 -> 5
print(f"~d = {~d}")        # ~110 = -(110 + 1) -> -7
print(f"d << 1 = {d << 1}") # 110 << 1 = 1100 -> 12
print(f"d >> 1 = {d >> 1}") # 110 >> 1 = 011 -> 3
print()

# Identity Operators
print("Identity Operators:")
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")
print()

# Membership Operators
lst = [1, 2, 3, 10]
print("Membership Operators:")
print(f"10 in lst: {10 in lst}")
print(f"5 not in lst: {5 not in lst}")

a=0
print (f"all the data is set {a}")
print ("all the data is set ",a) 


