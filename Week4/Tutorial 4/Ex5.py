# 5. Make a copy of 14StarRectangle_nestedLoops and modify it to produce the following
# output. [Hint: you will need two inner loops, one after the other.]

rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
for row in range(rows):
    output = ""
    for col in range(cols):
        output += "*"
    for col in range(cols):
        output += "="
    print(output)

print()
input("Press return to continue ...")