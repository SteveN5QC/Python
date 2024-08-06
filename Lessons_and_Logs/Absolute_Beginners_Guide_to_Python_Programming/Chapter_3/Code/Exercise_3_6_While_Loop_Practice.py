# Exercise_3_6_While_Loop_Practice 

# Task: Write a while loop to reverse a string. 

# initialize the reversed string

reversed_string = ""

# Request User input of string to reverse

starting_string = input("Please type the string to reverse followed by <Enter>:  ")

i = 0

while i < len(starting_string):
    reversed_string = starting_string[i] + reversed_string
    i = i + 1

print("The input string was:  ", starting_string)  
print()
print("The reversed string is:  ", reversed_string)   

# Print Template:  print(f"Sequence place {loop_index:.0f} is {num_a:.0f}")

"""
Steve’s Working Draft Workflow:  
•	Document the Problem
•	Develop or Understand a Logic Narrative
•	Develop Psudo Code
•	Code
•	Test and Debug


Exercise 6:  While Loop Practice 

Description: 
This exercise will help you practice while loops by writing a loop to reverse a string. You will gain a better understanding of condition-based iteration and string manipulation. 

 
Task: 
Write a while loop to reverse a string. 

"""