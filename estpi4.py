from decimal import *
getcontext().prec = 100

s = Decimal(1);
pi = Decimal(3);

print ("Approximation of the number PI through the Nilakantha's series\n")
n = int(input("Enter the number of iterations: "))

print("\nPlease wait. Running...\n");

for i in range(2, n*2, 2):
    pi = pi + s * (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
    s = -1 * s

print ("Aproximated value of PI :")
print (pi)