# You’re calibrating a tiny sensor before training a model. Given x, min_v, and max_v, compute:
# norm = (x - min_v) / (max_v - min_v)
# Then print norm with 2 decimal places.
# New concept — Feature scaling
# Models learn better when inputs share similar scales; min–max transform values into [0, 1] using a equation

values = input("Enter x, min_v, max_v: ").split()

x = float(values[0])
min_v = float(values[1])
max_v = float(values[2])

norm = (x - min_v) / (max_v - min_v)

print(f"{norm:.2f}")
