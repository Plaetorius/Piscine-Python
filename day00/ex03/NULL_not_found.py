# Renamed to 'o' because 'object' is for something classes
def NULL_not_found(o: any) -> int:
	# print(o)
	# print(type(o))
	if o == None:
		print("Nothing: None <class 'NoneType'>")
	elif o != o:
		print("Cheese: nan <class 'float'>")
	elif o == 0 and type(o) == int:
		print("Zero: 0 <class 'int'>")
	elif o == '':
		print("Empty: <class 'str'>")
	elif o == False:
		print("Fake: False <class 'bool'>")
	else:
		print("Type not Found")
		return 1
	return 0
	