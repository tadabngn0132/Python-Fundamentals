# 6. Make a copy of 06Randoms_forLoop and modify it so that it ignores the value 7 (i.e. it does
# not include the value 7 in the output string even if it is one of the random values. Now
# modify it so that if the number 0 happens to be one of the random values it changes the
# output string to “Bad luck, no random values for you” and jumps out of the loop.

from random import randint


minimum = int(input("Min: "))
maximum = int(input("Max: "))

n_randoms = int(input("How many random numbers? "))
output = ""

b = 0

for counter in range(n_randoms):
    output += f" {randint(minimum, maximum)}"

    if b in range(minimum,maximum+1):
        if "0" in output:
            output = "Bad luck, no random values for you"
            break
        else:
            7 not in range(minimum, maximum)
            
            output += f" {randint(minimum, maximum)}"

print(output)

print()
input("Press return to continue ...")