# Task 1: A simple function
def print_info():
    """
    This is a Type 1 function - no arguments, no return value
    It simply prints information to the screen
    """
    print("Name: Ugochi Ndubuisi")  # Your actual name
    print("Major: Bioinformatics")   # Your major


# Task 2: Argument receiving function
def gc_content(dna_sequence):
    """
    This is a Type 2 function - accepts argument, no return value
    Calculates and prints the GC content of a DNA sequence
    
    GC content = (count of G + count of C) / total length * 100
    """
    # Convert to uppercase to handle both cases
    dna_sequence = dna_sequence.upper()
    
    # Count G and C nucleotides
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    
    # Calculate total length
    total_length = len(dna_sequence)
    
    # Calculate GC content percentage
    if total_length > 0:  # Avoid division by zero
        gc_percentage = ((g_count + c_count) / total_length) * 100
        print(f"GC content: {gc_percentage:.2f}%")
    else:
        print("Error: Empty DNA sequence")


# Task 3: Function that returns a value
def timesTen(number):
    """
    This is a Type 4 function - accepts argument AND returns value
    Multiplies the input number by 10 and returns the result
    """
    result = number * 10
    return result


# Task 4: Multiple arguments
def calculate_average(num1, num2, num3):
    """
    This is also a Type 4 function - accepts multiple arguments, returns value
    Calculates the average of three numbers
    """
    total = num1 + num2 + num3
    average = total / 3
    return average


# Main function to call all other functions
def main():
    """
    Main function that demonstrates all the tasks
    """
    print("=== Task 1: Simple Function ===")
    print_info()
    
    print("\n=== Task 2: GC Content Function ===")
    # Example DNA sequence
    test_dna = "ATGCGATCGTAGC"
    print(f"DNA sequence: {test_dna}")
    gc_content(test_dna)
    
    print("\n=== Task 3: TimesTen Function ===")
    test_number = 5
    result = timesTen(test_number)
    print(f"{test_number} times ten = {result}")
    
    print("\n=== Task 4: Average Function ===")
    # Test with three numbers
    n1, n2, n3 = 10, 20, 30
    avg = calculate_average(n1, n2, n3)
    print(f"Average of {n1}, {n2}, and {n3} = {avg}")


# Call main function to run the program
# This line ensures main() runs when the script is executed
if __name__ == "__main__":
    main()
