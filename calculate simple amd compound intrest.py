def simple_interest(principal, rate, time):
  interest = principal * rate * time / 100
  return interest

def compound_interest(principal, rate, time):
  interest = principal * (1 + rate / 100) ** time - principal
  return interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

simple_interest = simple_interest(principal, rate, time)
print("Simple interest:", simple_interest)

compound_interest = compound_interest(principal, rate, time)
print("Compound interest:", compound_interest)
