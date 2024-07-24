# Exercise_2_6_Comparison_and_Logical_Operations

# Read In the person's age
age_string = input("Please enter the persons age ")
age_number = float(age_string)


# Check and set for child
if age_number < 13:
    child = True
    teenager = False
    adult = False
    senior = False


# Check and set for teenager
elif (age_number >= 13) and (age_number <20):
    child = False
    teenager = True
    adult = False
    senior = False


# Check and adult or senior
else:
    if (age_number < 65):
        child = False
        teenager = False
        adult = True
        senior = False
    else:
        child = False
        teenager = False
        adult = False
        senior = True


# Print the person's age category
if (child == True):
    print("This person is a child.")

elif (teenager == True):
    print("This person is a teenager.")

else:
    if (adult == True):
        print("This person is an adult.")
    else:
        print("This person is a senior.")

