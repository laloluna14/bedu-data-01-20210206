'''
Sample code of how the string interpolation works in Python
'''

name = 'Eduardo'
last_name = 'Luna'

# f-strings
full_name_f = f'{name} {last_name}'
print(full_name_f)

# string fortmatting
full_name_formatting = '{} {}'.format(last_name, name)
print(full_name_formatting)

full_name_formatting = '{n} {l}'.format(l = last_name, n = name)
print(full_name_formatting)