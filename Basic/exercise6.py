                                ###############################
                                #                             #
                                #          Exercise 6         #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
# with those numbers.

# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

string = input("Enter your numbers separated by commas : ")
list = []
for num in string:
    if num != ",":
        list.append(num)

tuple = tuple(list)

print('List : ',list)
print('Tuple : ',tuple)

# Also we can use
# list = string.slpit(",")

# str.split(sep=None, maxsplit=-1)
#Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit
#splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there
#is no limit on the number of splits (all possible splits are made).

