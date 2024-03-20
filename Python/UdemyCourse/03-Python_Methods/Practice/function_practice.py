#warmups
#LesserOfTheTwo:
#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
print("################# WARM UPS #############################")
def is_even(x):
    return x%2 == 0

def lesser_of_two_evens(a,b):
    if is_even(a) and is_even(b):
        if a > b:
            return b
        else:
            return a
        
    if a > b:
        return a
    
    return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

print("##############################################")
#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    t = text.split(" ")
    return t[0][0] == t[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

    ##makes_twenty(20,10) --> True
    #makes_twenty(12,8) --> True
    #makes_twenty(2,3) --> False ####
print("##############################################")

def makes_twenty(a,b):
    return (a == 20 or b == 20) or (a + b) == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

#level 1
print("################# LEVEL 1 #############################")
#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    return (name[0].upper() + name[1:3] + name[3].upper() + name[4:])

print(old_macdonald('macdonald'))

print("##############################################")
'''MASTER YODA: Given a sentence, return a sentence with the words reversed
##
Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

    >>> "--".join(['a','b','c'])
    >>> 'a--b--c'                  '''

def master_yoda(text):
    s = text.split(" ")
    s.reverse()
    return " ".join(s)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print("##############################################")
''' ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    
NOTE: `abs(num)` returns the absolute value of a number'''

def almost_there(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)

li = [90,104,150,209]
for values in li:
    print(almost_there(values))

print("################# LEVEL 2 #############################") 
'''#### FIND 33: 

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False'''

def has_33(li):
    for index, value in enumerate(li):
        if value == 3 and index != len(li) - 1:
            if li[index + 1] == 3:
                return True
            
    return False

print(has_33([1,3,3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
'''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'''

def paper_doll(text):
    st = ''

    for letter in text:
        st += letter + letter + letter

    return st

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print("##############################################")
'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19'''

def blackjack(a,b,c):
    s = (a + b + c)
    if s <= 21:
        return s
    else:
        if a == 11 or b == 11 or c == 11:
            s -= 10
            if s <= 21:
                return s

    return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print("##############################################")
'''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
 
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14'''

def summer_69(li):
    six_flag = True
    s = 0
    for index, value in enumerate(li):
        if value != 6 and six_flag == True:
            s += value
        else:
            six_flag = False

            if value == 9:
                six_flag = True

    return s

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print("################# CHALLENGING PROBLEMS #############################")
'''SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False'''

def spy_game(nums):
    li = []
    for index, value in enumerate(nums):
        if value in [0,7]:
            li.append(value)

    return li[0] == 0 and li[1] == 0 and li[2] == 7

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print("##############################################")
'''COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    count_primes(100) --> 25

By convention, 0 and 1 are not prime.'''

def count_primes(num):
    s = 0
    for value in range(2,num+1):
        if is_prime(value):
            s += 1
    return s


def is_prime(num):
    for v in range(2,num):
        if num % v == 0:
            return False

    return True

print(count_primes(100))

print("################# JUST FOR FUN #############################")
### Just for fun:
'''PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
    print_big('a')
    
    out:   *  
          * *
         *****
         *   *
         *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. <br>For purposes of this exercise, it's ok if your dictionary stops at "E".'''
dic = {'a':"  *  \n * *\n*****\n*   *\n*   *", "e":"****\n*\n*\n****\n*\n*\n****"}

def print_big(letter):
    return dic[letter]

print(print_big('a'))
print(print_big('e'))