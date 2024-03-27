# The local driver’s license office has asked you to create an application that grades the 
# written portion of the driver’s license exam. The exam has 20 multiple-choice questions. 
# Here are the correct answers:
# 1.A 2.C 3.A 4.A 5.D 6.B 7.C 8.A 9.C 10.B 11.A 12.D 13.C 14.A 15.D 16.C 17.B 18.B 19.D 20.A
# Your student’s answers for each of the 20 questions from a text file and store the answers in another list.
# (Create your own text file to test the application.) After the student’s answers have been read 
# from the file, the program should display a message indicating whether the student passed or failed the exam. 
# (A student must correctly answer 15 of the 20 questions to pass the exam.) 
# It should then display the total number of correctly answered questions, 
# the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.

def main():
    # Read the correct answers from a file
    with open('correct_answers.txt', 'r') as file:
        correct_answers = file.read().split()

    # Read the student's answers from a file
    with open('student_answers.txt', 'r') as file:
        student_answers = file.read().split()

    # Check the student's answers
    num_correct = 0
    incorrect_questions = []
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            num_correct += 1
        else:
            incorrect_questions.append(i + 1)

    # Display the results
    if num_correct >= 15:
        print("Congratulations! You passed the exam.")
    else:
        print("Sorry, you failed the exam.")

    print("Total number of correctly answered questions:", num_correct)
    print("Total number of incorrectly answered questions:", len(incorrect_questions))
    print("Incorrectly answered questions:", incorrect_questions)

if __name__ == '__main__':
    main()
    