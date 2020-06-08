# Creates a list of numbers in descending order, based on a positive integer passed as a parameter
def descending_order(number):
    if number >= 0:
        return (int(''.join(sorted(str(number), reverse=True))))
    else:
        raise ValueError('Value < 0 is not acceptable')

# Recursively, sum each digit of a number, until this number be <= 9
def digital_root(n):
    if n < 10:
        return n
    else:
        aux = 0
        for num in str(n):
            aux += int(num)
        return digital_root(aux)
   
# Reed two numbers "first" and "second" and return the sum of their factorials
def factorial_sum(first, second):
    sum_first = 1
    sum_second = 1
    for i in range(1 ,first+1):
        sum_first *= i
    for i in range(1 ,second+1):
        sum_second *= i
    return sum_first + sum_second

# Read a number and returns 'prime' or 'not prime'
def fast_prime_number(number):
    if number > 0:
        if number == 1:
            return 'Prime'
        for i in range(2, number):
            if number % i == 0:
                return 'Not Prime'
            else:
                return 'Prime'
    else:
        raise ValueError('Value <= 0 is not acceptable')
                         
# Returns a list which contains a fibonnacci sequence, being list[-1] < param
def fibonnacci(num_param):
    if num >= 0:
        a,b = 0,1 
        fibonnacci = []
        while a < num:
            fibonnacci.append(a)
            a, b  = b, a + b
        return fibonnacci
    else:
        raise ValueError('Value < 0 is not acceptable')     

# Based on class, verify which instance of student have most money
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        
def most_money(students):  
    def get_money(s):
        money = s.fives * 5 + s.tens * 10 + s.twenties * 20
        return money    
    money = []
    most_name = 'all'
    if all(get_money(x) == get_money(students[0]) for x in students) and len(students) > 1:
        return most_name
    for s in students:
        money.append(get_money(s))
    return students[money.index(max(money))].name

# Sorts an array by moving their zeros to the end
def move_zeros(array):
    return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if not isinstance(a, bool) and a == 0]

# A Narcissistic Number is a number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. 
def narcissistic( value ):
     return sum([int(x) ** len(str(value)) for x in str(value)]) == value        
        
# Verify the growing of a city, by passing the range of population and receiving
# the time in years to reach this number
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        years += 1
    return years        

# Sorts an array by sorting in ascending order their odd numbers, but the even numbers don't move
import numpy as np
def sort_array(array):
    array = np.array(array)
    index = np.where(array % 2 != 0)
    array[index] = np.sort(array[index])
    return list(array)

# returns a number that is the concatenation 
# of the powers resulting from each of the 
# numbers that make up the number passed as param
def square_numbers(number):
    concat_square = str()
    for n in str(number):
        concat_square += str(int(n) ** 2)
    return int(concat_square)

# Print a sequence of numbers, at the format:
# 1
# 22
# 333
# 4444
# .....
def triangle_quest(length):
    if length >= 0:
        for i in range(1, length):
        print(str(i) * i)
    else:
        raise ValueError('Value < 0 is not acceptable')

# Like Fibonnacci, but with sum with 3 last elements
def tribonacci(signature, n):
    if n > 0:
        tribonacci_list = signature.copy()
        a, b, c = signature[0], signature[1], signature[2]
        while len(tribonacci_list) < n:
            a = a + b + c
            tribonacci_list.append(a)
            b = a + b + c
            c = a + b + c
            tribonacci_list.append(b)
            tribonacci_list.append(c)
        return tribonacci_list[:n]
    else:
        return []
