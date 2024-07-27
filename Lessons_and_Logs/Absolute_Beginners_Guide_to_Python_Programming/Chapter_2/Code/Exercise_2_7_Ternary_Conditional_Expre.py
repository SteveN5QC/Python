# Exercise_2_7_Ternary_Conditional_Expressions

# BACKGROUND:  The operation "%" Divides the left hand number by the right hand number and returns the remainder.

# Input a number string:  input_string
input_string = input("Please enter a number ")

# Convert the string to an integer:  my_integer = int(input_string)
my_integer = int(input_string)

# Use the "%" operation: my integer % 2: test_value = my_integer % 2
test_value = my_integer % 2

# If the test_value is 0 the original number is even otherwise it is not even
if test_value == 0:
    even = True
else:
    even = False

# Print odd or even
print(f"Your number is {'even.' if even == True else 'odd.'}")

"""

Exercise 7: Ternary Conditional Expression 
Description: 
Learn to use ternary conditional expressions for concise decision-making in your code. This exercise involves writing a script that uses a ternary expression to determine whether a user’s input number is even or odd. 
Task: 
Write a script that determines whether a user’s input number is even or odd using a ternary conditional expression. 

"""