'''
Program that asks for user's weight and height and returns IMC
'''

weight = float(input('Give me your weight in kilograms: '))
height = float(input('Give me your height in meters: '))

imc = weight / height ** 2

print(f'Your IMC equals to {imc}')