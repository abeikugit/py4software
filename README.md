Question 1:
Convert Binary to Decimal in Python
i used the built-in function in Python.

Built-in Function in Python to convert Binary to Decimal:
In Python, we can use the int() function to convert a binary to its decimal value. The int() function takes 2 arguments, a value and the base of the number to be converted, which is 2 in the case of binary numbers
I declared a function called binaryToDecimal. 
to contain the codes.


Question 2:

Decimal to Binary Conversion in Python
The easiest technique to convert the decimal numbers to their binary equivalent is the Division by 2.

In Division by 2 technique, we continuously divide a decimal number by 2 and note the reminder till we get 1 as our input value. Then we read the noted reminders in reverse order to get the final binary value.

Let’s break the earlier statements to get more clarity. Assume we have a special function that divides the input number by 2 and gives the remainder as output. For Decimal to Binary, we call this special function multiple times till we get the 1 as the input value. Then, we finally print all the saved reminders to get the final binary(base-2) value.