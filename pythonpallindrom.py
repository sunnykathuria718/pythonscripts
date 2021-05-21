string = raw_input("Enter the string:")
rev_string = string[::-1]
#rev_string = string[1:4]
print(string[1:2])
print(string[::-1])
print(rev_string)
if string == rev_string:
	print("string is pallindrome")
else:
	print("string is not pallindrome")
