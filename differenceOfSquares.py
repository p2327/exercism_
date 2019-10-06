from typing import List
import itertools


def sumOfSquares(a: List[int]) -> int:
    return sum([a[i]**2 for i in range(len(a))])
    #return list(map(lambda x: x**2, a))


def squareOfSum(a: List[int]) -> int:
    return sum(a)**2


def delta(a: List[int]) -> int:
    return squareOfSum(a) - sumOfSquares(a)
