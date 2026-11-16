# Number Converter
# A simple Python program to convert a decimal number to binary and hexadecimal

def main():
    print("Number Converter")
    user_input = input("Enter a decimal number: ")
    
    # Convert input string to an integer
    number = int(user_input)
    
    # Built-in conversions
    binary_value = bin(number)
    hex_value = hex(number)
    
    print("Decimal:", number)
    print("Binary:", binary_value)
    print("Hexadecimal:", hex_value)

if __name__ == "__main__":
    main()
