# Module 02 - Practice
from datetime import datetime
import math

#poem.py

text="Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. Twinkle, twinkle, little star,\n\tHow I wonder what you are"

print(text)

#current_datetime.py
print("Current date and time:")
print(datetime.now().strftime("%Y-%m-%d %H:%m:%S"))


#geometry.py
radius=1.1
print(f"radius={radius}\nArea=",math.pi * radius **2)
#Formating with 2 significative digits
print(f"{math.pi * radius**2:.2g}")

