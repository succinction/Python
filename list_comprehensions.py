"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

# [num for elem in vec for num in elem]
    
# [output_expression for variable in input_expression if condition]


"""


names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]


def long_names(num):
    return [name for name in names if len(name) >= num]

# print(long_names(5))

def starts_with(letter):
    return [name for name in names if name[:1] is letter]

# print(starts_with("S"))

def last_names(people):
    return [person[1] for person in people]

# print(last_names(people))

def smoosh(people):
    return [item for person in people for item in person]

# print(smoosh(people))