# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from typing import Tuple
from fractions import Fraction

def ask_for_information() -> tuple[int, int, int, int]:
    st = input("Please enter two fractions (using /) over space: ")
    fr_1, fr_2 = st.split()
    nom_1, denom_1 = fr_1.split('/')
    nom_2, denom_2 = fr_2.split('/')
    return int(nom_1), int(denom_1), int(nom_2), int(denom_2)

def fraction_reduction(nom, denom)-> tuple[int, int]:
    n = nom
    d = denom
    while n != 0 and d != 0:
        if n > d:
            n = n % d
        else:
            d = d % n
    res = n + d
    return nom//res, denom//res
def count_fractions():
    noms_and_denoms = ask_for_information()
    sum_nom = noms_and_denoms[0]*noms_and_denoms[3] + noms_and_denoms[1]*noms_and_denoms[2]
    sum_denom = noms_and_denoms[1]*noms_and_denoms[3]
    sum_nom, sum_denom = fraction_reduction(sum_nom, sum_denom)
    print(f'Sum of entered fractions is: {sum_nom}/{sum_denom}')
    mult_nom = noms_and_denoms[0]*noms_and_denoms[2]
    mult_denom = noms_and_denoms[1]*noms_and_denoms[3]
    mult_nom, mult_denom = fraction_reduction(mult_nom, mult_denom)
    print(f'Product of entered fractions is: {mult_nom}/{mult_denom}')
    a = Fraction(noms_and_denoms[0], noms_and_denoms[1])
    b = Fraction(noms_and_denoms[2], noms_and_denoms[3])
    print(f'Checking with Fractions: sum = {a + b}, product = {a * b}')
count_fractions()
