# Write a program that uses a loop to prompt the user to enter 5 test scores, 
# each one between 0 and 100. For each testscore it reads from the user it 
# prints “PASS” if the student score greater than or equal to 70 otherwise it 
# prints “FAIL”. The program should count the number of students that pass 
# and number of students that fail. As before a student scoring greater 
# than or equal to 70 passes the test and below 70 fails. It should print 
# the total count of students who pass and the total count of students 
# who fail at the end.

pass_count = 0
fail_count = 0

for _ in range(5):
    score = int(input("Enter a test score: "))
    if score >= 70:
        print("PASS")
        pass_count += 1
    else:
        print("FAIL")
        fail_count += 1

print("Total students passed:", pass_count)
print("Total students failed:", fail_count)