def divide_numbers(dividend, divisor, /, round_to=2):
    return round(dividend/ divisor, round_to)

print(divide_numbers(3,4,5))
# print(divide_numbers(dividend = 3,divisor=4,round_to=5))
print(divide_numbers(3,4,round_to=5))