#! 
# If x to the power of 2 is less than or equal to  10, execute 27*x for values in range
[27*x for x in range(1,20) if x**2<=10]

# EVEN NUMBERS in a range
number_list = [x for x in range(20) if x % 2 ==0]
print(number_list)

# Find all numbers that can be DIVIDED BY 2 AND 5

num_list = [x for  x in range(20) if x %2 == 0]
print(num_list)
