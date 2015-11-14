                                ###############################
                                #                             #
                                #          Exercise 35        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
###################################################################################################################

def prog(x, y):
    if x == y:
        return True
    elif x + y == 5:
        return True
    elif abs(x - y) == 5:
        return True
    else:
        return False

print(prog(2, 40))