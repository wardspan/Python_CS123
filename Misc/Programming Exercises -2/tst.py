# Initialize grade counters
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# Initialize variables for total score and number of students
total_score = 0
num_students = 5

# Read test scores and grades for each student
for i in range(num_students):
    score = float(input(f"Enter test score for student {i+1}: "))
    grade = input(f"Enter grade for student {i+1}: ")

    # Update grade count
    grade_counts[grade] += 1

    # Add score to total
    total_score += score

# Calculate average score
average_score = total_score / num_students

# Print grade counts
for grade, count in grade_counts.items():
    print(f"Number of students with grade {grade}: {count}")

# Print total score and average score
print(f"Total score of all students: {total_score}")
print(f"Average score of all students: {average_score}")