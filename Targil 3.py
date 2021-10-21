#create a function that prints the numbers between 1-x.
# accept the x as parameter.
# default value should be 10

def printNum(min=1, max=10):
    for i in range(min, max, 1):
            print(i)

printNum()