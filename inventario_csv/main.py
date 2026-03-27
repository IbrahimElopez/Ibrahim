import csv

print("Welcome to coders-riwi")

coders = []

with open('data/coders.csv','r', newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        coders.append(row)

name = input("What is your name ?")
city = input("what is your city ?")
clan = input("what is your clan ?")

coders.append({"name": name, "city": city, "clan": clan})

with open('data/coders.csv', 'w',  newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "city", "clan"])
    writer.writeheader()
    writer.writerows(coders)