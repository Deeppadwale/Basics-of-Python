import os

directory_path = '/python'  # Make sure this path is correct and exists

try:
    contents = os.listdir(directory_path)
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")


import pyjokes

jocks=pyjokes.get_joke()

print(f"Thise is the jocks{jocks}")

