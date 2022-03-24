def count_currency(amount):
        notes = [1000, 500, 100, 50, 10, 5, 2, 1]

        for i in notes:
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(i, " : ", j)


 # Calling function
amount = int(input("Enter the amount :"))
count_currency(amount)