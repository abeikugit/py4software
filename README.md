# ToBinary
python 3 piece of code to convert binary to decimal and decimal to python.

## to convert x decimal value to binary
use the 'decimal_to_binary' function and pass in your value as a parameter. 
" decimal_to_binary(x) "

## to convert x binary value to decimal
use the 'binary_to_decimal' function and pass in your value as a parameter. 
"binary_to_decimal(x)"


Decimal to binary
The function decimalToBinary() takes an argument that is a decimal number and repeatedly divides it by 2.  line 1 and 7
An array, bin_list[], is declared which takes the value of the remainder in line 3.
Line 4 uses the while loop to check if the decimal number is greater than 0. If true, the program flow goes inside the loop.
Line 5 uses the built-in modulo operator, %, to extract the remainder and line 6 appends the remainder to the right-hand end of the string.
In line 8, bin_list.reverse() wil print the array in reverse order.
After the division process reaches 0, a binary string is constructed in lines 9-10.
The upper steps keep repeating till binary > 0 then the output(binary number) gets printed.


Binary to decimal
With user input 10110:
A user-defined function called binaryToDecimal was created which takes "number" as an argument. 
The string method str() will convert any type of value to a string type so in this case, 10110 will be converted to a string, and the length method len() will find the length of the string. 
Using the for loop, the range method, range(), will take the length of the string(that is, the number(10110) that has been converted to a string) and will return a sequence of values from 0 to one less than the value defined as its argument. 