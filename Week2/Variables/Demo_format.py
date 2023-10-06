name = input('Enter your name: ')
age = int(input('Enter your age: '))
gpa = float(input('Enter your GPA: '))

print(f"{'Name':<20}{'Age':>3}{'GPA':>5}")
print(f'{name:<20}{age:>3}{gpa:>5}')

message = 'Hello'
print(f'+{message:>20}+')
print(f'*{message:<20}*')
print(f'~{message:^20}~')
print(f'?{message:20}?')

n = 100
print(f'|{n:>20}|')
print(f'|{n:<20}|')
print(f'|{n:^20}|')
print(f'|{n:20}|')

PI = 3.141592653589793
print(f'|{PI:>20.2f}|')
print(f'|{PI:<20.4f}|')
print(f'|{PI:^20.6f}|')
print(f'|{PI:20.8f}|')