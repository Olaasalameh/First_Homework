def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            return None  # Invalid binary number
        power -= 1
    return decimal

# Read binary number from user, handle input errors
while True:
    binary = input("Enter a binary number: ")
    if set(binary) <= {'0', '1'}:  # Check if input contains only '0' and '1'
        break
    else:
        print("Invalid input! Please enter a binary number containing only 0s and 1s.")

# Convert binary to decimal
decimal = binary_to_decimal(binary)

if decimal is not None:
    print("The equivalent decimal number is:", decimal)
else:
    print("Invalid binary number entered!")
