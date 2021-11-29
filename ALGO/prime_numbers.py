#Prime numbers are numbers that are greater than one and divisible by one or itself
num = int(input("Input Your number \n"))
# prime numbers are greater than 1
if num > 1:
   		# check for factors
   		for i in range(2, num):
   			if (num % i) == 0:
   				print(num,"is not a prime number")
   				print(i,"times",num//i,"is",num)
   				break
   		else:
   			print(num,"is a prime number")

# if input number is less than or equal to 1, it is not a prime number
else:
	print(num,"is not a prime number") 
    