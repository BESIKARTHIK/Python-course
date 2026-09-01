budget = int(input("Enter the budget: "))
if budget > 1000:
    print("Go for a trip")
elif budget > 5000:
    print("Resort stay")
elif budget > 3000:
    print("movie and dinner")
elif budget > 1000:
    print("cafe and shopping")
else:
    print("stay Home")