# Задание №6
# ✔ Выведите в консоль таблицу умножения # от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

# for i in range(2, 10): # 2 6
#     for j in range(2, 11): # 2 3 4 5 6 7 8 9 10
#         for k in range(i, i + 4): # 2,6  6,10
#             if k != i + 4 - 1:
#                 print(f'{k:>2} X {j:>2} = {k * j:>2}\t')
#             elif j != 10:
#                 print(f'{k:>2} X {j:>2} = {k * j:>2}\n')
#             else:
#                 print(f'{k:>2} X {j:>2} = {k * j:>2}\n\n')

# for i in range(2,10):
#     for j in range(2,10):
#         print((str(i)+'*'+str(j)+'='+str(i*j)).rjust(9),end=' '*2)
#     print()

mult_gen = (f'\t{k:>2} X {j:>2} = {k * j:>2}\t' if k != i + 4 - 1 else \
            f'{k:>2} X {j:>2} = {k * j:>2}\n' if j != 10 else \
            f'{k:>2} X {j:>2} = {k * j:>2}\n\n' \
                for i in range(2, 10, 4) \
                    for j in range(2, 11) \
                        for k in range(i, i + 4) )
print(*mult_gen, end=' ')
