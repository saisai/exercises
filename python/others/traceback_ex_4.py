import traceback
import sys

try:
    do_stuff()
except Exception:
    #print(traceback.format_exc())
    # or
    #print(sys.exc_info()[2])
    traceback.print_exc()
