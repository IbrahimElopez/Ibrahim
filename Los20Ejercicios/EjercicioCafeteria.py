coffe = 4000
tea = 3500
juice = 5000
what_drink = input("What drink would you like?:")
how_many = int(input("How many would you like?:"))
if what_drink == 'coffe':
    Total_amount = coffe * how_many
elif what_drink == 'tea':
    Total_amount = tea * how_many
elif what_drink == 'juice':
    Total_amount = juice * how_many
else: print("Enter how many you would like")
print("Total Amount:", Total_amount)