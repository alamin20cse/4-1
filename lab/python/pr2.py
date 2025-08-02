import cmath  # For complex number support

# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
    exit()
# Calculate the discriminant
D = b**2 - 4*a*c

# Calculate the two roots using the quadratic formula
root1 = (-b + cmath.sqrt(D)) / (2*a)
root2 = (-b - cmath.sqrt(D)) / (2*a)

# Output the results
print("The solutions of the equation are:")
print("x1 =", root1)
print("x2 =", root2)
