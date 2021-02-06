'''
Dictionaries
'''

student_1 = {
    'name': 'Galileo',
    'age': 31
}

student_2 = {
    'name': 'Sofía',
    'age': 4,
    'city': 'Zapopan',
    'state': 'Jalisco'
}

# Para evitar errores en el caso de que no exista el valor
print(student_2.get('state', 'N/A'))

print(student_1)
print(type(student_1))

print(student_1["name"])
print(student_1["age"])

print(f'{student_1["name"]} is {student_1["age"]} years old.')