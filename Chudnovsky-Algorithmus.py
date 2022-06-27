from math import ceil, factorial
from decimal import Decimal, getcontext
from time import time


def pi(precision: int) -> str:

    if not isinstance(precision, int):
        raise TypeError("Undefined for non-integers")
    elif precision < 1:
        raise ValueError("Undefined for non-natural numbers")

    getcontext().prec = precision
    num_iterations = ceil(precision / 14)
    constant_term = 426880 * Decimal(10005).sqrt()
    exponential_term = 1
    linear_term = 13591409
    partial_sum = Decimal(linear_term)
    for k in range(1, num_iterations):
        multinomial_term = factorial(
            6 * k) // (factorial(3 * k) * factorial(k) ** 3)
        linear_term += 545140134
        exponential_term *= -262537412640768000
        partial_sum += Decimal(multinomial_term *
                               linear_term) / exponential_term
    return str(constant_term / partial_sum)[:-1]


decimal_places = 10000


start = time()
Pi = pi(decimal_places+2)
end = time()

print(Pi)
print(
    f"time required to calculate pi to the {decimal_places} decimal place: {end - start}")
