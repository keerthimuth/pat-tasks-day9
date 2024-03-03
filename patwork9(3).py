from functools import reduce

# Function to generate Fibonacci series using lambda and reduce
fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 1), [0, 1])

# Generate Fibonacci series up to 50 elements
result = fibonacci(50)

# Print the result
print(result)
