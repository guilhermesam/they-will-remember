# Creates a list of numbers in descending order, based on a positive integer passed as a parameter
def descending_order(number):
    if number >= 0:
        return (int(''.join(sorted(str(number), reverse=True))))
    else:
        raise ValueError('Value < 0 is not acceptable')

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
  
def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        years += 1
    return years

# returns a number that is the concatenation 
# of the powers resulting from each of the 
# numbers that make up the number passed as param
def square_numbers(number):
    concat_square = str()
    for n in str(number):
        concat_square += str(int(n) ** 2)
    return int(concat_square)
