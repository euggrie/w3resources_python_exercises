                                ###############################
                                #                             #
                                #          Exercise 10        #
                                #     www.w3resource.com      #
                                ###############################



#  Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

######################################################################################################################
def prog(string):
    new_string = ""
    char1 = string[0]
    char2 = string[-1]
    rest = string[1:-1]
    new_string = char2 + rest + char1

    # return str1[-1:] + str1[1:-1] + str1[:1] another option

    return new_string

print(prog("banana"))
