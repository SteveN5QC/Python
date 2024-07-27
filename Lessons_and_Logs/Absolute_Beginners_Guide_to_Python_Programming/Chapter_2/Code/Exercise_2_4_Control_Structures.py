# Exercise_2_4_Control_Structures

startnum = input("Please enter a number")

working_num = float(startnum)

# If the number is positive say so. if working_num .gt. 0 print "Your number is positive."
if working_num > 0:
    print("Your number is positive.")

# Else if the number is zero say so.  if working_num .eq. 0 print "Your number is zero."
elif working_num == 0:
    print("Your number is zero.")

# Else (the only remaining option) say the number is negative.  print "Your number is negative."
else:
    print("Your number is negative.")



"""
Exercise 4: Control Structures 
Description: 
Practice using control structures to make decisions in your code. In this exercise, you will write a script that asks the user for a number and checks if the number is positive, negative, or zero, printing an appropriate message for each case. 
Task: 
Write a script that asks the user for a number and checks if the number is positive, negative, or zero, printing an appropriate message for each case. 

"""