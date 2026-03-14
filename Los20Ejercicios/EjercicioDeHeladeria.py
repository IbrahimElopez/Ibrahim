vanilla_count = 0
chocolate_count = 0
strawberry_count = 0

for i in range (5):
    choice = input("Enter Flavor: ").lower()
    if choice == "vanilla":
        vanilla_count += 1
    elif choice == "chocolate":
        chocolate_count += 1
    elif choice == "strawberry":
        strawberry_count += 1
    else: print("flavor not found")
#print("The results are: ", "Vanilla:", vanilla_count, "Chocolate:", chocolate_count, "Strawberry:", strawberry_count)
print(f"The results are: , Vanilla:, {vanilla_count}, Chocolate:, {chocolate_count}, Strawberry:, {strawberry_count}")

