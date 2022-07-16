# ToBinary
python 3 piece of code to convert binary to decimal and decimal to python.

## to convert x decimal value to binary
use the 'decimal_to_binary' function and pass in your value as a parameter. 
" decimal_to_binary(x) "

## to convert x binary value to decimal
use the 'binary_to_decimal' function and pass in your value as a parameter. 
"binary_to_decimal(x)"

Decimal to binary
The function decimalToBinary() takes an argument that is a decimal number and repeatedly divides it by 2.
The while loop checks if the decimal number is greater than 0. If true, the program flow goes inside the loop.
Using the built-in modulo operator, %, the remainder is extracted and appended to the right-hand end of the string.
bin_list.reverse() wil print the array in reverse order.
After the division process reaches 0, a binary string is constructed
The upper steps keep repeating till binary > 0 then the output(binary number) gets printed.


Binary to decimal
With user input 10110:
A user-defined function called binaryToDecimal takes an argument "number" 
The string method str() will convert the number  to a string type  and the length method, len(), will find the length of the string. 
Using "for loop", the range method, range(), will take the length of the string(that is, the number(10110) that has been converted to a string) and will return a sequence of values from 0 to one less than the value defined. 
