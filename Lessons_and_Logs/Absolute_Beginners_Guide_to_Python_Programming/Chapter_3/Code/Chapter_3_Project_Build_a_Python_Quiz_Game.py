# Chapter_3_Project_Build_a_Python_Quiz_Game

"""

Steve’s Working Draft Workflow:  
•	Document the Problem
•	Develop or Understand a Logic Narrative
•	Develop Psudo Code
•	Code
•	Test and Debug


3.15 Project: Build a Python Quiz Game 
 
This next project is a Quiz Game, further solidifying your understanding of collections and loops by applying these concepts in a fun, interactive way. This project tests your knowledge and encourages creative problem-solving and coding practice. 
 
Objective: 
Create an interactive quiz game that tests the player's knowledge across various topics. The game should present a series of questions, each with multiple-choice answers, and track the player's score throughout the session.” 
 
Setup Instructions Define Questions and Answers:  
Create a list of dictionaries, where each dictionary represents a quiz question, its multiple-choice options, and the correct answer. 
 
Since the focus of the project isn’t to test your creativity, I will provide you with some questions below. Use them, or don’t use them. Either works.  
 
Gameplay Flow:  
Display a welcome message to the user.  Loop through the questions. 
 
Optionally: 
You could randomly shuffle the questions to ensure a unique gameplay experience each time. To do so, you would need to import Python’s random package and then shuffle the questions. We haven’t talked about importing Python packages, so here is the code to do it:  
 
# Shuffle the questions
import random
random.shuffle(questions)  
 
Iterate through the questions, presenting each one to the user along with the answer choices.  
 
Prompt the user for their answer to each question.  
 
Scoring:  
Keep track of the user's score by incrementing it for each correct answer.  Provide immediate feedback to the user after each question, indicating whether their answer was correct or incorrect. If incorrect, display the correct answer.  
 
Ending the Game:  
 
•	Allow the user to exit the game early by typing a specific command (e.g., 'exit').  
•	Once all questions have been answered, or the user decides to exit, display the user's final score.  
 
Success Criteria:
•	The game must successfully run without errors. 
•	The user should be able to select their answer to each question and receive immediate feedback. 
•	The game should accurately track and display the user's score. 
•	The game should offer an option for the user to exit at any point. 
 
Setting Up for Success Review Collections:
•	Understand how lists and dictionaries can store quiz questions and options. 
•	Practice Loops: Familiarize yourself with for and while loops for iterating through the questions and validating user inputs. 
•	Input and Output: Get comfortable with using input() to capture user responses and print() to display messages and questions. 
 
Sample Quiz Questions 
Question 1: Who was buried in Andrew Jackson's grave? 
Options:  Donald Trump  Andrew Jackson  John Tyler  Joe Biden  
Correct Answer: Andrew Jackson
Question 2: What color was George Washington’s great white horse? 
Options:  Black  Brown  White  Green  Correct Answer: White  
Question 3: What data type is used to store items as a sequence that can maintain order? 
Options:  List  Tuple  Set  Dictionary
Correct Answer: List  
Question 4: To loop over each character in a word, which Python structure should you use? 
Options:  For loop  While loop  If statement  Print Statement  
Correct Answer: For loop  
Question 5: Which Python collection allows us to store unique items identified by a key?
Options:  List  Tuple  Set  Dictionary
Correct Answer: Dictionary  
Question 6: Which Python collection type prevents duplicates? 
Options:  List  Tuple  Set  Dictionary
Correct Answer: Set  
 
This project is designed to reinforce your understanding of Python's fundamental concepts while also providing a fun and interactive way to engage with the material. Remember, the key to success is not just completing the project but learning and experimenting with Python along the way. 
 
Example of Possible Output Welcome to the Basic Quiz Game!  
1/6: What data type is used to store items as a sequence that can maintain order?  1. List  2. Tuple  3. Set  4. Dictionary  Your answer (1-4): 1  Correct! You earned a point.  
2/6: What color was George Washington’s great white horse?  1. Black  2. Brown  3. White  4. Green  Your answer (1-4): 3  Correct! You earned a point.  
3/6: Who was buried in Andrew Jackson grave?  1. Donald Trump  2. Andrew Jackson  3. John Tyler  4. Joe Biden  Your answer (1-4): 2  Correct! You earned a point.  
4/6: Which Python collection type prevents duplicates?  1. List  2. Tuple  3. Set  4. Dictionary  Your answer (1-4): 3  Correct! You earned a point.  
5/6: To loop over each character in a word, which Python structure should you use?  1. For loop  2. While loop  3. If statement  4. Print Statement  Your answer (1-4): 1  Correct! You earned a point.  
6/6: Which Python collection allows us to store unique items identified by a key?  1. List  2. Tuple  3. Set  4. Dictionary  Your answer (1-4): 1  
 

 




"""