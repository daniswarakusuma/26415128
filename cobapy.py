#!/usr/bin/python
#def mean(numbers):
#	return float(sum(numbers)) / max(len(numbers),1)
with open ('doge') as d:
    for line in d:
	f=line.split(';')
	a=[]
	a.append(f[5])
	#print a
	a.append(f[7])
	a.append(f[9])
	a.append(f[11])
	total=0
	#print mean(a)
	for i in range(0,len(a)):
		total+=int(a[i])

	print total/4
