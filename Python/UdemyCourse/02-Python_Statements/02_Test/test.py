# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
li = st.split(" ")
l = [word for word in st.split() if word[0].lower() == 's']
print(l)

for word in li:
    if word[0].lower ()== 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10.
# answer: list(range(0,11,2))
for i in range(0,11):
    print(i)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
l = [x for x in range(1,51) if x % 3 == 0]
print(l)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

l = [x if len(x) % 2 == 1 else "even!" for x in st.split(" ")]
print(l)

for value in range(1,101):
    if value % 3 == 0:
        if value % 5:
            print(f"{value}: FizzBuzz")
        print(f"{value}: Fizz")
    elif value % 5 == 0:
        print(f"{value}: Buzz")
    else:
        print(f"{value} is none")

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
li = [x[0] for x in st.split(" ")]
print(li)