
import math

def perform_math_operations():
    try:
        number = float(input("Enter a number: "))
        if number <= 0:
            print("Logarithm is only defined for numbers greater than 0.")
        else:
            print(f"Square root of {number}: {math.sqrt(number)}")
            print(f"Natural log of {number}: {math.log(number)}")
            print(f"Sine of {number} radians: {math.sin(number)}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


perform_math_operations()
