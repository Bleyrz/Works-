immutable_var=1,2,3,4,'Memory',True
print(immutable_var)
#immutable_var[0]=9 #кортеж – это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных.
#print(immutable_var) #ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам
mutable_list=['shark','sheep','donkey','horse','bull']
print(mutable_list)
mutable_list[0]='seeker'
print(mutable_list)