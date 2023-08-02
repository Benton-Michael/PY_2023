# Week 1
#* Assignment: Nested Dictionaries and Lists

#*       0            1
x = [ [5, 2, 3], [10, 8, 9] ]

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan' },
    { 'first_name': 'John', 'last_name': 'Rosales' }
]

sports_directory = {
    'basketball' : [ 'Kobe', 'Jordan', 'James', 'Curry' ],
    'soccer' : [ 'Messi', 'Renaldo', 'Rooney']
}
z = [ {'x' : 10, 'y': 20} ]

#---------------------------------------------
#TODO 1. Change the value 10 in x to 15. Once you're done, x should be [ [5, 2, 3 ], [15, 8, 9 ] ]
x[1][0] = 15
print(x)



#--------------------------------------------
# TODO 2. Change the last_name of the 1st student from Jordan to Bryant
students[0]['last_name'] = 'Bryant'
print(students)



#--------------------------------------------
# TODO 3: In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])



#--------------------------------------------
#! Iterating through a list of dictionaries
# TODO 4. Create a function iterate_dictionary(some_list) that, given a list of dictionaries the function loops through each dictionary in the list and prints each key and the associated value. 

new_students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'fist_name':'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterate_dictionary(some_list):
    for i in range(0, len(some_list)):
        output = ""
        for key, val in some_list[i].items():
            output += f" {key} - {val},"
        print(output)
    
iterate_dictionary(new_students)


#--------------------------------------------
#! Get values from a list of dictionaries
# TODO 5: Create a function iterate_dictionary_2(key_name, list) that given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example: 
# iterate_dicitonary_2('first_name', students) will output:
# Michael
# John
# Mark
# KB

def iterate_dicitonary_2(key_name, list):
    for i in range(0, len(list)):

        for key, val in list[i].items():
            if key == key_name:
                print(val)

#* comment out the todo that is mutating the list
# iterate_dicitonary_2('first_name', students)
iterate_dicitonary_2('last_name', students)


#--------------------------------------------
#! Iterate through a dictionary with List Values
# TODO: Create a function print_info(some_dict) that given a whose values are all lists, 
# TODO prints the name of each key along with the size of its list, and then prints
# TODO the associated values within each key's list

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank' ],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key, val in dict.items():
        print("------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)
