# CodeWars kata that expects an array to be returned

def fizzbuzz(limit):

    list = []
    
    for number in range(1, limit+1):
        if number % 15 == 0:
            list.append("FizzBuzz")
        elif number % 5 == 0:
            list.append("Buzz")
        elif number % 3 == 0:
            list.append("Fizz")
        else:
            list.append(number)
    return list
    
    
#My version that prints a list from 1-n

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 15 == 0: print("FizzBuzz")
        if i % 5 == 0: print("Buzz")
        if i % 3 == 0: print("Fizz")
        else: print(i)                  
        
