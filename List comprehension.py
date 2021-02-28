x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = []
result2 = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k !=n:
                result = [i,j,k]
                result2.append(result)
print(result2)

        

