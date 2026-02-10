def caching_fibonacci():
    # Stores already computed Fibonacci numbers (memoization cache)
    cache = {}

    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # If the result is already cached, return it immediately
        if n in cache:
            return cache[n]

        # Compute the value recursively, store it in cache, and return it
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Return the inner function (it keeps access to cache via closure)
    return fibonacci


# Create Fibonacci function with a private cache inside (closure)
fib = caching_fibonacci()

# Use fib(n) to calculate Fibonacci numbers
print(fib(10))  # 55
print(fib(15))  # 610
