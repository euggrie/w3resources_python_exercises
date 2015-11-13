

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.



#function = (input(str("Enter function name: "))).lower


built_in = ['any','all','abs','input','open','staticmethod','enumerate''int','ord''str''eval''isinstance','pow''sum'
 'basestring','execfile','issubclass','print','super','bin','file','iter','property''tuple''bool''filter'
 'len','range','type','bytearray','float','list','raw_input','unichr','callable','format''locals''reduce',
 'unicode','chr','frozenset','long','reload','vars','classmethod','getattr','map','repr','xrange','cmp','globals','max',
 'reversed','zip','compile','hasattr','memoryview','round','__import__','complex','hash','min','set','delattr','help',
 'next','setattr','dict','hex','object','slice','dir','id','oct','sorted']

def program(func):
    for i in built_in:
        if func == i:
            print(func.__doc__)

        else:
            pass

program('all')

