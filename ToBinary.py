
# FUNCTION: Convert binary to decimal
def toBinary():
    Value = input("Enter decimal number >>> :") #Take user input
    copy = Value
    number = int(Value)
    bin_list = []
    while number > 0:
        num = number % 2
        bin_list.append(num)
        number //= 2
    bin_list.reverse()
    print("The binary equivalence of", copy, "is : ")
    for i in bin_list:
        print(i, end="")

# function to convert binary to decimal
def convertToDecimal():
    binary = input('Enter Binary Number >>> : ')
    decimal = 0
    # lenght of binary
    i = len(binary)

    # loop through the binary digit
    for x in binary:
        i = i - 1
        decimal += pow(2, 1) * int(x)
    print("Decimal of {p} is {q} ".format(p=binary, q=decimal))

toBinary()
print()

convertToDecimal()
print()
