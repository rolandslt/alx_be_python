

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number:"))
operation =input("Choose the operation (+, -, *, /):")



match operation:
    case "+":
        result = number1 + number2
        print(f"The result is {result}")   
    case "-" : 
        result = number1 - number2 
        print(f"The result is {result}")   
    case "*" : 
        result = number1  * number2
        print(f"The result is {result}" )   
    case "/" :  
        result = number1 / number2
        if number2 != 0 :
          print(f"The result i {result}") 
        else :
           print(f"Cannot divide by zero.")    
    case _:
      print("invalid operation")    