# Exercise_3_5_For_Loop_Practice

# Write a for loop to print the first 10 numbers in the Fibonacci sequence

"""
In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2. Starting from 0 and 1, the sequence begins[1]

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....

    num_a is the first number
    num_b is the second number

    loop_index goes from 1 - 10 for the exercise

    initialize the variables

    Print "The first 10 numbers in the Fibonacci sequence are:"

    for loop_index from 1 - 10
        Print num_a
        num_next = num_a + num_b
        num_a = num_b
        num_b = num_next

    Expected Output:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34

"""
# Initialize the variables

num_a = 0
num_b = 1

# Print the initial line

print("The first 10 numbers in the Fibonacci sequence are:")


# NOTE:  This loop ends BEFORE 11 -- AKA After 10!

for loop_index in range(1, 11):
        print(num_a)
        num_next = num_a + num_b
        num_a = num_b
        num_b = num_next

"""
Actual Output:
C:\Users\N5QC\Documents\Repositories\Python\Lessons_and_Logs\Absolute_Beginners_Guide_to_Python_Programming\Chapter_3\Code> python Exercise_3_5_For_Loop_Practice.py
The first 10 numbers in the Fibonacci sequence are:
0
1
1
2
3
5
8
13
21
34
PS C:\Users\N5QC\Documents\Repositories\Python\Lessons_and_Logs\Absolute_Beginners_Guide_to_Python_Programming\Chapter_3\Code>

Steve’s Working Draft Workflow:  
•	Document the Problem
•	Develop or Understand a Logic Narrative
•	Develop Psudo Code
•	Code
•	Test and Debug


Exercise 5:  For Loop Practice 

Description: 
Gain experience with for loops by writing a loop that generates the first 10 numbers in the Fibonacci sequence. This exercise will enhance your understanding of iterative processes and sequence generation. 

 
Task: 
Write a for loop to print the first 10 numbers in the Fibonacci sequence
 




"""