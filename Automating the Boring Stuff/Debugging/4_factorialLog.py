#! python3

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# To disable the log messages we call this funtion below so we
# don't have to go removing all the logging calls by hand. 
logging.disable(logging.CRITICAL)

logging.debug('Start of Program')

def factorial(n):
    
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1

    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of Program')

# Logging Levels
# These levels are just suggestions. It's up to us to ultimately
# decide which category the mssage belongs to. 
# 1) logging.debug()
# 2) logging.info()
# 3) logging.warning()
# 4) logging.error()
# 5) logging.critical()

# Note: passing the logging.DEBUG to the basicConfig() 
# function will show messages from all logging levels. But
# passing the logging.ERROR will only shoe ERROR and 
# CRITICAL messages and skip the DEBUG, INFO and WARNING 
# messages.

# We could also save log messages to a text file instead of 
# displaying it to the screen. We could do that like so:
# logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') 
 