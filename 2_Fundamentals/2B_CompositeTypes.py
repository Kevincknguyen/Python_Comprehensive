# ---Tuples---
from turtle import update

tuples=("Immutable","Mixed Values","AKA records","BUT YOU CAN add and slice them",55,False)
print(tuples[1])

tips="most useful for packaging multiple values in a return statement, or making immutable lists to prevent user error."


# ---Lists---
mylist=["Brackets","Mutable","Mixed possible but tyypically similar types",["nested list","this"],5]
print("-----Nested list print:",mylist[3][0])
mylist.pop()
mylist.pop(1)
mylist.append("Appends to end")
newList=["!!!!!!This adds to front!!!!!!!!"]+mylist+["!!!!!!This adds to back!!!!!!!!"]
print("------New List after concate:",newList)

copyOfList=[1,2,3,4]
print("------First index inclusive, 2nd index exclusive:",copyOfList[1:3])


other_examples=[".extend(2ndlist) adds the lists together",
".index(value) returns index at given value",
]


# ---Dictionaries----
dictionary={"existing key":"existing value","age":28,"mutable":True}
dictionary['existing key']="update"
dictionary['new key']="new value"
print("Dictionary: ",dictionary)
remove_key_value=dictionary.pop('existing key')
print(remove_key_value)
print(dictionary)

# Existing keys must be UNIQUE

built_in_fx_include=[".copy()","fromkeys(sequence,[value])",".items()",".keys()",".values()"]