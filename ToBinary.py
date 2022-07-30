#!/usr/bin/python3
#Tracy Sarah Afram-Owusu
#BT/SEG/21/007

def decimalToBinary(value):
    number = int(value)
    bin_list = []
    while number > 0:
        rem = number % 2
        bin_list.append(rem)
        number //= 2
    bin_list.reverse()
    res = [str(i) for i in bin_list]
    return "".join(res)


userInput = input("Enter a decimal number: ")
print("Its binary equivalent is: ", decimalToBinary(userInput))


def binaryToDecimal(number):
    number = int(number)
    value = 0
    i = 1
    length = len(str(number))
    for x in range(length):
        rem = number % 10
        value = value + (rem * i)
        i = i * 2
        number = int(number/10)
    return value


userInput = input("Enter a binary number: ")
print("Its decimal equivalent is: ", binaryToDecimal(userInput))
