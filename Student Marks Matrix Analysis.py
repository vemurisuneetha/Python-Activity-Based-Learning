n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    row = []
    for j in range(m):
        x = int(input(f"Enter marks student {i+1} subject {j+1}: "))
        row.append(x)
    marks.append(row)
max_total = 0
topper = 0
for i in range(n):
    total = 0
    for j in range(m):
        total = total + marks[i][j]
    print(f"Student {i+1} total:", total)
    if total > max_total:
        max_total = total
        topper = i+1
print("Topper is Student", topper, "with", max_total, "marks")