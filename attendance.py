
No_of_students = int(input("Enter number of students : "))
No_of_days = int(input("Enter number of days : "))
Students = []
for i in range(No_of_students):
    i = input("Enter student name:"+str(i+1)+"   ")
    Students.append(i)
Students.sort()
empty_list = [0] * (len(Students))
for j in range(No_of_days):
    for k in range(No_of_students):
        l = input("If %s was present today: Enter p if NOT Enter a :     " % Students[k])
        if l.lower() == 'p':
            ndx = Students.index(Students[k])
            empty_list[ndx] += 1
Total_attendance = empty_list
for i in range(len(Students)):
    Roll_no = i+1
    Day_attendance = Total_attendance[i]
    Attendance_percentage = (Day_attendance/No_of_days)*100
    print(Roll_no, Students[i].ljust(10, ' '), Attendance_percentage)
