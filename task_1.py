# task_1 - сaching fibonacci

def caching_fibonacci():
    cache = {}  # Створення порожнього словника для кешу

    def fibonacci(n):
        if n <= 0:  # Перевірка на випадок n <= 0
            return 0
        if n == 1:  # Перевірка на випадок n == 1
            return 1
        if n in cache:  # Перевірка, чи вже є значення у кеші
            return cache[n]

        # Обчислення значення числа Фібоначчі з кешуванням результатів
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Повертаємо функцію, а не результат

# Отримуємо функцію fibonacci із кешуванням
fib = caching_fibonacci()

# Використовуємо функцію для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))  

