# MID-SEMESTER 
#EMMANUEL AGYABEN MOZU
#BT/SEG/21/008



#convrt numbers to binary
from ast import Pass


def number_to_binary(digit):
    digit = int(digit)
    bin_list = []
    while digit > 0 :
        cast = digit % 2
        bin_list.append(cast)
        digit //= 2
    bin_list.reverse()
    print(" Binary equivalence of", copy,  "is: ")
    for i in bin_list :
        print(i, end="") 

#convrt binary to number 
def binary_to_number():
        number = int(value)
        bin_list = []
        while number > 0:
            num = number % 2
            bin_list.append(num)
            number //= 2
        bin_list.reverse()
        res = [str(i) for i in bin_list]
        return "".join(res)




digit = input("Please enter a decimal value:>")
binary_to_number(digit)

digit = input("Please enter a binary value:>")
binary_to_number(digit)