# https://realpython.com/python-practice-problems/
    # cd python-challenges
    # python integersums.py

'''

Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.

Planning:
Input - single integer

Method -
1) retrieve list of numbers from 0 to n
2) sum all numbers
3) return the total of numbers

Expected Pattern -
input n
loop number + sum (from 0) = new sum
loop until loop number = n

eg: n = 5
1) 1 + 0 = 1
2) 2 + 1 = 3
3) 3 + 3 = 6
4) 4 + 6 = 10
5) 5 + 10 = 15

'''

def add_it_up(n):
    '''
    This function takes a single integer as input and returns the sum of the integers from zero to the input parameter.
    '''
    sum_of_nums = 0

# my result:
    # for num in range(n): # 0 - 4 (5x loops)
    #     num += 1 # 1,2,3,4,5
    #     sum_of_nums += num # 1,3,6,10,15
    # return sum_of_nums

# with error:
    try:
        for num in range(n): # 0 - 4 (5x loops)
            num += 1 # 1,2,3,4,5
            sum_of_nums += num # 1,3,6,10,15
        return sum_of_nums
    except TypeError:
        return f"Input Type Error: {n} is not an Integer. Please enter an integer"

# RealPython solution alt (not recommended):
    # num = 1
    # sum_of_nums = 0
    # while num < n + 1:
    #     sum_of_nums = sum_of_nums + num
    #     num = num + 1
    # return sum_of_nums

# RealPython solution alt:
    # for num in range(n + 1): # 0 - 5 (6x loops)
    #     sum_of_nums += num # 0,1,3,6,10,15
    # return sum_of_nums

# RealPython alt:
    # return sum(range(n + 1)) # inbuilt sum

print(add_it_up(5))
print(add_it_up(2.5))
print(add_it_up("banana"))
