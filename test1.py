x = 117
x1 = x
z = []
z.append(x)
z1 = {}
#print(x)
for i in range(4):
	y = x*(1-(1/3))
	#print(y)
	z.append(y)
	z1[x] = y
	if i!=3:
		x = (x+sum([i+(i*0.10) for i in z[1:]]))/(i+2)
		#print(x)
	else:
		break
print(z[1]*0.10)
print(z1)
