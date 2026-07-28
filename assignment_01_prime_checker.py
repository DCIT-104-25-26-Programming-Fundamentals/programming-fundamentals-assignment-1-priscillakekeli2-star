# Function to check if a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Main program
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")