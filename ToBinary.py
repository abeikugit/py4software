
#
# Mozu Agyaben Emmanuel
# BT/SEG/21/008
# QUESTION 3 

print("\nQuestion 3.")
digit = input("Please enter a decimal value:>")
copy = digit
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

print("\nQuestion 2.")
# 2. create a program to accept the name of a user and display the name only if it is Palindrome1
user_name = input("Enter your name: ")
new_name = user_name[::-1]
if user_name == new_name:print("Palindrome : ", user_name)

