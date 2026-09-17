# def sum(*numbers):
#     sum = 0
#     # for x in numbers
#     for x in numbers:
#         sum += x
#     return sum

# print(sum(1,2,3))


# pdb.set_trace() is a function call in Python that hardcodes a breakpoint directly into your code.
import pdb; pdb.set_trace()

def calculate_total(prices, tax_rate):
    subtotal = sum(prices)
    breakpoint()  # Execution pauses here; drops you into the pdb shell
    total = subtotal * (1 + tax_rate)
    return total

calculate_total([10, 20, 30], 0.05)