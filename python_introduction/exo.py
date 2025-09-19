rows = 5  # height of the pyramid
i = 1     # start with the first row

while i <= rows:
    # Print spaces before the stars
    spaces = 1
    while spaces <= rows - i:
        print(" ", end="")  
        spaces += 1

    # Print stars (2*i - 1 stars for symmetry)
    stars = 1
    while stars <= (2 * i - 1):
        print("*", end="")
        stars += 1

    # Move to the next line after finishing a row
    print()
    i += 1
