my_dict={'Valentin':1995,'Ludmila':1998,'Semen':1990 }
print('Year of birth list :',my_dict)
print('Year of birth Valentin:',my_dict['Valentin'])
print('Year of birth Sahsa:',my_dict.get('Sahsa'))
my_dict.update({'Sahsa': 1989, 'Ignat': 2001})
print('Fired',my_dict.pop('Ludmila'))
print('Updated Year of birth list :',my_dict)
print()
my_set = {7, 3, 4, 5, 7, True, True, 'list','type', 'int', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)