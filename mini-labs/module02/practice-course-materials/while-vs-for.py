# Because while and for loops are functionally equivalent, which one to choose?

# for loops are commonly used when you know IN ADVANCE the number of iterations
invoices = ['invoice 1', 'invoice 2', 'invoice 3']
for invoice in invoices:
    print(f"send {invoice}") 
print("Done.")

# while loops are commonly Used when you DONT KNOW when the loop will ends
while(True):
    #if the user only press enter (empty input)
    if(not input("-> ")):
        print("Bye")
        break
    print("Thanks for your input")

