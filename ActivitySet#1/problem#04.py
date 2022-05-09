# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate =input("enter the rate per hour:")
r =float(rate)
if(h>40):
    rem=h-40
    pay=(1.5*rem+40)*r
else:
    pay=h*r
print(pay)    