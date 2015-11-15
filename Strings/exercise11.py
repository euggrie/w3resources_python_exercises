                                ###############################
                                #                             #
                                #          Exercise 11        #
                                #     www.w3resource.com      #
                                ###############################



#  Write a Python program to remove the characters which have odd index values of a given string.

#################################################################################################

def prog(string):
    word = ""
    for i in range(len(string)):
        if i % 2 == 0:
            word = word + string[i]

    return word

print(prog('python'))
