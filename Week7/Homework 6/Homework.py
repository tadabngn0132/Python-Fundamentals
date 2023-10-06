students = ['John', 'Peter', 'Mary', 'Jane', 'Tom', 'Jerry', 'Alice', 'Bob']
departments = ['IT', 'GD', 'IT', 'Biz', 'Biz', 'GD', 'IT', 'GD']
GPAs = [3.5, 3.0, 3.2, 3.6, 3.8, 3.9, 3.7, 3.4]

# Enter student name, find student and print his, her GPA and department
name = input('Enter student name: ')
found_pos = None

for i in range(len(students)):
    if students[i] == name:
        found_pos = i
        break

if found_pos == None:
    print("No student found")
else: 
    print(f'Student {students[found_pos]}, Department {departments[found_pos]}, GPA {GPAs[found_pos]}')

# Enter department name, find students in that department and print their names and GPAs
department = input('Enter student department: ')
found_pos = None
found_poss = []

for i in range(len(departments)):
    if departments[i] == department:
        found_pos = i
        found_poss.append(found_pos)

if found_pos == None:
    print("No department found")
else:
    for n in found_poss:
        print(f'{students[n]}, {departments[n]}, {GPAs[n]}')

# Find best student (highest GPA)
m = GPAs[0]
found_pos = 0

for n in GPAs:
    if n > m:
        m = n
print(f'Highest GPA: {m}')

# Enter a GPA, count how many students have GPA >= that GPA
GPA = float(input("Enter student GPA: "))

count = 0
for i in range(len(GPAs)):
    if GPAs[i] > GPA:
        count += 1
print(f'Number of products that students have GPA >= that GPA: {count}')

# Calculate average GPA of students in all departments
total_gpa = 0
count = 0

for i in range(len(GPAs)):
    total_gpa += GPAs[i]
    count += 1

print(f'{total_gpa/count:.2f}')

# Calculate average GPA of students in each department
total_gpa_it = 0
count_it = 0
total_gpa_gd = 0
count_gd = 0
total_gpa_biz = 0
count_biz = 0

for i in range(len(departments)):
    if departments[i] == 'IT':
        total_gpa_it += GPAs[i]
        count_it += 1
    elif departments[i] == 'GD':
        total_gpa_gd += GPAs[i]
        count_gd += 1
    else:
        total_gpa_biz += GPAs[i]
        count_biz += 1

print(f'Average GPA of IT students: {total_gpa_it/count_it:.2f}')
print(f'Average GPA of GD students: {total_gpa_gd/count_gd:.2f}')
print(f'Average GPA of Biz students: {total_gpa_biz/count_biz:.2f}')