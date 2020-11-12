people = [ {"name":"Harry", "house": "Gryffindor"},
            {"name": "Cho", "house": "Ravenclaw"},
            {"name": "Draco", "house": "Slytherin"}
]

# "lambda" is a function, that a "person" as input and return the person "name" in sort alphabatically.
people.sort(key=lambda person: person["name"])
print(people)