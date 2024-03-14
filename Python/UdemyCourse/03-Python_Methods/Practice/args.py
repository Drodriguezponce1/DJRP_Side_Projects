#if you had some arbritary def that can have many arguments use the *args part

def five_percent(*args):
    return sum(args) * .05

print(five_percent(1,2,3,4,5,6))

def my_funct(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My fave fruit is {kwargs['fruit']}")
    else:
        print(f"I DID NOT FIND ANY FRUIT HERE!")   

my_funct(fff = "Banana")   

def func(*args, **kwargs):
    print(f'I would like {args[1]} {kwargs["sodas"]}\'s')

func(10,20,30, fruit = 'Banana', sodas = "Dr. Pepper")