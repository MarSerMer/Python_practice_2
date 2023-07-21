# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def get_fibo(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a+b

fibo_nums = get_fibo(22)
print(*fibo_nums)