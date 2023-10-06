# 4. Make a copy of 13StarSquare_nestedLoops and modify it to produce the following output.
# [Hint: this involves one very small change to the code.]

size = int(input("What size square? "))
for row in range(size):
    output = ""
    for col in range(size):
        output += "*="
    print(output)

print()
input("Press return to continue ...")