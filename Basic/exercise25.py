                                ###############################
                                #                             #
                                #          Exercise 25        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to check whether a specified value is contained in a group of values.

# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

#############################################################################################
a = [1, 5, 8, 3]

def prog(list, x):
    if x in list:
        return True
    else:
        return False
print(prog(a, 5))
print(prog([3,6,7,8,9,3,2], 1))
