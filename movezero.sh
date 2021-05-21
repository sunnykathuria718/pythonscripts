#!/bin/bash
# Sorting the array in Bash 
# using Bubble sort
  
# Static input of Array
arr=(10 0 100 0 12)
  
echo "Array in original order"
echo ${arr[*]}
  
# Performing Bubble sort 
for ((i = 0; i<5; i++))
do
      
    for((j = 0; j<5-i-1; j++))
    do
      
        if [ ${arr[j]} -eq 0 ]
        then
            # swap
            temp=${arr[j]}
            arr[$j]=${arr[$((j+1))]}  
            arr[$((j+1))]=$temp
        fi
    done
done
  
echo "Array in sorted order :"
echo ${arr[*]}
