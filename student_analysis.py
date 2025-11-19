students=["Alice","Bob","Charlie","Diana","Eve"]
marks=[85,92,78,96,88]
print("=====STUDENT REPORT=====")
print(f"Total students:{len(students)}")
average_marks=sum(marks)/len(marks)
print(f"Average marks:{average_marks:.2f}")
print(f"Highest score:{max(marks)}")
print(f"Lowest score:{min(marks)}")
print("\n______ALL STUDENTS______")
for i in range(len(students)):
               print(f"{students[i]}:{marks[i]}/100")
