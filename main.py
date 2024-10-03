s = 'eksjzqw'
k = 2
temp = list(s)
for i in range(k//2):
    temp[i], temp[k-1-i] = temp[k-1-i], temp[i]
for i in range((len(s)-k)//2):
    temp[k+i], temp[len(s)-1-i] = temp[len(s)-i-1], temp[k+i]
for i in range(len(s)//2):
    temp[i], temp[len(s)-i-1] = temp[len(s)-1-i], temp[i]
temp = str(temp)
print(temp)