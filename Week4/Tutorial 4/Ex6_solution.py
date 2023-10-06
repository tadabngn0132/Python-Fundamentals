from random import randint


minimum = int(input("Min: "))
maximum = int(input("Max: "))

n_randoms = int(input("How many random numbers? "))
output = ""
bad_luck = False
for counter in range(n_randoms):
    n = randint(minimum, maximum)
    if n == 0:
        print("Bad luck, no random values for you!")
        bad_luck = True
        break
    elif n != 7:
        output += f" {n}"

if not bad_luck:
    print(output)

print()
input("Press return to continue ...")