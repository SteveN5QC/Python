# Exercise_3_5_ENHANCED

# Original:  Write a for loop to print the first 10 numbers in the Fibonacci sequence
# Enhancement: Modify to accept an input of how many places to print and then print that many places


# Ask how many numbers in the Fibonacci sequence to print

input_string = input("How many numbers in the Fibonacci sequence shall I print for you? ")
sequence_count = int(input_string)


# # Initialize the variables

num_a = 0
num_b = 1

# Print the initial line

print(f"The first {sequence_count:.0f} numbers in the Fibonacci sequence are:")
 

for loop_index in range(1, (sequence_count + 1)):
        print(f"Sequence place {loop_index:.0f} is {num_a:.0f}")
        num_next = num_a + num_b
        num_a = num_b
        num_b = num_next

"""
Output:

PS C:\Users\N5QC\Documents\Repositories\Python\Lessons_and_Logs\Absolute_Beginners_Guide_to_Python_Programming\Chapter_3\Code> python Exercise_3_5_ENHANCED.py
How many numbers in the Fibonacci sequence shall I print for you? 25
The first 25 numbers in the Fibonacci sequence are:
Sequence place 1 is 0
Sequence place 2 is 1
Sequence place 3 is 1
Sequence place 4 is 2
Sequence place 5 is 3
Sequence place 6 is 5
Sequence place 7 is 8
Sequence place 8 is 13
Sequence place 9 is 21
Sequence place 10 is 34
Sequence place 11 is 55
Sequence place 12 is 89
Sequence place 13 is 144
Sequence place 14 is 233
Sequence place 15 is 377
Sequence place 16 is 610
Sequence place 17 is 987
Sequence place 18 is 1597
Sequence place 19 is 2584
Sequence place 20 is 4181
Sequence place 21 is 6765
Sequence place 22 is 10946
Sequence place 23 is 17711
Sequence place 24 is 28657
Sequence place 25 is 46368
PS C:\Users\N5QC\Documents\Repositories\Python\Lessons_and_Logs\Absolute_Beginners_Guide_to_Python_Programming\Chapter_3\Code>


"""