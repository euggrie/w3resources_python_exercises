                                ###############################
                                #                             #
                                #          Exercise 22        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to count the number 4 in a given list

###########################################################################################

li = [1,2,3,4,4,4,4,4,45,5,6,6,7,7,8,8,9,6,6,666,888,9,9]
def prog(list):
    count = 0
    for i in list:
        if i == 4:
            count = count + 1
    return count

print(prog(li))