                                ###############################
                                #                             #
                                #          Exercise 7         #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to accept a filename from the user print the extension of that. Go to the editor

#Sample filename : abc.java
#Output : java

##################################################################################################

filename = input("Enter Filename: ")
file_ext = filename.split(".")
print("The extention of the file is: " + file_ext[-1])


