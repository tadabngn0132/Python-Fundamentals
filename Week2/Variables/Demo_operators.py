# integer / float operators: +, -, *, /, //, %, **
a = 9
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division (result is a float)
print(a // b) # integer division (result is an integer)
print(a % b)  # modulo (remainder)
print(a ** b) # exponentiation (power)

# string operators: +, *
a = 'Hello'
b = 'Python'
print(a + b) # concatenation
c = a + a
d = a * 2    # multiplication concatenates the string with itself
print(c, d)
print('-' * 20)