# Create a list of numbers in descending order, based on a positive integer passed as a parameter
def descending_order(number):
    if number >= 0:
        return (int(''.join(sorted(str(number), reverse=True))))
    else:
        raise ValueError('Value < 0 isn't acceptable')
        
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
        raise ValueError('Value < 0 isn't acceptable')
        
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
        raise ValueError('Value < 0 isn't acceptable')
