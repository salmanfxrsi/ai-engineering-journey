def sum(**kwargs):
    print(kwargs)
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

print(sum(a=30, b=42, c=22, d=98))