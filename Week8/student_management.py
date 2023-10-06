def student_manager():
    names = []
    gpas = []

    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_student(names, gpas)
        elif choice == 2:
            delete_student(names, gpas)
        elif choice == 3:
            edit_student(names, gpas)
        elif choice == 4:
            search_student(names, gpas)
        elif choice == 5:
            print_all(names, gpas)
        elif choice == 6:
            print('Program ends')
            running = False
        else:
            print('Invalid choice, try again')

def print_menu():
    print('1. Add student')
    print('2. Delete student')
    print('3. Edit student')
    print('4. Search student')
    print('5. Print all students')
    print('6. Quit')

def add_student(names, gpas):
    name = input('Enter student name: ')
    gpa = float(input('Enter student GPA: '))
    names.append(name)
    gpas.append(gpa)
    print(f'Student {name} added')

def delete_student(names, gpas):
    name = input('Enter student name: ')
    for i in range(len(names)):
        if names[i] == name:
            names.pop(i)
            gpas.pop(i)
            print(f'Student {name} deleted')
            return
    print(f'Student {name} not found')

def edit_student(names, gpas):
    found_pos = None
    finding = 'yes'
    
    while finding:
        name = input('Enter student name: ')
        for i in range(len(names)):
            if name == names[i]:
                found_pos = i
        
        if found_pos == None:
            print(f'{name} not found')
        else:
            print(f'Student: {name[found_pos]}, GPA: {gpas[found_pos]}')
            new_gpa = float(input('Enter new student GPA: '))
            gpas[found_pos] = new_gpa
        print(f'Student: {name[found_pos]}, GPA: {gpas[found_pos]}')
        print()
        answer = input("Do you want to edit more student (yes/no): ")
        finding = answer == 'yes'

def search_student(names, gpas):
    gpa = float(input('Enter GPA: '))
    for i in range(len(names)):
        if gpas[i] >= gpa:
            print(f'{names[i]}: GPA = {gpas[i]}')

def print_all(names, gpas):
    for i in range(len(names)):
        print(f'{names[i]}: GPA = {gpas[i]}')