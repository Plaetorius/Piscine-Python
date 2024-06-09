# Renamed to 'o' because 'object' is for something classes
def all_thing_is_obj(o: any) -> int:
	type_dict = {
		list: f'List : {type(o)}',
		tuple: f'Tuple : {type(o)}',
		set: f'Set : {type(o)}',
		dict: f'Dict : {type(o)}',
		str: f'{o} is in the kitchen : {type(o)}',
	}
	print(type_dict.get(type(o), "Type not found"))
	return 42
