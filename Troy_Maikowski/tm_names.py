students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#part I
def print_names(arr):
    for d in arr:
        print d['first_name'], d['last_name']
        
print_names(students)

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

#part II
def students_instructors(users):
    for key, val in users.items():
        count = 1
        print key
        for record in val:
            print count, "-", record['first_name'].upper(), record['last_name'].upper(), "-", len(record['first_name'] + " " + record['last_name']) - 1
            
students_instructors(users)