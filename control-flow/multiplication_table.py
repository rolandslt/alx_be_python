rows = 10 
number = int(input("Enter a number to see its multiplication table:"))
for Y in range(1, rows + 1) :
    Z = number * Y
    print(f"{number} * {Y} = {Z}")
print() 