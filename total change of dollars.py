# Write a program to get change values in Quarter, Dime, 
# Nickels and Pennies, and calculate the value of change in 
# Dollars. Consider Quarter = 0.25 $, Dime = 0.10 $, Nickels = 
# 0.05 $ and Penny = 0.01 $.



def get_change_value(quarters, dimes, nickels, pennies):
  total_value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
  return total_value

quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))

total_value = get_change_value(quarters, dimes, nickels, pennies)
print("The total value of your change is ${}".format(total_value))
