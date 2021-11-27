def SortedSquares (arr):
     # since we know the list is sorted we can simply look at the first and last elements magnitude to know which square will be larger

     # let's start with two pointers, one at element [0] and one  at element [arr_length - 1]

     left, right = 0, len(arr)-1
     
     # we'll need to keep track of how many elements we've sorted so we'll initialize a tracker.  We also initialize an result list to store our answer

     tracker = len(arr) - 1
     final = [0 for x in arr]

     # we now move from out to in storing the largest elements first and ending with the smallest, all while squaring our result

     while index >= 0: 
  
        if abs(arr[left]) >= abs(arr[right]): 
            final[tracker] = arr[left] ** 2 
            left += 1
        else: 
            final[tracker] = arr[right] ** 2 
            right -= 1
        tracker -= 1
      
    return final 
