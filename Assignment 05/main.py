import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total

print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))
print(square(6))

print(string_utils.capitalize_words("hello world"))
print(string_utils.reverse_string("python"))
print(string_utils.word_count("hey you hows going"))

print(disc.apply_discount(1000, 10))
print(calculate_total([100, 200, 300]))
