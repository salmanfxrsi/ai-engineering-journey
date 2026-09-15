D = {"target": "Google", "location": "Mountain View, CA", "employees": 100000, "founded": 1998, "CEO": "Sundar Pichai", "products": ["Search", "Ads", "Cloud", "YouTube"], "market_cap": 1.5e12}

keys = D.keys()

D["employees"] = 120000

print(keys)

values = D.values()
print(values)

D["employees"] = 160000
print(values)

items = D.items()
print(items)

# iterating
for key, value in D.items():
    print(key, value)