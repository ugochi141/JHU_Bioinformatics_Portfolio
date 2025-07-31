# Ndubuisi_A06.py
# Assignment 6 Solutions

# Task 1: if-elif-else statements
print("=== Task 1: Weight Calculator ===")
# Ask user for mass in kilograms
mass = float(input("Enter the object's mass in kilograms: "))

# Calculate weight using the formula: Weight = mass x 9.8
weight = mass * 9.8

# Display the calculated weight
print(f"The object weighs {weight:.2f} Newtons")

# Check weight conditions and display appropriate message
if weight > 1000:
    print("The object is too heavy!")
elif weight < 10:
    print("The object is too light!")
else:
    print("The object is just the right weight!")

print()  # Empty line for spacing

# Task 2: while loop -- input validation
print("=== Task 2: Number Validation ===")
# Keep asking until we get a valid number
while True:
    number = float(input("Enter a number between 1 and 100: "))
    
    # Check if number is in valid range
    if 1 <= number <= 100:
        print(f"Valid number: {number}")
        break  # Exit the loop
    else:
        print("Invalid! Please enter a number between 1 and 100.")

print()  # Empty line for spacing

# Task 3: Loops practice
print("=== Task 3: Bug Collector ===")
total_bugs = 0

# Collect bugs for 7 days
for day in range(1, 8):
    bugs_today = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_today

# Display the total
print(f"Total number of bugs collected over 7 days: {total_bugs}")

print()  # Empty line for spacing

# Task 4: Creating a list
print("=== Task 4: Amino Acids List ===")
# Create the list of amino acids
amino_acids = ["Try", "Asp", "Lys", "Met"]

# Print the entire list at once
print("Printing entire list at once:")
print(amino_acids)

# Print each element individually using a loop
print("\nPrinting each amino acid individually:")
for amino_acid in amino_acids:
    print(amino_acid)

print()  # Empty line for spacing

# Task 5: List functions
print("=== Task 5: List Manipulation ===")
# 1- Add "Asp" to the end of the list
amino_acids.append("Asp")

# 2- Print the new list
print("After appending 'Asp':")
print(amino_acids)

# 3- Sort the amino acids in the list
amino_acids.sort()

# 4- Print the sorted list
print("\nAfter sorting:")
print(amino_acids)

# 5- Reverse the order of the sorted list
amino_acids.reverse()

# 6- Print the reversed order
print("\nAfter reversing:")
print(amino_acids)

# 7- Create sub-list of the 2nd to 4th amino acid
sub_list = amino_acids[1:4]  # Remember: Python uses 0-based indexing

# 8- Print the sub list
print("\nSub-list (2nd to 4th amino acids):")
print(sub_list)

print()  # Empty line for spacing

# Task 6: Lists and Decisions
print("=== Task 6: Amino Acid Selection ===")
# Create the list with the specified amino acids
amino_acids_2 = ["Trp", "Arg", "Liu", "Ilu", "Asp"]

# Get the length of the list
list_length = len(amino_acids_2)

# Prompt user for a number
user_choice = int(input(f"Enter a number from 1 to {list_length}: "))

# Check if the number is in valid range
if 1 <= user_choice <= list_length:
    # Convert to 0-based index (subtract 1)
    index = user_choice - 1
    print(f"The amino acid at position {user_choice} is: {amino_acids_2[index]}")
else:
    print(f"Error: Please enter a number between 1 and {list_length}")

