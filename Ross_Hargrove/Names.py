students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Loop that iterates through each item in the dictionary and prints the first and last name
for value in students:
    print value["first_name"], value["last_name"]

# This print statement seperates part 1 and part 2 for readability
print " "

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

# Loop that iterates through each item in the dictionary
for key, data in users.items():
    print key
    index=1
    # Loop that iterates through the list and prints the first and last name along with place in list and name length
    for value in data:
        length = len(value["first_name"])+len(value["last_name"])
        print "{} -".format(index), value["first_name"], value["last_name"], "- {}".format(length)
        index+=1