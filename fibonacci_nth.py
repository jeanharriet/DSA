def fibonacci(n):
    # Base cases
    if n == 1:
        return 0      # 1st term
    if n == 2:
        return 1      # 2nd term
    # Recursive case: sum of the previous two terms
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the term's position N: "))
if n <= 0:
    print("Error:input a positive integer")
else:
    print(f"The {n}th term of the Fibonacci series = {fibonacci(n)}")