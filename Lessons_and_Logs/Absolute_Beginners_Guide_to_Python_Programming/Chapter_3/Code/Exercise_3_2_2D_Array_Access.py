# Exercise_3_2_2D Array Access 

# Task: Create a 3x3 matrix and print each element using nested loops.

first_row = ["A", "B", "C"]
second_row = ["D", "E", "F"]
third_row = ["G", "H", "I"]

matrix = [first_row, second_row, third_row]



# Iterate over each row -- printing row number and contents

for row_number, row in enumerate(matrix):
    print(f"Row {row_number + 1} contains:")
    
    # Iterate over row contents
    for element in row:
        print(f" {element}")

print()  # Print a new line for readibility



"""

Steve’s Working Draft Workflow:  
•	Document the Problem
•	Develop or Understand a Logic Narrative
•	Develop Psudo Code
•	Code
•	Test and Debug


 Exercise 2:  2D Array Access 

Description: 
Learn to work with multi-dimensional arrays (lists of lists) by creating a 3x3 matrix and accessing its elements using nested loops. This exercise will enhance your understanding of how to iterate over complex data structures. 
 
Task: 
Create a 3x3 matrix and print each element using nested loops. 




"""