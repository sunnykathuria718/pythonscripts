import array as arr
a = [1,0,2,0,0,0,0,3,4,58]
prev_idx = 0
for i in range(len(a)):
	if a[i] != 0:
	   a[i], a[prev_idx] = a[prev_idx] , a[i]
	   prev_idx+=1
print(a)
