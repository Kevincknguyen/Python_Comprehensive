# ---Tuples---
from turtle import update


tuples=("Immutable","Mixed Values",55,False)
print(tuples[1])

# ---Lists---
list=["Brackets","Mutable","Mixed possible but tyypically similar types",5]
print(list[2])
list.pop()
list.pop(1)
list.append("Test")
print(list)


# ---Dictionaries----
dictionary={"key":"value","age":28,"mutable":True}
dictionary['key']="update"
dictionary['new key']="new value"
print(dictionary)
remove_key_value=dictionary.pop('key')
print(remove_key_value)
print(dictionary)