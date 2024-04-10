# Write a program that prints a message stating what your letter grade is. For example 
# if your grade is above 90 it should print “you have an A”. If you have a score 
# between 80 and 89 it should print “You have a B”. So the program should prompt 
# the user to enter 5 test scores, each between 0 and 100. For each test score it should 
# print an appropriate message based on test score. For example if the score is between 
# 90 and a 100 it should print the message “You have an A”. 
# 90 – 100 A
# 80 – 89  B
# 70 – 79  C
# 65 – 69  D
# 0 – 64   F

# Prompt the user to enter 5 test scores
for i in range(5):
    score = int(input("Enter test score: "))

    # Determine the letter grade based on the score
    if score >= 90:
        print("You have an A")
    elif score >= 80:
        print("You have a B")
    elif score >= 70:
        print("You have a C")
    elif score >= 65:
        print("You have a D")
    else:
        print("You have an F")