message = 'Hello Python' # this is a string
n = 10 # this is a number (integer)
x = 10.4 # this is a number (float)
flag = True # this is a boolean

print(message, n, x, flag)
print(type(message), type(n), type(x), type(flag))

# Convert between types
# Convert a number to a string (always possible)
n = 10
print(type(n))
n = str(n)
print(type(n))

# Convert a string to a number (sometimes possible)
n = int(input('Enter a number:'))
print(type(n))

# Convert integer to float
a = float(10)
print(a)

# Convert float to integer => round down
a = 10.999999
print(int(a))