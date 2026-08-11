
text = input("Enter text: ")


uppercase_count = 0
lowercase_count = 0
digits_count = 0
spaces_count = 0
others_count = 0


for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char == ' ':
        spaces_count += 1
    else:
        others_count += 1


print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
print(f"Digits: {digits_count}")
print(f"Spaces: {spaces_count}")
print(f"Other Characters: {others_count}")