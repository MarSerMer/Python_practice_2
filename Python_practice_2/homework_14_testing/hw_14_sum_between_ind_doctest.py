
def sum_between_indexes(nums: list[int], start: int, end: int) -> int:
    """
    Функция получает на вход список чисел и два индекса.
    Вернуть сумму чисел между между переданными индексами.
    Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
    >>> sum_between_indexes([12, 0.7, 95, 7, 0.3 ],2,70)
    102.3
    >>> sum_between_indexes([0,0,0,0,0],1,2)
    0
    >>> sum_between_indexes([-5,-12,-7,-90,-1],-10,-50)
    0
    """
    i_start= max(0,min(start, end))
    i_end = min (len(nums), max(start,end))
    return sum(nums[i_start:i_end+1])

if __name__ == '__main__':
    # nums = [12, 0.7, 95, 7, 0.3 ]
    # print(sum_between_indexes(nums, 2, 70))
    import doctest
    doctest.testmod(verbose=True)