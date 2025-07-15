# Prompt the user to input the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to control rows
while row < size:
    # Inner loop using for to print asterisks in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after one full row
    row += 1
