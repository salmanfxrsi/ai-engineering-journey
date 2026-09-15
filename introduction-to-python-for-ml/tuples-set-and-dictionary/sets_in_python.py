A = {10, 20, 30, 40, 50}
print(type(A), A)

# empty structures
L = []
print(type(L))

T = ()
print(type(T))

S = {}
print(type(S))

#accessing 

S= { 1, 2, 3, 4, 1,2 } 

if (10 in S):
    print("3 is present")
else:
    print("not present")

sum =0 

for element in S:
    sum+= element 

print(sum)

#mutable

s= {5, 1 , 2 ,4, 3} 

s.add(10) 
s.add(0)

print(s)

s.pop()
s.pop()
print(s)

s.remove(5) 

print(s)






