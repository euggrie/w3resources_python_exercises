
#### Exercise 8 ####

"""Write a Python program to reverse a string word by word.

Input string : 'hello .py'
Expected Output : '.py hello'"""


class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))