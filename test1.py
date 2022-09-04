def fib(n):
	if n==1:return 0
	elif n==2:return 1
	else:
		a =0
		b=1
		c = 0 
		for i in range(0,n-2):
			c= a+b
			a=b
			b=c
		return c
print(fib(8))

