# 1. Write the function print_line(n) that print n asterisks in 1 line. Using this function to print a triangle of stars.
# Example output:
# *
# * *
# * * *
# * * * *

# 2. Write the function print_triangle(n_lines, mode) that print triangle of stars based on the mode. There are 3 modes: normal, reversed and bottomup. If invalid mode is passed, should print an error.
# Normal mode output looks like in the exercise 1. 
# Here is the output of calling the function passing reversed mode print_triangle(3, 'reversed')
#       *
#     * *
#   * * *
# Bottomup mode: print_triangle(4, 'bottomup')
# * * * *
# * * *
# * *
# *
# Add 1 more parameter so that the function can print triangle of any symbol, not just asterisk.

def print_line(n):
    for i in range(1, n+1):
        print("* ", end=" ")

print_line(4)

def print_normal_triangle(n):
    for i in range(1, n+1):
        print_line(i)
        print()

print_normal_triangle(6)

def print_reverse_triangle(n):
    for i in range(0, n+1):
        for j in range(0, n+1):
            if(j>n-i): print("* ",end=' ')
            else: print("  ",end=" ")
        print()

print_reverse_triangle(6)

def print_bottom_triangle(n):
    for i in range(n, 0, -1):
        print_line(i)
        print()

print_bottom_triangle(6)