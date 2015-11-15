                                ###############################
                                #                             #
                                #          Exercise 5         #
                                #     www.w3resource.com      #
                                ###############################


#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two
#  characters of each string.
#  Sample String : 'abc', 'xyz'
#  Expected Result : 'xyc abz'

####################################################################################################################
string1 = 'abc'
string2 = 'xyz'
def prog(a, b):
    char = a[-1]
    char2 = b[-1]
    a = a.replace(char, char2)
    b = b.replace(char2, char)
    return b + " " + a

print(prog(string1,string2))
