                                ###############################
                                #                             #
                                #          Exercise 2         #
                                #     www.w3resource.com      #
                                ###############################


# Write a Python program to count the number of characters (character frequency) in a string.

###############################################################################################

def prog(txt):
    dict = {}
    for i in txt:
        k = dict.keys()
        if i in k:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(prog('gooogle.com'))