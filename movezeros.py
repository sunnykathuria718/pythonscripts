a = [2,6,0,4,0,5]
prev_idx = 0
for i in range(len(a)):
    if  a[i] != 0:
       hold = a[prev_idx]
       a[prev_idx] = a[i]
       a[i] = hold
       prev_idx+=1
print(a)
