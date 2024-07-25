# Chapter_2_Project_Loan_Payment_Calculator

# Prompt for Basic Loan Information:  
# Ask the user to input the total loan amount for the car. 

total_loan = input("Please enter the total loan amount ($):  ")

 
# Request the annual interest rate as a percentage. 
# The user should be able to input a number like 7.5 for a 7.5% rate. 

annual_interest_rate = input("Please enter the Annual Interest Rate (%):  ")


 
# Inquire about the loan duration in years from the user.  

loan_duration = input("Please enter the Loan Duration (Years):  ")

 
# Inquire About Down Payment:  
# Ask the user if they want to include a down payment. 

is_down_payment = input("Is there a down payment (yes or no):  ")
if is_down_payment == yes:
    logical_down_payment = True

else:
    logical_down_payment = False

# To Do:  Validate / Correct Input

# If the user answers yes, prompt for the down payment amount 
# If down payment 
#    Ask for amount
#    Adjust loan amount accordingly by subtracting the down payment from the initial loan amount. 

if logical_down_payment == True:
    down_payment = input("Please enter the down paymentamount ($):  ")
    net_loan = float(total_loan) - float(down_payment)


# else use entered loan amount
else net_loan = float(total_loan)



 



 
# Calculate Monthly Payment:  
# First, check if the annual interest rate is greater than 0.  
#   If yes, convert the annual interest rate to a monthly rate and proceed with the regular loan payment calculation formula.  
#   If the interest rate is 0%, calculate the monthly payment by simply dividing the loan amount 
#      (after adjusting for any down payment) by the total number of payments (loan duration in years multiplied by 12).


 
# Use the formula to calculate the monthly payment of a loan. 
 
# The formula is:  
#    where: 
#    M is the monthly payment.  
#    P is the loan amount (principal).  
#    r is the monthly interest rate (annual interest rate divided by 12).  
#    n is the total number of payments (loan duration in years multiplied by 12).  
# 
# The point of this project is not to know how to read math formulas, so here is the code to calculate the monthly payment: 
# 
# Car loan monthly payment calculation
# numerator = loan_amount * monthly_interest_rate
# denominator = 1 - (1 + monthly_interest_rate) ** -total_payments
# monthly_payment = numerator / denominator  

num_of_payments = (float(loan_duration) * 12)
years_duration = float(loan_duration)
numerator = net_loan * (float(annual_interest_rate) / 12)
denominator = 1 - (1 + (float(annual_interest_rate))) ** num_of_payments
monthly_payment = numerator / denominator 
 
# Output Detailed Loan Information:  
#     Display the loan amount (after any down payment adjustment). 

print(f"The net loan amount is {net_loan:.2f}.")

#     Show the total number of payments and the duration of the loan in years. 

print(f"The total number of payments is {num_of_payments:.2f} over {years_duration:.2f} years.")


#  ================= Here Next =====================================

#     Present the interest rate to the user.  Finally, display the calculated monthly payment, formatted to two decimal places.  


  

"""
Scratchpad for equations

current_age = input("How old are you?")
age_in_seven_years = int(current_age) + 7
print(f"In seven years, you'll be {age_in_seven_years} years old!")

circumfrence = input("How far around is the circle?")
diameter = float(circumfrence) / (22/7)
print(f"The circle's diameter is {diameter:.2f}.")

"""
 
# Tips for Success: 
#      Clarity and Precision: Ensure your prompts are clear so the user knows exactly what information to enter. 
#      Precision in instructions leads to accurate inputs.  
 
# Variable Naming: 
# Use descriptive names for your variables to make your code self-explanatory and easier to follow.  
# 
# Implement Conditional Logic: 
# Use if statements effectively to guide the program's flow based on the user's inputs about the down payment and interest rate.  


"""

Steve’s Working Draft Workflow:  
•	Document the Problem -- This came from the book -- See below
•	Develop or Understand a Logic Narrative -- Probably from the book -- See below
•	Develop Psudo Code
•	Code
•	Test and Debug  


2.13 Project: Loan Payment Calculator 
Are you ready to tackle your first project? I think so. Like all projects in this book, you can download the final solution from GitHub. For more details, refer to the Appendix. 
 
Objective: 
Enhance your understanding of Python by developing a Loan Payment Calculator that accounts for optional down payments and handles a 0% interest rate. This project will deepen your knowledge of variables, data types, and arithmetic operations and introduce you to making decisions in your code using conditional logic. 
 
Step-by-Step Guide:
 
Prompt for Basic Loan Information:  Ask the user to input the total loan amount for the car.  Request the annual interest rate as a percentage. The user should be able to input a number like 7.5 for a 7.5% rate.  Inquire about the loan duration in years from the user.  
 
Inquire About Down Payment:  Ask the user if they want to include a down payment.  If the user answers yes, prompt for the down payment amount and adjust the loan amount accordingly by subtracting the down payment from the initial loan amount.  
 
Calculate Monthly Payment:  First, check if the annual interest rate is greater than 0.  If yes, convert the annual interest rate to a monthly rate and proceed with the regular loan payment calculation formula.  If the interest rate is 0%, calculate the monthly payment by simply dividing the loan amount (after adjusting for any down payment) by the total number of payments (loan duration in years multiplied by 12).  Use the formula to calculate the monthly payment of a loan. 
 
The formula is:  where: M is the monthly payment.  P is the loan amount (principal).  r is the monthly interest rate (annual interest rate divided by 12).  n is the total number of payments (loan duration in years multiplied by 12).  The point of this project is not to know how to read math formulas, so here is the code to calculate the monthly payment: # Car loan monthly payment calculation
numerator = loan_amount * monthly_interest_rate
denominator = 1 - (1 + monthly_interest_rate) ** -total_payments
monthly_payment = numerator / denominator  
 
Output Detailed Loan Information:  Display the loan amount (after any down payment adjustment).  Show the total number of payments and the duration of the loan in years.  Present the interest rate to the user.  Finally, display the calculated monthly payment, formatted to two decimal places.  
 
Tips for Success: Clarity and Precision: Ensure your prompts are clear so the user knows exactly what information to enter. Precision in instructions leads to accurate inputs.  
 
Variable Naming: Use descriptive names for your variables to make your code self-explanatory and easier to follow.  Implement 
 
Conditional Logic: Use if statements effectively to guide the program's flow based on the user's inputs about the down payment and interest rate.  
 
Test Thoroughly: Run your program with different scenarios (including with and without a down payment, with a 0% and a positive interest rate) to ensure it behaves as expected under various conditions.  By completing this project, you'll not only practice basic Python programming concepts but also learn how to incorporate conditional logic to make your programs more dynamic and adaptable to user input. 
 
This practical application reinforces the fundamentals and Example of Possible Output 
•	Enter purchase amount: 15000  
•	Annual interest rate: 10  
•	Loan duration (years): 5  
•	Include down payment? (y/n): y  
•	Down payment amount: 2000  
Loan Details:      
•	Purchase Amount: $15000.00      
•	Down Payment: $2000.00      
•	Loan Amount: $13000.00      
•	Number of Payments: 60 (5 years)      
•	Interest Rate: 10.000      
•	Monthly Payment: $276.21



"""

