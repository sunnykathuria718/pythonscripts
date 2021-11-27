#!/bin/bash
echo "Enter any number"
read num
number=$num
reverse=0
while [ $num -gt 0 ]
do
rem=`expr $num % 10`
reverse=`expr $reverse \* 10 + $rem`
num=`expr $num / 10`
done
if [ $number -eq $reverse ]
then
echo "This is Pallindrome"
else
echo "This is not Pallindrome"
fi
