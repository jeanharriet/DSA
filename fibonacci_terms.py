def generate_fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    series = generate_fibonacci(n - 1)
    series.append(series[-1] + series[-2])   # next term = sum of last two
    return series


n = int(input("Enter number of terms: "))
if n <= 0:
    print("Oops can't be found, positive number only")
else:
    print(f"First {n} terms:", generate_fibonacci(n))