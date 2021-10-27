# give the seq datas and this app convert to list or tuple

seq = input("enter ur seq numbers and seperated whit comma:\n") # numbers

my_list = seq.split(',') # convert to the list
my_tuple = tuple(my_list) # convert to tuple

print("\nList: {0} \ntuple : {1}".format(my_list,my_tuple))