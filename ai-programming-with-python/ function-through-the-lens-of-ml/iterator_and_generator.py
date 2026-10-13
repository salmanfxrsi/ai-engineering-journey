# iterator
s = {10, 20, 30, 40, 50, 60}

s_iter = iter(s)

print(s_iter)
print(type(s_iter))

for i in s:
    print(i)


# generator
lst = [x for x in range(500)]

def data_loader(chunk_size, lst):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
    
x = data_loader(5, lst)
print(type(x))