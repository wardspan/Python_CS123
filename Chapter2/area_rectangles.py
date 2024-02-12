print("Welcome to the rectangle areas comparer!")
print("This program will compare the areas of two rectangles and tell you which one is larger.")
rectangle1_length = float(input("Enter the length of the first rectangle: "))
rectangle1_width = float(input("Enter the width of the first rectangle: "))
print("Great job! Now let's get the dimensions of the second rectangle.")
rectangle2_length = float(input("Enter the length of the second rectangle: "))
rectangle2_width = float(input("Enter the width of the second rectangle: "))
rectangle1_area = rectangle1_length * rectangle1_width
rectangle2_area = rectangle2_length * rectangle2_width
if rectangle1_area > rectangle2_area:
    print("The area of the first rectangle is", rectangle1_area, "which is greater than the area of the second rectangle,", rectangle2_area)    
elif rectangle1_area < rectangle2_area:
    print("The area of the second rectangle is", rectangle2_area, "which is greater than the area of the first rectangle,", rectangle1_area)    
else:
    print("The areas of the rectangles are equal.")
print("Goodbye!")
