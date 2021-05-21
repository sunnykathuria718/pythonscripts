#!/bin/bash
#num=545
echo "Enter any number"
read num
#storing the reaminder
s=0
#store number in reverse order
rev=""
#store originbal number in another variable
temp=$num

while [ $num -gt 0 ]
do
#Get remainder
s=$(( $num % 10 ))
#Get next digit
num=$(( $num / 10 ))
#store previous number and current digit in store
rev=$( echo ${rev}${s} )
done
if [ $temp -eq $rev ];
then 
echo "Number is Pallindrome"
else
echo "Number is not Pallindrome"
fi

