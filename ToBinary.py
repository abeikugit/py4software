number = input("Input a decimal number")
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
