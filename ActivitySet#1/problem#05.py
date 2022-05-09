# Functions
def computepay(h, r):
    if(h>40):
        rem=h-40
        pay=(rem*1.5+40)*r
    else:
        pay=h*r
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter the rate per hour")
r = float(rate)
p = computepay(h, r)
print("Pay", p)