#Functions ALWAYS return something
def f():
    print("f executed")

# tax_rate = 0.2 means it is its default value
def compute_total_price(price, tax_rate=0.2):
    total = price * (1 + tax_rate)
    return total

result = f()
# A function without return statement, returns None
print(result)

# Positional arguments
print(compute_total_price(1500, 0.2))

# Named arguments
print(compute_total_price(tax_rate=0.2, price=1500))

# Default arguments (use 0.2 by default for tax_rate)
print(compute_total_price(1500))

# Override default value (tax_rate is equal to 0.5 here)
print(compute_total_price(1500, 0.5))
