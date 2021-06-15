import decimal
from functools import lru_cache


@lru_cache(maxsize=1_000_000)
def fibo(number):
    decimal.getcontext().prec = 1_000_000
    choice = int(number)
    root = decimal.Decimal(5 ** 0.5)
    fi = (1 + root) / 2
    x = ((fi ** choice) - ((-fi) ** -choice)) / root
    x = round(x)
    return str(x)


@lru_cache(maxsize=1_000_000)
def fi_sum(number):
    n = int(number)
    if n <= 0:
        return str(0)
    fibo = [0] * (n + 1)
    fibo[1] = 1
    sum_fi = fibo[0] + fibo[1]
    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        sum_fi = sum_fi + fibo[i]
    return str(sum_fi)
