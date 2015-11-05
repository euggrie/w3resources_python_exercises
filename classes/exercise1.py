######## Python Exercise: Convert an integer it to a roman numeral #######

class py_solution:
	def converter(self, valor):
		numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		letras = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
		numero_romano = ''
		i = 0
		while valor > 0:
			for _ in range(valor // numeros[i]):#Take "valor" from argument given, look for the closest integer in list "numeros"
				numero_romano += letras[i]#assign the correspondent letter from "letras" and add that letter to string "numero_romano"

				valor -= numeros[i]#subtract that integer from "valor" and assign it to the variable
				
			i += 1 #Increase i to start the procces again until valor = 0
		return numero_romano # Return string numero_romano when valor = 0


print(py_solution().converter(64))
