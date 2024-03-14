#check if even
def is_even(num):
    return num % 2 == 0

print(is_even(4))

# for values in range(1,11):
#     if is_even(values):
#         print(f"{values} is even!")

#return true if any number is even inside a list
def check_even_list(num_list):
    for values in num_list:
        if is_even(values) == True:
            print(f"This list contains at least 1 even number!")
            return True
        else:
            pass
    
    return False

print(check_even_list([3,5,7]))

# return a list of evens
def even_list(num_list):
    return [x for x in num_list if is_even(x) == True]

l = even_list([1,2,3,4,5,6,7,8,9,10])
print(l)

m = even_list([3,5,7,9])
print(m)


