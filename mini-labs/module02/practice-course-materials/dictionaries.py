# Suppose we are writing program to handle invoices
# To represent 'invoice' in your program
# Invoice : id, total
# All my invoices:


# This is bad way of representing data
# I have to know the order of the data and
# what each data means! Data is not self-descriptive!
invoices = [
    #invoices[0][0], invoices[0][1]
    ["I000001",      5000],
    ["I000002", 3000],
    ["I000003", 20000],
    [3000, "I000004"] #mistake
]

#Access my first invoice
#fields and values depend upon positions!
id1 = invoices[0][0]
total1 = invoices[0][1] # Not really easy to use!

#Enter dictionaries
# This is a dictionary representing an invoice
invoice = {
    #key (field) => value
    "id": "I000001",
    "total": 5000
}

#How to access a value of a dictionary? By key!
#I want the value under the 'total' key
print(invoice['total'])
print(invoice['id'])

#MUCH BETTER WAY TO ORGANIZE AND DESCRIBE DATA IN PROGRAMS
invoices = [
    {
        "id": "I000001",
        "total": 5000
    },
    {
        "id": "I000002",
        "total": 3000
    },
    {
        "id": "I000003",
        "total": 20000
    }
]