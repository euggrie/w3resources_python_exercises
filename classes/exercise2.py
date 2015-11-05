##### ~ Python Exercise: Convert a roman numeral to an integer ~ #####

"""class py_solution:
	def roman_to_int(self, s):
		rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		int_val = 0
		for i in range(len(s)):
			if i > 0 and rom_val[s[i]] > rom_val[s[i-1]]:
				int_val += rom_val[s[i]] - 2 * rom_val[s[i-1]]
				
			else:
				int_val += rom_val[s[i]]
		return int_val

#print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('CLXXIII'))
#print(py_solution().roman_to_int('C'))"""


###########################
#						  #
#		My solution       #
#						  #
###########################

class solution:
	def converter(self, valor):
		numero_romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		numero_integral = 0
		for i in range (len(valor)):
			numero_integral += numero_romano[valor[i]]
		return numero_integral

print(solution().converter('MMD'))