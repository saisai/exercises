import traceback
import sys

try:
    raise TypeError("Oups!")
except Exception as err:
    try:
        exc_info = sys.exc_info()

        # do you usefull stuff here
        # (potentially raising an exception)
        try:
            raise TypeError("Again !?!")
        except:
            pass
        # end of useful stuff


    finally:
        # Display the *original* exception
        traceback.print_exception(*exc_info)
        del exc_info
