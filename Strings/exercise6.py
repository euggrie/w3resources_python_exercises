                                ###############################
                                #                             #
                                #          Exercise 6         #
                                #     www.w3resource.com      #
                                ###############################


#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
#  is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
#  leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcing'
#  Sample String : 'string'
#  Expected Result : 'stringly'

####################################################################################################################

def prog(txt):
    a = 'ing'
    b = 'ly'
    if len(txt) >= 3:

        if txt[-3:] != 'ing':
            return txt + a
        elif txt[-3:] == 'ing':
            return txt + b

    else:
        return txt

print(prog('abc'))
print(prog('dancing'))
