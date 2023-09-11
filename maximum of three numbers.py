# Write a program to find a maximum of given three numbers 
# (Use ternary operator).

def max_of_three(a, b, c):
  return (a if a > b and a > c else b if b > a and b > c else c)

a = 10
b = 20
c = 30

max_number = max_of_three(a, b, c)
print("The maximum number is", max_number)