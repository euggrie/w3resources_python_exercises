# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.#

class py_solution:
	def is_valid_parenthese(self, string):
		stack = []
		chain = {"(": ")", "{": "}", "[": "]"}
		for parenthese in string:
			if parenthese in chain:
				stack.append(parenthese)
			elif len(stack) == 0 or chain[stack.pop()] != parenthese:
				return False
		return True


print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
print(py_solution().is_valid_parenthese("()[{)}}}}{{"))
