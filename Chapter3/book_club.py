print("Welcome to the Book Point Calculator!")
books_purchased = int(input("Enter the number of books purchased: "))
points = 0  # initialize points
if books_purchased <= 1:
    points = 0  # no points
elif books_purchased <= 3:
    points = 5  # 5 points
elif books_purchased <= 5:
    points = 15  # 15 points
elif books_purchased <= 7:
    points = 30  # 30 points
else:
    points = 60
print("You have earned", points, "points.")
print("Goodbye!")