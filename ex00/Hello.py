ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# List

ft_list[1] = "World!"

ft_list[-1] = "World!"

ft_list.pop(-1)
ft_list.append("World!")

ft_list = [word if word != "tata!" else "World!" for word in ft_list]

def change_list(word):
	return (word if word != "tata!" else "World!")

ft_list = list(map(change_list, ft_list))

ft_list = list(map(lambda word : (word if word != "tata!" else "World!"), ft_list))

ft_list = ' '.join(ft_list).replace("tata!", "World!")


# Tuple

# Set

# Dictionary


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)