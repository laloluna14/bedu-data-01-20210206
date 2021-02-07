'''
given a number show its Tabla de Multiplicar
'''

number = int(input('Give me a number: '))

for i in range(1, 11):
    mult = number * i
    print(f'{number} X {i} = {mult}')