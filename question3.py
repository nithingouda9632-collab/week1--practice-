text = input("Enter text: ")

upper = 0
lower = 0
digits = 0
spaces = 0
other = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        other += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other Characters:", other)