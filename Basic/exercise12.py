                                ###############################
                                #                             #
                                #          Exercise 12        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to print the calendar of a given month and year.

# Note : Use 'calendar' module.

###################################################################################################

import calendar
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

cal2 = calendar.TextCalendar()
print(cal2.formatmonth(year,month))

#Another option to print it in HTML:
#cal = calendar.HTMLCalendar()
#print(cal.formatmonth(2015,11,True))