people =  [
   {"name": "Emma", "sex": "female", "age": 24},
   {"name": "Mia", "sex": "female", "age": 22},
   {"name": "Johnny", "sex": "male", "age": 34},
   {"name": "Alexis", "sex": "female", "age": 44},
   {"name": "Alexis", "sex": "male", "age": 33}
]


selected_attributes = {"name": "Alexis", "sex": "male"}

def filter_people(people, attributes):
    result = people
    for k, v in attributes.items():
        result = [ p for p in result if p[k] == v]
    
    return result


print(*filter_people(people, selected_attributes), sep="\n")

