a = [-4,11,0,3,10]
ans1 = [0 for x in a]
print(ans1)
left = 0
right =  len(a) - 1
print(right)

insertloc = len(a) - 1
ans = [0] * len(a)
print(insertloc)

while left <= right:
   leftsquare = a[left] * a[left]
   rightsquare = a[right] * a[right]
   
   if leftsquare <= rightsquare:
      ans[insertloc] = rightsquare
      right -= 1
      insertloc -= 1
   else:
      ans[insertloc] = leftsquare
      left += 1
      insertloc -= 1
print(a)
print(ans)

