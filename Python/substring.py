main_string = "Hello, this is a sample string containing some text."
substring = "sample"
index = main_string.find(substring)
if index != -1:
    print(f"'{substring}' found at index {index}")
else:
    print(f"'{substring}' not found")

try:
    index = main_string.index(substring)
    print(f"'{substring}' found at index {index}")
except ValueError:
    print(f"'{substring}' not found")
