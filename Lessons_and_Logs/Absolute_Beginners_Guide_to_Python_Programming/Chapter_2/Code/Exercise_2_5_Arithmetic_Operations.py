# Exercise_2_5_Arithmetic_Operations

# Read In the first number
first_string = input("Please the first or left number")
first_number = float(first_string)

# Read in the second number
second_string = input("Please the second or right number")
second_number = float(second_string)

# Print the sum of the numbers

sum = first_number + second_number

print(f"{first_number:.2f} plus {second_number:.2f} is {sum:.2f}.")

# print(f"The sum of {first_number:.2f} is {sum:.2f}.")



# Print the difference (first minus second)

difference = first_number - second_number

print(f"{first_number:.2f} minus {second_number:.2f} is {difference:.2f}.")

# Print the product of the numbers

product = first_number * second_number

print(f"{first_number:.2f} times {second_number:.2f} is {product:.2f}.")

# Divide the numbers and print the result (first divided by second)

division = first_number / second_number

print(f"{first_number:.2f} divided by {second_number:.2f} is {division:.2f}.")


# Exponentiate the numbers and print the result (first to the second power)

power = first_number ** second_number

print(f"{first_number:.2f} raised to {second_number:.2f} power is {power:.2f}.")