pattern = int(input("Enter the size of the pattern:"))
i = 0
while  i < pattern:
    # Outer loop controls the number of rows
    for j in range(pattern):
        # Inner loop prints asterisks for each row
        print("*", end="")
    print()  # Move to a new line after each row of asterisks
    i += 1