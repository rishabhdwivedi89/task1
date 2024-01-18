def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]

# Get the number of terms from the user
try:
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci(n)
        print(f"Fibonacci Sequence up to {n} terms: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
