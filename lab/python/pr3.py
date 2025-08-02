# Step 1: Define coefficients
a = 5
b = 10

# Step 2: Show the original equation
print("Step 1: Original equation:")
print(f"{a}x + {b} = 0")  # Output: 5x + 10 = 0

# Step 3: Move the constant term to the other side
print("\nStep 2: Subtract", b, "from both sides:")
# Output: Subtract 10 from both sides
print(f"{a}x = -{b}")  # Output: 5x = -10

# Step 4: Divide both sides by the coefficient of x
print(f"\nStep 3: Divide both sides by {a}:")
x = -b / a
print(f"x = -{b} / {a}")  # Output: x = -10 / 5

# Step 5: Final result
print("\nStep 4: Final answer:")
print("x =", x)  # Output: x = -2.0
