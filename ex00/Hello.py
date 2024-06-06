ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# ======================= LIST =======================

# Direct index
# ft_list[1] = "World!"

# Reverse index
# ft_list[-1] = "World!"

# Pop n' append
# ft_list.pop(-1)
# ft_list.append("World!")

# List comprehension
# ft_list = [word if word != "tata!" else "World!" for word in ft_list]

# Map with function
# def change_list(word):
# 	return (word if word != "tata!" else "World!")

# ft_list = list(map(change_list, ft_list))

# Map with lambda
# ft_list = list(map(lambda word : (word if word != "tata!" else "World!"), ft_list))

# Conversion to string
ft_list = ' '.join(ft_list).replace("tata!", "World!").split(' ')

# ======================= TUPLE =======================

# Tuples are unchangeable, thus, conversion to list and then back into a tuple
ft_tuple = tuple(list(map(lambda word : (word if word != "toto!" else "France!"), ft_tuple)))

# ======================= SET =======================

# Sets are unordered, thus popping pops a random value
# (printing also shows them in a random order)
# Remove n' Add
ft_set.remove("tutu!")
ft_set.add("Paris!")

# ======================= DICT =======================

# Change via key
ft_dict['Hello'] = "42Paris!"

# Simple change

# Pop
# ft_dict.pop('Hello')
# ft_dict['Hello'] = "42Paris!"

# Popitem (pops last element, returns pair <key, value>)
# ft_dict.popitem()
# ft_dict['Hello'] = '42Paris!'


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)