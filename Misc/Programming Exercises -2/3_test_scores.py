# Write a program that will count the number of A’s,B’s ,C’s when the user 
# enters 5 test scores. The program should prompt the user to enter a 
# score between 0 and 100. Count the number of grades A's, B’s, C’s and print them.

# Initialize counters
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

# Loop to get 5 test scores
for i in range(5):
    score = int(input("Enter a score between 0 and 100: "))

    # Check the grade and increment the respective counter
    if score >= 90:
        count_a += 1
    elif score >= 80:
        count_b += 1
    elif score >= 70:
        count_c += 1
    elif score >= 65:
        count_d += 1
    else:
        count_f += 1
        

# Print the counts
print("Number of A's:", count_a)
print("Number of B's:", count_b)
print("Number of C's:", count_c)
print("Number of D's:", count_d)
print("Number of F's:", count_f)