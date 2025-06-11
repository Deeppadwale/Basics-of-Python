email = "Deeppadwale.2001@example.com"
domain = email[0] +         email[email.index(".") + 1] +           email[email.index("@") + 1:]


 # Slicing from just after '@' to the end
print("Email domain is:", domain)


# #  1. Basic Slicing

text = "PythonProgramming"
print(text[0:6])  # Output: Python


# #  2. Slicing with Omitted Start or Stop

text = "PythonProgramming"
print(text[:6])   # Output: Python (start defaults to 0)
print(text[6:])   # Output: Programming (stop defaults to end)


# #  3. Slicing with Step

text = "123456789"
print(text[::2])  # Output: 13579 (every 2nd character)

# # 4. Negative Index Slicing

text = "HelloWorld"
print(text[-5:])  # Output: World
print(text[-10:-5])  # Output: Hello

# #  5. Reversing a String
text = "Python"
print(text[::-1])  # Output: nohtyP

# 6. Real-World Examples

filename = "report.pdf"
ext = filename[-3:]
print("File extension:", ext)  # Output: pdf

#  Extract Last 4 Digits of Phone Number
phone = "9876543210"
print("Last 4 digits:", phone[-4:])  # Output: 3210

# # Get Initials from Name

name = "John Doe"
initials = name[0] + name[name.index(" ") + 1]
print("Initials:", initials)  # Output: JD


#  Get Year from Date
date = "2025-06-10"
year = date[:4]
print("Year:", year)  # Output: 2025


# F-Strings

price={1000}
account=f"all the account is handle price:{1000}"
print(account)
print(type(price))


# upper cases 

a = "deep padwale !"
print (a.upper())

b = "Deep padwale"
print (b.lower())

c="  deep ,padwale "
print(c.strip())

