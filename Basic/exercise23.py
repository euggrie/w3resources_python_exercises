                                ###############################
                                #                             #
                                #          Exercise 23        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given sting.
#  Return the n copies of the whole string if the length is less than 2

##############################################################################################################

def prog(string, n):
    flen = 2
    if flen > len(string):
        flen = len(string)
    substring = string[:flen]

    result = ""
    for i in range(n):
        result = result + substring
    return result
print(prog('abcdef', 2))
print(prog('p', 3))