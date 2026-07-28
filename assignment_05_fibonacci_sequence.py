# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

# Part A - Print the first N Fibonacci terms
def print_fibonacci(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    a, b = 0, 1
    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()  # Move to the next line


# Part B - Check if a number is in the Fibonacci sequence
def check_fibonacci(number):
    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return

    a, b = 0, 1

    while a < number:
        a, b = b, a + b

    if a == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# ---------------- Main Program ----------------

# Part A
n = int(input("How many terms? "))
print_fibonacci(n)

# Part B
num = int(input("Enter a number to check: "))
check_fibonacci(num)