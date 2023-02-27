arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for i in arr :  
    for j in i:
        for x in word :
            if j == x :
                time += arr.index(i) +3
print(time)