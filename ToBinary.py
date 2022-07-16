# Isaac Banson Botwe
# Assignment

# Function Binary to Decimal number
from builtins import int

def binaryToDecimal(val):
    return int(val, 2)


if __name__ == '__main__':
    print(binaryToDecimal('100'))
    print(binaryToDecimal('101'))
    print(binaryToDecimal('1001'))


# Function to convert Decimal to Binary

def decimalToBinary(ip_val):
    if ip_val >= 1:
        # recursive function call
        decimalToBinary(ip_val // 2)

    # printing remainder from each function call
    print(ip_val % 2, end='')



if __name__ == '__main__':
    # decimal value
    ip_val = int(input("enter your number  "))

    # Calling special function
    decimalToBinary(ip_val)
