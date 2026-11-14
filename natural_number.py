def sum_natural(n):
    # Base case
    if n <= 0:
        return 0
    # Recursive case: n + sum of first (n-1) numbers
    return n + sum_natural(n - 1)


n = int(input("enter the value of n:"))
print(f"Sum of first {n} natural numbers = {sum_natural(n)}")