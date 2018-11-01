import random

students = []
with open('students.txt') as student_file:
    for student in student_file.readlines():
        students.append(student.strip())

for i in range(1000):
    print(random.choice(students))
