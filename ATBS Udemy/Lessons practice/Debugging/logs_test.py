#Basic logging type in python
import logging
logging.basicConfig(level=logging.DEBUG,
        format = "%(asctime)s - %(levelname)s - %(message)s")

'''There are 5 log level
-- logging.debug(), info(), warning(), error(), critical()

the below will diable all logging type if applied
logging.disable(logging.critical)
'''

print('--------')

def factorial(n):
    logging.info('start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.info('Return value is %s' % (total))
    return total

print(factorial(5))
logging.info('End Of Program')


print('-----------')
