count_change = lambda amount: cc(amount, 5)

def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins - 1) + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)


def first_denomination(kinds_of_coins):
        if kinds_of_coins == 1:
            return 1
        elif kinds_of_coins == 2:
            return 5
        elif kinds_of_coins == 3:
            return 10
        elif kinds_of_coins == 4:
            return 25
        elif kinds_of_coins == 5:
            return 50   

def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    for i in range(1, n+1):
        midpoint = .5 * (2 * a + delta_x * (2*i-1))
        total_sum += f(midpoint)
    return total_sum * delta_x

f1 = lambda x: x**2 + 1

area = approximate_integral(0, 1, 10, f1)

import sys

def max_diff(nums):
    res, min_so_far = -1, sys.maxsize
    for elem in nums:
        min_so_far = min(min_so_far, elem)
        if elem > min_so_far:
            res = max(res, elem - min_so_far)
    return res