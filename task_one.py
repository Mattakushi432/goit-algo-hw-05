def caching_fibonacci():
    cache = {}

    def fibonacci(n):

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result

        return result

    return fibonacci


print("Створюємо наш калькулятор Фібоначчі...")
fib = caching_fibonacci()

print(f"Обчислюємо fib10: {fib(10)}")
print(f"Обчислюємо fib15: {fib(15)}")
print(f"Обчислюємо fib8: {fib(8)}")
