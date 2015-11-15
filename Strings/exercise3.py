                                ###############################
                                #                             #
                                #          Exercise 3         #
                                #     www.w3resource.com      #
                                ###############################


# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead the empty string.
#  Sample String : 'w3resource'
#  Expected Result : 'w3ce'
#  Sample String : 'w3'
#  Expected Result : 'w3w3'
#  Sample String : ' w'
#  Expected Result : Empty String

####################################################################################################################

def prog(txt):
    result = ""
    if len(txt) > 2:
        for i in txt:
            result = txt[0:2] + txt[-2:]
    return result

print(prog('hi, how are you?'))
print(prog('H'))
