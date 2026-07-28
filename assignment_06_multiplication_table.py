# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# Multiplication Table Generator
# =============================================================================

# -----------------------------
# PART A — Single Table
# -----------------------------
def single_table():
    try:
        number = int(input("Enter a number: "))

        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Error: Please enter a valid integer.")


# -----------------------------
# PART B — Tables from 1 to N
# -----------------------------
def tables_to_n():
    try:
        n = int(input("\nEnter a positive integer (N): "))

        if n <= 0:
            print("Error: N must be a positive integer.")
            return

        for number in range(1, n + 1):
            print(f"\nMultiplication Table for {number}:")
            for i in range(1, 13):
                print(f"{number} x {i} = {number * i}")
            print("---------------------------")

    except ValueError:
        print("Error: Please enter a valid integer.")


# -----------------------------
# Main Program
# -----------------------------
single_table()
tables_to_n()
