

eligible = []
ineligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter Student Details")

    name = input("Student Name: ")
    roll = input("Roll Number: ")

    marks = []
    for j in range(3):
        mark = int(input("Enter subject mark: "))
        marks.append(mark)

    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family annual income: "))

    total = sum(marks)
    aggregate = total / 3

    if (min(marks) >= 40 and
        attendance >= 75 and income <= 250000):

        eligible.append([
            name, roll, aggregate,
            attendance, income
        ])
    else:
        ineligible.append(name)

# Ranking based on predefined tie rules
eligible.sort(
    key=lambda x: (-x[2], -x[3], x[4])
)

print("\n--- SCHOLARSHIP RANKING ---")

if len(eligible) == 0:
    print("No eligible students found.")

for rank, student in enumerate(eligible, 1):
    print("\nRank:", rank)
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Aggregate:", student[2])
    print("Attendance:", student[3])
    print("Income:", student[4])

print("\n--- INELIGIBLE STUDENTS ---")

for name in ineligible:
    print(name)

print("\nScholarship Allocation Completed")
