# Coefficients (with input from user)
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the constant b: "))

# Show the original equation
print("\nStep 1: Original equation:")
print(f"{a}x + {b} = 0")

# Move the constant term to the other side
print("\nStep 2: Subtract", b, "from both sides:")
print(f"{a}x = -{b}")

# Divide both sides by the coefficient of x
print(f"\nStep 3: Divide both sides by {a}:")
x = -b / a
print(f"x = -{b} / {a}")

# Final result
print("\nStep 4: Final answer:")
print("x =", x)
