import random
 
def generate_groups(letters, num_groups):
    # Ensure the letters are in a list
    letters = list(letters)
    
    # Generate the specified number of groups
    for _ in range(num_groups):
        group = random.choices(letters, k=5)
        print(''.join(group))
 
# Example usage:
letters_input = input("Enter a string of letters: ")
num_groups_input = int(input("Enter the number of groups: "))
 
generate_groups(letters_input, num_groups_input)
