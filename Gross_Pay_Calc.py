# takes input from user for hours worked and rate of pay and calculates your gross pay
# calculates overtime based on a 40 hour work-week and rate of 1.5x

hrs = input("Enter Hours:")

try:
    h = float(hrs)
except:
    print("Error, please enter a numeric number")

rate = input("Enter Rate")

try:
    r = float(rate)
except:
    print("Error, please enter a numeric number")

if h <= 40:
    gross = h * r
    print("Gross pay is ", gross)
else: 
    if h > 40:
        gross = ((h-40)*rate*1.5)+rate*40
        print("Gross pay with overtime is ", gross)

print("Thanks")
input("Press any key to exit")
          
