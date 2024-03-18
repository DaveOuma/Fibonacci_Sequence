What is a Fibonacci sequence in Python?

A Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In Python, you can generate a Fibonacci sequence using a simple loop or recursion. Here's an example of both approaches:

Using a loop:

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Using recursion:

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
n = 10
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Both methods will generate the first n Fibonacci numbers. The recursive approach might be less efficient for large n due to redundant calculations.

NOTE:
The current program will prompt the user to input the number of terms (n) for the Fibonacci sequence. It then generates the Fibonacci sequence up to the specified term n using a loop and the fibonacci_sequence function. Finally, it prints the generated Fibonacci sequence.
