
conditionals={
    "==":"is equal",
    "!=":"not equal",
    ">=":"greater than (or equal to)",
    "<=":"less than (or equal to)",
    "and":"both expressions msut be true to return true",
    "or":"either condition true to return true",
    "not":"reverses true false opearand",
   
}


#FOR LOOPS------------------------------------------------------------------------------------
inclusiveStart=0
exclusiveStop=20
step=2

for variable in range (inclusiveStart,exclusiveStop,step):
    print(variable)

for variable in "Hello":
    print(variable)

dictionary_list_or_tuple={"example":"test"}
for item in dictionary_list_or_tuple:
    print(item)
    print(dictionary_list_or_tuple[item])

dictionary_specific={1:"one",2:"two"}
for key,val in dictionary_specific.items():
    print (key,val)


#While LOOPS------------------------------------------------------------------------------------

while_condition=5
while while_condition<10:
    while_condition +=1
else:
    print("This else is considered part of loop... triggers only if no break or returns")


#LOOPS TOOLS------------------------------------------------------------------------------------

a_break="breaks from the INNERMOST loop"
b_continue="cancels current loop iteration, continues loop"
c_return="breaks function"