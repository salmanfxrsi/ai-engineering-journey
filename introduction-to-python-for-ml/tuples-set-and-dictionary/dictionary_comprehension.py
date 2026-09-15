square = {x: x**2  for x in range(1, 11) if x % 2 == 0}
print(square)

locations = ["New York", "Los Angeles", "Chicago"]
co_ordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]

exact_location = {co_or : loc for co_or, loc in zip(co_ordinates, locations)}
print(exact_location)

