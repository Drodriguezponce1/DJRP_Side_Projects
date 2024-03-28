# https://github.com/Drodriguezponce1/Complete-Python-3-Bootcamp/blob/master/03-Methods%20and%20Functions/08-Functions%20and%20Methods%20Homework.ipynb
import math
import string
print(math.pi)

#numero 1: write a function that computes the volume of a sphere 4/3PIr^3
print("############# NUMBER 1: VOLUME OF SPHERE #############")
def vol(rad):
    return (4/3)*math.pi*(rad**3)

print(f"Radius of {2}: {vol(2)}")


#numero 2: write a function that checks whether a number is in a given range(inclusive of high and low)
print("################# NUMBER 2: CHECK IN RANGE ############")
def ran_bool(num, low, high):
    return num in range(low, high+1)

def ran_check(num, low, high):
    if ran_bool(num, low, high):
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not in the range between {low} and {high}")

ran_check(5,6,7)

#numero 3: write a function that accepts a string and calculates the amount of upper case and lower cases
print("##################### NUMERO 3: CHECK UPPER AND LOWER ################")
def up_low(s):
    upper, lower = 0,0
    for letter in s:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    
    return upper,lower

st = 'Hello Mr. Rogers, how are you this fine Tuesday?'
u,l = up_low(st)

print(f"No. of Upper case characters: {u}\nNo. of Lower case characters: {l}")

#numero 4: write a function that takes a list and returns a new list with uniqie elemenets from the first list
print("########################## NUMERO 4: MAKE UNIQUE LIST FROM A LIST ################")
def unique_list(lst):
    return list(set(lst))

sample = [1,1,1,1,2,2,3,3,3,3,4,5]
print(f"Unique list: {unique_list(sample)}")

#numero 5: write a function that multiplies all numbers in a list
def multiply(numbers):
    su = 1

    for num in numbers:
        su *= num

    return su

li = [1,2,3,-4]
print(f"Multiple of list: {multiply(li)}")

#numer 6: write a program to check whether a string is a palindrome
print("###################### NUMERO 6: PALINDROME #################")
def palindrome(s):

    s = s.replace(" ","")
    return s == s[::-1]

print(palindrome("nurses                         run"))

#numero 7: write a program that checks whether a string is a pangram (contains every letter in the alphabet)
print("################### NUMERO 7: PANGRAM ###############")
def is_pangram(str1, alphabet = string.ascii_lowercase):

    str1 = str1.lower().replace(" ", "")

    for letter in alphabet:
        if letter not in str1:
            return False

    return True

def pangram(str1,  alphabet = string.ascii_lowercase):
    return alphabet == set(str1.lower().replace(" ", "").sort())
print(is_pangram("The quick brown fox jumps over the lazy dog"))