def spam():
    bacon()

def bacon():
    raise Exception('This is an exception message')

# spam()

# We get a Traceback error when the Exception isn't handled
# We can call the func: traceback.format_exc() if we want the 
# information from an exception's traceback but also want an 
# except statement to gracefully handle the exception.


import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

