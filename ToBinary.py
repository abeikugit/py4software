#!/usr/bin/python3

"""
Tobinary.py
python 3 piece of code to convert binary to decimal and decimal to python.
"""


def decimal_to_binary(value):
    """
        How to convert a decimal value to binary format
        Eg.
        print(decimal_to_binary(39))
    """
    # return bin(value).replace('0b', "")
    number = int(value)
    bin_list = []
    while number > 0:
        num = number % 2
        bin_list.append(num)
        number //= 2
    bin_list.reverse()
    res = [str(i) for i in bin_list]
    return "".join(res)


def binary_to_decimal(value):
    """
        How to convert a binary value to decimal format
        Eg.
        print(binary_to_decimal(100110))
    """
    # return int(str(value), 2)
    value = int(value)
    res = 0
    i = 1
    while value != 0:
        rem = value % 10
        res = res + (rem*i)
        i = i*2
        value = int(value/10)
    return res


number = input("Input a decimal number : ")
print(decimal_to_binary(number))
number = input("Input a binary number : ")
print(binary_to_decimal(number))

"""
Example on using above functions.
number = input("Input a decimal number")
print(decimal_to_binary(number))
number = input("Input a binary number")
print(binary_to_decimal(number))
"""