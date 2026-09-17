number = 15

if number > 0:
  print(f"{number} is positive")
else:
  print(f"{number} is negative")

if number:
  print(f"{number} is not equal to zero")

# Walrus operator (affectation and evaluation)
if x:=1:
  print("ok")