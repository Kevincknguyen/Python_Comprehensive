x = [ [5,2,3], [10,8,9] ] 
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
print(z)


#Problem 1
print("----------PROBLEM 1 ----------------")
x[1][0]=15
print(x)

students[0]['last_name']="bryant"
print(students)

sports_directory['soccer'][0]="Andres"
print(sports_directory)

z[0]['y']=30
print(z)

#Problem 2
print("----------PROBLEM 2 ----------------")
students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print(students2)

def iterateDictionary(w):
    for item in w:
        strings=""
        for key,value in item.items():
            strings +=value + " "
        print(strings)

iterateDictionary(students2)

#Problem 3
print("----------PROBLEM 3 ----------------")
def iterateDictionary2(key_name,some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])


iterateDictionary2('first_name', students2)

iterateDictionary2('last_name', students2)


#Problem 4
print("----------PROBLEM 4 ----------------")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):
    for keys, values in some_dict.items():
        print((len(some_dict[keys])) , (keys))
        for value in values:
            print(value)


printInfo(dojo)
