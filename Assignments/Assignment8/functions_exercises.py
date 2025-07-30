#!/usr/bin/env python3
"""
Functions Exercises: User Input and File Validation
Demonstrates function benefits through practical examples
"""

import os  # Import os module for file operations

# Exercise 1: Function that prompts user and returns their answer
def get_user_input(prompt_message):
    """
    This function prompts the user with a custom message and returns their response.
    
    Parameters:
        prompt_message (str): The message to display to the user
    
    Returns:
        str: The user's response
    """
    # Get input from user with the provided prompt
    user_response = input(prompt_message + " ")
    
    # Return the response back to whoever called this function
    return user_response


# Exercise 2: Function that validates filename with 5 attempts
def validate_filename():
    """
    This function keeps prompting for a filename until a valid file is entered
    or until 5 attempts have failed.
    
    This is a Type 1 function - no parameters, no return value
    """
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        # Prompt user for filename
        filename = input(f"Attempt {attempts + 1}/{max_attempts} - Enter a filename: ")
        
        # Check if file exists using os.path.exists()
        if os.path.exists(filename):
            print("File found, thanks!")
            return  # Exit the function early if file is found
        else:
            print(f"File '{filename}' not found. Please try again.")
            attempts += 1
    
    # If we get here, all 5 attempts failed
    print("You did not enter a valid file name")


# Additional helper function to demonstrate benefits
def create_test_file():
    """
    Creates a test file for demonstration purposes
    """
    with open("test_file.txt", "w") as f:
        f.write("This is a test file for the exercise.")
    print("Created 'test_file.txt' for testing purposes.")


# Main program
def main():
    """
    Main function that demonstrates both exercises
    """
    print("=== EXERCISE 1: User Input Function ===")
    print("This demonstrates a function that returns a value\n")
    
    # Call the function with different prompts
    name = get_user_input("What is your name?")
    print(f"Hello, {name}!")
    
    favorite_color = get_user_input("What is your favorite color?")
    print(f"Nice! {favorite_color} is a great color!")
    
    # Demonstrate reusability - we can use the same function multiple times
    major = get_user_input("What is your major?")
    print(f"Studying {major} sounds interesting!\n")
    
    print("\n=== EXERCISE 2: File Validation Function ===")
    print("This demonstrates a function with logic and no return value\n")
    
    # Optional: Create a test file
    create_file = input("Would you like to create a test file? (yes/no): ").lower()
    if create_file == 'yes':
        create_test_file()
        print()
    
    # Call the file validation function
    validate_filename()
    
    print("\n=== Program Complete ===")
    print("Notice how functions made our code:")
    print("1. More organized (each task in its own function)")
    print("2. Reusable (we called get_user_input multiple times)")
    print("3. Easier to understand (descriptive function names)")


# Only run main() if this script is run directly (not imported)
if __name__ == "__main__":
    main()
