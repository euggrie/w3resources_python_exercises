                                ###############################
                                #                             #
                                #          Exercise 7         #
                                #     www.w3resource.com      #
                                ###############################


#  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
#  if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#  Sample String : 'The lyrics is not that poor!'
#  Expected Result : 'The lyrics is good!'

####################################################################################################################

def prog(string):
    snot = string.find('not')
    sbad = string.find('poor')

    if sbad > snot:
        string = string.replace(string[snot:(sbad+4)], 'good')

    return string

print(prog('The lyric is not that poor!'))