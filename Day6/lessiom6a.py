Dict = {'ali' : 18, 'rahim' : 12, 'karim' :45, 'joya' :20}
print ('all item :')
print(Dict)
print('print by key rahom: ')
print(Dict['rahim'])

Boys = {'ali' : 18, 'rahim' : 12, 'karim' :45, 'joya' :20}
Girls = {'joya' : 18}

studentx=Boys.copy()
studenty=Girls.copy()

print('all boys : ')
print(studentx)
print ('all girls :')
print(studenty)

print ('add sarah to our existiong dictionary')
Dict.update({"sarah": 9})
print(Dict)
print('if exist update dictionary')
Dict.update({'karim':12})
print(Dict)

print('delete by key:')
del Dict['ali']
print(Dict)

print(type(studentx))
print(dir(Dict))

print('print items:')
print("students name: %s" % Dict.items())
print('convert dic to list:')
print("studenrs name: %s" % list(Dict.items()))

print ('print only keys:')
for key in Dict.keys():
	print(key)

print ('print only values:')
for val in Dict.values():
	print(val)
	
print ('printonly key and value n: ')
for key in Dict.keys():
	print(key + "_" + str(Dict[key]))
	
students = list(Dict.keys())
students.sort()
print("sorted keys : " + str (students))

s=students[1]
print("key 1:" +s)

v=str(Dict[s])
print(v)

print("length : %d" % len (Dict))

plants = {}

plants ["radish"] =2
plants ["squash"] =4
plants ["carrot"] =7

print(plants["radish"])

print (plants.get("tuna"))
print(plants.get("tuna,"no tuna found"))
print (plants)

