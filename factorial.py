def factorial(n):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)


n = int(input("Enter a number: "))
print(f"Factorial of {n} = {factorial(n)}")