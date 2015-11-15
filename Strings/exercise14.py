                                ###############################
                                #                             #
                                #          Exercise 14        #
                                #     www.w3resource.com      #
                                ###############################



#  Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in
#  sorted form (alphanumerically). Go to the editor
#  Sample Words : red, white, black, red, green, black
#  Expected Result : black, green, red, white,red

######################################################################################

secuence = input("Enter comma separated words: ")
words = [word for word in secuence.split(",")]
print(",".join(sorted(list(set(words)))))