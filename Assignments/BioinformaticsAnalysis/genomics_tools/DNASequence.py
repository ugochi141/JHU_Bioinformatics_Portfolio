# Ask user for DNA sequence
dna = input("Enter a DNA sequence: ")

# Print length of sequence
print(f"Length of sequence: {len(dna)}")

# Count and print number of A's
print(f"Number of A's: {dna.count('A')}")

# Create RNA by replacing T with U
rna = dna.replace('T', 'U')
print(f"RNA sequence: {rna}")

