def calc_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    grades = []
    for i in range(5):
        grade = int(input("Enter test grade: "))
        grades.append(grade)
        letter_grade = determine_grade(grade)
        print("Letter grade:", letter_grade)

    average = calc_average(grades)
    letter_average = determine_grade(average)
    print("\nAverage test score:", average)
    print("Letter average:", letter_average)
    
main()
