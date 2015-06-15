#overtime function

def computepay(h,r):
    
	if h <= 40:
    	  return h * r
	else:
	  return (40*r) + ((h-40) * 1.5 * r)

#get user input

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print p
