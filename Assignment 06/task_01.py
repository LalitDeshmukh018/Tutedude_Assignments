try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Input must be a number")
except ZeroDivisionError:
    print("Denominator cannot be zero")
else:
    print("Result:", result)
finally:
    print("Operation Complete")
