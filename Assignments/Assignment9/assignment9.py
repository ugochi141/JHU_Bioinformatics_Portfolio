import os

# === Task 1: Create NumberList.txt ===
def task1():
    with open('NumberList.txt', 'w') as f:
        for num in range(1, 101):
            f.write(f"{num}\n")

# === Task 2: Read and Sum Numbers ===
def task2():
    total = 0
    with open('NumberList.txt', 'r') as f:
        for line in f:
            num = int(line.strip())
            print(num)
            total += num
    print(f"Total: {total}")

# === Task 3: Process Sequence Files ===
def task3():
    output_lines = []
    for filename in os.listdir('.'):
        if filename.endswith('.txt') and filename.startswith('seq'):
            with open(filename, 'r') as seq_file:
                output_lines.append(seq_file.read().strip())
                output_lines.append("||")
    
    with open('Output.txt', 'w') as out_file:
        out_file.write('\n'.join(output_lines))

# === Run All Tasks ===
if __name__ == "__main__":
    print("=== Running Task 1 ===")
    task1()
    
    print("\n=== Running Task 2 ===")
    task2()
    
    print("\n=== Running Task 3 ===")
    task3()
    
    print("\nAll tasks completed successfully!")
