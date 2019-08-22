n = int(input())

count = 0

for i in range(0,n):
    count = 0
    for j in range(0,n):
        count = count + 1
    
    print('n =',i,"count",count)
