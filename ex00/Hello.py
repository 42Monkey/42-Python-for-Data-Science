ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")

# tuples are immutable, use concatenation with a new tuple is required
# [:1] means starts at index 0 and stop before index 1, a slight difference from regular indexing
ft_tuple = ft_tuple[:1] + ("Thailand!",)

# to modify a set, must remove the old value and add the new one
# python sets are unordered, could get {'Bangkok!', 'Hello'}, normal behaviour
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

# dictionaries are key-paired values, just needed to modify the value of the first key
ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
