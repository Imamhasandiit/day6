students =[
{'id':1,'name':'nazmul','salary':300000},
{'id':2,'name':'Haque','salary':350000},
{'id':3,'name':'niloy','salary':30000},
{'id':4,'name':'sagor','salary':30000},
]
print("%-5s %-20s %-10s" % ('id','name','salary'))
print (40*"=")
for std in students:
	print("%-5s %-20s %-10s" %(std['id'],std['name'],std['salary']))
##############	
print("%-5s %-20s %-10s" % ('id','name','salary'))
print (40*"=")

for std in students:
	print("{:>5} {:>5} {:>5}".format (std['id'],std['name'],std['salary'])	) 
	
#DEF
#Defining function
