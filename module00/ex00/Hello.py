ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# lists are ordered, mutable sequence allowing duplicates elements
ft_list.append("World!")

# tuple are ordered, immutable sequence, allowing duplicates elements
# tuples are immutable, concatenation with a new tuple is required
# [:1] starts at index 0 and stops before index 1 (exclusive stop index)
ft_tuple = ft_tuple[:1] + ("Thailand!",)

# set are unordered collection of unique elements
# to modify a set, must remove the old value and add the new one
# sets are unordered, printed output can vary (normal behaviour)
ft_set.remove("tutu!")
ft_set.add("Bangkok!")

# dicttionaries are a collection of unique key-value pairs
# just needed to modify the value of the first key
ft_dict["Hello"] = "42Bangkok!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
