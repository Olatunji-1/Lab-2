# Use this playground to experiment with list methods, using Test Run
my_list =[3,5,6,7,2]
string = '24198'

print(my_list)

my_list.append(8)
print(my_list)

new_list = list(string)
print(new_list)

new_list.sort()
print(new_list)

my_list.pop(-1)
print(my_list)

last_list = my_list.__add__(new_list)
print(last_list)