import traceback
import sys

from traceback_example import produce_exception

try:
    produce_exception()
except Exception as err:
    print('print_exception():')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print('exc_type ', exc_type)
    print('exc_value ', exc_value)
    print('exc_tb ', exc_tb)
    traceback.print_exception(exc_type, exc_value, exc_tb)