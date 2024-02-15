from math import tan,pi
s = float(input('s:'))
n = int(input('n:'))
area =((n*s**2)/(4*tan(pi/n)))
print(area)