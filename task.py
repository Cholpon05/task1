name = input("Enter your name")
month = input("Enter month of your studies")
if month.lower() == "1":
    print("You are beginner")
else:
    if month.lower()!= "5":
        print("You are intermediate")

print("Welcome to your bank account!")

balance = []
while True:
    print("1) Calculate all expences ")
    print("2) Amount off expenses ")
    print("3) Add new expenses ")
    option = int(input("Choose variant: "))
    if option == 3:
        amount = int(input("Enter amount: "))
        name = input("Name of the service or good: ")
        date = input("Date of transaction: ")
        balance.append([amount, name, date])

    if option == 2:
        result = 0
        for i in balance:
            print(i, i[0])
            result += i[0]
            print(f"Total balance: {result}")

    if option == 1:

        print()
        for i in balance:
            print(f"{i[0]} | {i[1]} | {i[2]}")
        print()

