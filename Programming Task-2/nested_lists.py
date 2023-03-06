if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    lowest = min([student[1] for student in students])
    slw = max([student[1] for student in students])
    
    for student in students:
        if student[1] > lowest and student[1] < slw:
            slw = student[1]
    second_lowest = [student[0] for student in students if student[1] == slw]
    
    for student in sorted(second_lowest):
        print(student)
