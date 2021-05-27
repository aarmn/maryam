import math
inp=int(input())
if (inp==1):
	print("its 1 not prime nor composite")
else:
	for i in range(2,math.floor(inp**0.5)+1):
		if (inp%i==0):
			print("not prime")
			break
