#! 
# If x to the power of 2 is less than or equal to  10, execute 27*x for values in range
[27*x for x in range(1,20) if x**2<=10]

# EVEN NUMBERS in a range
number_list = [x for x in range(20) if x % 2 ==0]
print(number_list)

# Find all numbers that can be DIVIDED BY 2 AND 5
num_list = [y for  y in range(100) if (y %2 == 0) and (y % 5 ==0)]
print(num_list)

# Conditional Statements - iterating to find the even and odds from a list
obj =  ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

# Creating Tuples 

