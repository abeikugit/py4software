# Isaac Banson Botwe
# Assignment


#!/usr/bin/python3
def decimal_to_binary():
    
    number = input("Input a decimal number   ")
    copy = number
    number = int(number)
    bin_list = []
    while number > 0 :
        num = number % 2
        bin_list.append(num)
        number //= 2
    bin_list.reverse()
    print("The binary equivalence of", copy,  "is: ")
    for i in bin_list :
        print(i, end="")

decimal_to_binary();
    
# Question 2:

# Python code to convert binary to decimal
def binToDec(bin_value):
    
    # converting binary to decimal
    decimal_value = 0
    count = 0
    
    while(bin_value != 0):
        digit = bin_value % 10
        decimal_value = decimal_value + digit * pow(2, count)
        bin_value = bin_value//10
        count += 1

    # returning the result        
    return decimal_value

# main code
if __name__ == '__main__':
    binary = int(input("Enter a binary value: "))
    print("decimal of binary ", binary, " is: ", binToDec(binary))




