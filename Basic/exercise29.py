                                ###############################
                                #                             #
                                #          Exercise 29        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present
#  in color_list_2.
# Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
#Expected Output :
#{'Black', 'White'}

###########################################################################################################
def prog(set1,set2):
    result = []
    for color in set1:
        if color not in set2:
            result.append(color)
    return result
print(prog(color_list_1, color_list_2))
# another solution
print(color_list_1.difference(color_list_2))

