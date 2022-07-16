
# FUNCTION: Convert decimal to binary
def toBinary():
    Value = input("Enter decimal number >> : ") #Take user input
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
print("********************************************************")
toBinary()
print()


def bi_to_decimal(val):
   
    # Convert a binary value to decimal
    val = int(val)
    rs = 0
    j = 1
    while val != 0:
        rem = val % 10
        rs = rs + (rem*j)
        j = j*2
        val = int(val/10)
    return rs
number = input("Enter binary number here >>: ")
print("The equivqlence of ",number,"is :",bi_to_decimal(number))
print("********************************************************")
