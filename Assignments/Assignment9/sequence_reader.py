import os

# ===== Task 1: Read and print two sequence files =====
def task1():
    try:
        # Read and print seq1.txt
        with open('seq1.txt', 'r') as file1:
            print("=== seq1.txt ===")
            print(file1.read())
        
        # Read and print seq2.txt
        with open('seq2.txt', 'r') as file2:
            print("\n=== seq2.txt ===")
            print(file2.read())
            
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure files are in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ===== Task 2: Write combined content to output file =====
def task2():
    try:
        combined_content = ""
        
        # Read seq1.txt
        with open('seq1.txt', 'r') as file1:
            combined_content += file1.read()
        
        # Read seq2.txt
        with open('seq2.txt', 'r') as file2:
            combined_content += file2.read()
        
        # Write to output file
        with open('combined_sequences.txt', 'w') as outfile:
            outfile.write(combined_content)
            print("Files combined successfully! Output saved to 'combined_sequences.txt'")
            
    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure files are in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ===== Main execution =====
if __name__ == "__main__":
    print("\n" + "="*50)
    print("TASK 1: PRINTING SEQUENCE FILES")
    print("="*50)
    task1()
    
    print("\n" + "="*50)
    print("TASK 2: COMBINING FILES")
    print("="*50)
    task2()
    
    # Simple file preview
    try:
        with open('combined_sequences.txt', 'r') as f:
            print("\nCombined file preview:")
            print(f.read(100))  # Show first 100 characters
    except:
        print("Could not preview combined file")
