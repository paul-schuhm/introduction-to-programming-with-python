# Practice: Dicitonary basics

# Model of a customer
customer_a = {
	"first_name": "Jane",
	"last_name": "Doe",
	"email": "jdoe@email.com",
	"total_purchases": 150.00
}

# Update value associated to key 'total_purchases'
customer_a['total_purchases'] += 50.00

# Let's check if the value is correctly updated
print(customer_a['total_purchases'])

# Add a key 'is_vip' (using list/index notation)
customer_a['is_vip'] = True

# Print the full name (with formated strings)
print(f"{customer_a['first_name']} {customer_a['last_name']}")

# Recall on formated strings
x = 1
# Formated string ({x} will be evaluated and replaced by its value)
print(f"The value of x is {x}")

# Remove a key
customer_a.pop('email')
print(customer_a)



