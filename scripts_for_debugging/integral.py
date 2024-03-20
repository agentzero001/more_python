def approxiamet_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    for i in range(1, n+1):
        midpoint = .5 * (2 * a + delta_x * (2*i-1))
        total_sum += f(midpoint)
    return total_sum * delta_x

f1 = lambda x: x**2 + 1

area = approxiamet_integral(0, 1, 10, f1)
print(area)