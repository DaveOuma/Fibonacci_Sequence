#!/usr/bin/python3

def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the specified term n.

    Args:
    - n (int): The number of terms for the Fibonacci sequence.

    Returns:
    - list: A list containing the first n terms of the Fibonacci sequence.
    """
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    """
    Main function to execute the program.
    """
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci_sequence(n)
        print("The Fibonacci sequence up to term", n, "is:")
        print(fib_sequence)

if __name__ == "__main__":
    main()

