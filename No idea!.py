n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())

count = 0 
for i in array:
    if i in A:
        count += 1
    elif i in B:
        count -= 1
    else:
        count += 0
print(count)
