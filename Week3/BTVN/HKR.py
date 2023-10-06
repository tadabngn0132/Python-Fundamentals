# # Cách tự nghĩ
# c = input("Enter a simple character from the alphabet: ")
# if c in ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m'] or c in ['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M'] and len(c) == 1:
#     if c in ["a","e","i","o","u"]:
#             print("Vowel")
#     else:
#             print("Consonant")
# else:
#         print("Invalid")


# # Cách của AI
# import string
# c = input("Enter a simple character from the alphabet: ")
# if c in string.ascii_lowercase or c in string.ascii_uppercase and len(c) == 1:
#     if c in ["a","e","i","o","u"]:
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid")

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'vower_consonant' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING c as parameter.
#

def vower_consonant(c):
    if len(c) != 1 or not c.isalpha():
        return "Invalid"
    elif c.lower() in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # DO NOT CHANGE IN HERE

    c = input()

    res = vower_consonant(c)

    fptr.write(res + '\n')

    fptr.close()
