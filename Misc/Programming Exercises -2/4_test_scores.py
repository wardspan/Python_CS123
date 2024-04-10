# Write a program that will read 5 test scores for 5 students 
# and convert them. Count the number of A’s, B’s, C’s, D’s and F’s grades in class. 
# At the end print the count of number of students with each grade. It should 
# add up all the scores and report the total of all the scores. It should 
# calculate the average testscore as well and print Average of all the scores is = 

# Initialize grade counters
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# Initialize variables for total score and number of students
total_score = 0
num_students = 5

# Read test scores for each student
for i in range(num_students):
    score = float(input(f"Enter test score for student {i+1}: "))
    total_score += score

    # Convert score to grade
    if score >= 90:
        grade_counts['A'] += 1
    elif score >= 80:
        grade_counts['B'] += 1
    elif score >= 70:
        grade_counts['C'] += 1
    elif score >= 60:
        grade_counts['D'] += 1
    else:
        grade_counts['F'] += 1

# Calculate average test score
average_score = total_score / num_students

# Print grade counts
for grade, count in grade_counts.items():
    print(f"Number of students with grade {grade}: {count}")

# Print total score and average score
print(f"Total of all scores: {total_score}")
print(f"Average of all scores: {average_score}")