from random import randint

def random(minimum, maximum):
    if maximum > minimum:
        random1 = randint(minimum, maximum)
        return random1
    else:
        print(maximum, "is less than", minimum)

min_str = input("Min: ")
max_str = input("Max: ")

if max_str == '':
    maximum = 100
else:
    maximum = int(max_str)

if min_str == '':
    minimum = 1
else:
    minimum = int(min_str)

# rd = random(minimum, maximum)

# if rd is not None:
#     print(rd)

rd = None
while rd is None:
    rd = random(minimum, maximum)

print(rd)

print()
input("Press return to continue ...")


# from random import randint

# def random(minimum, maximum):
#     if maximum > minimum:
#         random1 = randint(minimum, maximum)
#         print(random1)
#     else:
#         print(maximum, "is less than", minimum)

# min_str = input("Min: ")
# max_str = input("Max: ")

# if max_str == '':
#     maximum = 100
# if min_str == max_str == '':
#     minimum = 1
#     maximum = 100

# minimum = int(min_str)
# maximum = int(max_str)

# rd = random(minimum, maximum)

# print()
# input("Press return to continue ...")