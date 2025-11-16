# Name: Kaushal Gohel
# Filename: module2_lab.py
# Description: This app accepts students names and GPAs and test if student qualifies for specific roles.


# Ask for students last name
students_last_name = input("Enter the student's last name: ")

# Quit if last name is ZZZ
if students_last_name == 'ZZZ':
    quit()

else:
    pass

# Ask for first name
students_first_name = input("Enter student's first name: ")

# Ask for GPA and ensure its float
students_gpa = float(input("Enter student's GPA: "))


if students_gpa >= 3.5:
    print("Student has made the Dean's list")

elif students_gpa >= 3.25:
    print("Student has made the Honor Roll")

