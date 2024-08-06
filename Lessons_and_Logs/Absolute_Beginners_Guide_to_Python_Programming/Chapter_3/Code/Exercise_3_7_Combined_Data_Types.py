# Exercise_3_7_Combined_Data_Types

# Task: 
# Create a list of dictionaries, where each dictionary represents a student with keys for name and grade.
# Print each student's name and grade using a loop.

"""
Dictionaries
student_1 Alice A --> student_1 = {"name": "Alice", "grade": "A"}
student_2 Bob B --> student_2 = {"name": "Bob", "grade": "B"}
student_3 Carla C --> student_3 = {"name": "Carla", "grade": "C"}
student_4 Dave D --> student_4 = {"name": "Dave", "grade": "D"}
student_5 Fred F --> student_5 = {"name": "Fred", "grade": "F"}
student_6 Irene I --> student_6 = {"name": "Irene", "grade": "I"}

List of Dictionaries
grade_list = [student_1, student_2, student_3, student_4, student_5, student_6]


"""

# Initialize Student Dictionaries

student_1 = {"name": "Alice", "grade": "A"}
student_2 = {"name": "Bob", "grade": "B"}
student_3 = {"name": "Carla", "grade": "C"}
student_4 = {"name": "Dave", "grade": "D"}
student_5 = {"name": "Fred", "grade": "F"}
student_6 = {"name": "Irene", "grade": "I"}

# Create the List of Dictionaries

grade_list = [student_1, student_2, student_3, student_4, student_5, student_6]


i = 0

while i < len(grade_list):
    print(grade_list[i])
    i = i + 1




"""

Steve’s Working Draft Workflow:  
•	Document the Problem
•	Develop or Understand a Logic Narrative
•	Develop Psudo Code
•	Code
•	Test and Debug


Exercise 7:  Combined Data Types
Description: 
Learn to work with combined data types by creating a list of dictionaries. Each dictionary will represent a student with keys for name and grade. You will print each student's name and grade using a loop. 
 
Task: 
Create a list of dictionaries, where each dictionary represents a student with keys for name and grade. Print each student's name and grade using a loop.

"""