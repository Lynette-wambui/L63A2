number = int(input("Enter a number: "))

# Bitwise And with 1 checks the last bit
if number & 1:
    print(f"{number} is odd! 😲")
else:
    print(f"{number} is even!")