import traceback

try:
    raise TypeError("Oups!")
except Exception as err:
    try:
        raise TypeError("Again !?!")
    except:
        pass

    traceback.print_exc()
