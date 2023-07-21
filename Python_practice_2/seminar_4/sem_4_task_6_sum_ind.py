# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def get_sum_between_indexes(nums: list[int | float], *, a: int , b: int) -> int | float | None:
    if a > 0 and b > 0:
        if max(a,b) >= len(nums):
            a = min(a,b)
            print(a)
            b = len(nums)-1
            print(b)
        elif a > b:
            a, b = b, a
        print(f'{a=} {b=}')
        res_sum = 0
        for i in range (a, b+1):
            res_sum += nums[i]
        return res_sum
    else:
        return None

def decision_from_seminar(nums: list[int], start: int, end: int) -> int:
    i_start= max(0,min(start, end))
    i_end = min (len(nums), max(start,end))
    return sum(nums[i_start:i_end+1])

nums = [12, 0.7, 95, 7, 0.3 ]
print(get_sum_between_indexes(nums, a=70, b=2))
print(decision_from_seminar(nums, 2, 70))