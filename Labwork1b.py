# Student Mark Management


# =========================
# INPUT STUDENTS
# =========================

def input_students():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")

        students[student_id] = {
            "name": name,
            "dob": dob
        }

    return students


# =========================
# INPUT COURSES
# =========================

def input_courses():
    courses = {}

    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print("\nCourse", i + 1)

        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        courses[course_id] = course_name

    return courses


# =========================
# INPUT MARKS
# =========================

def input_marks(students, courses):
    marks = {}

    print("\n===== INPUT MARKS =====")

    for course_id in courses:
        print("\nCourse:", course_id, "-", courses[course_id])

        marks[course_id] = {}

        for student_id in students:
            mark = float(
                input(
                    "Enter mark for "
                    + students[student_id]["name"]
                    + ": "
                )
            )

            marks[course_id][student_id] = mark

    return marks


# =========================
# LIST COURSES
# =========================

def list_courses(courses):
    print("\n===== COURSE LIST =====")

    for course_id in courses:
        print(course_id, "-", courses[course_id])


# =========================
# LIST STUDENTS
# =========================

def list_students(students):
    print("\n===== STUDENT LIST =====")

    for student_id in students:
        print(
            student_id,
            "-",
            students[student_id]["name"],
            "-",
            students[student_id]["dob"]
        )


# =========================
# SHOW STUDENT MARKS
# =========================

def show_marks(students, courses, marks):
    print("\n===== SHOW MARKS =====")

    course_id = input("Enter course ID: ")

    if course_id not in courses:
        print("Course does not exist!")
        return

    print("\nCourse:", courses[course_id])

    for student_id in students:

        mark = marks[course_id][student_id]

        print(
            student_id,
            "-",
            students[student_id]["name"],
            ":",
            mark
        )


# =========================
# MAIN PROGRAM
# =========================

print("===== STUDENT MARK MANAGEMENT =====")

students = input_students()

courses = input_courses()

marks = input_marks(students, courses)

list_courses(courses)

list_students(students)

show_marks(students, courses, marks)
