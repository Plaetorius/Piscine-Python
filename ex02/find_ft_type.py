# REnamed to 'o' because 'object' is defined
def all_thing_is_obj(o: any) -> int:
	type_dict = {
		list: f'List : {type(o)}',
		tuple: f'Tuple : {type(o)}',
		set: f'Set : {type(o)}',
		dict: f'Dict : {type(o)}',
		str: f'{o} : {type(o)}',
	}
	print(type_dict.get(type(o), "Type not found"))
	return 42
