def caching_fibonachi():
    cache = {}

    def fibonachi(n):

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        result = fibonachi(n - 1) + fibonachi(n - 2)
        cache[n] = result

        return result

    return fibonachi


print("Створюємо наш калькулятор Фібоначчі...")
fib = caching_fibonachi()

print(f"Обчислюємо fib10: {fib(10)}")
print(f"Обчислюємо fib15: {fib(15)}")
print(f"Обчислюємо fib8: {fib(8)}")
