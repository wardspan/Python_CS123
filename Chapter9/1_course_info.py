# Write a program that creates a dictionary containing course numbers and the room numbers 
# of the rooms where the courses meet. The dictionary should have the following key-value pairs:
# Course Number (key) CS101 CS102 CS103 NT110 CM241
# Room Number (value) 3004  4501  6755  1244  1411
#
# The program should also create a dictionary containing the instructors that teach each course. 
# The dictionary should have the following key-value pairs:
# Course Number (key) CS101 CS102 CS103 NT110 CM241
# Instructor (value) Haynes Alvarado Rich Burke Lee
#
# The program should also create a dictionary containing course numbers and the meeting times of each course. 
# The dictionary should have the following key-value pairs:
# Course Number (key) CS101 CS102 CS103 NT110 CM241
# Meeting Time (value) 8:00 a.m. 9:00 a.m. 10:00 a.m. 11:00 a.m. 1:00 p.m.
#
# The program should let the user enter a course number, then it should display the course’s room number, 
# instructor, and meeting time.

course_rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411"
}

course_instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

course_times = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."
}


def main():
    course_number = input("Enter a course number: ")

    if course_number in course_rooms:
        room_number = course_rooms[course_number]
        instructor = course_instructors[course_number]
        meeting_time = course_times[course_number]
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Invalid course number.")
        
if __name__ == "__main__":
    main()
    