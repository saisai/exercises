import traceback
import re

def called_from_main_shield():
    print("Calling introspect")
    tb = traceback.extract_stack()
    print(traceback.format_stack())
    print(f"line={tb[0].line} lineno={tb[0].lineno} file={tb[0].filename}")
    try:
        with open(tb[0].filename, mode="rt") as f:
            found_main_shield = False
            for i, line in enumerate(f):
                if re.search(r"__name__.*['\"]__main__['\"]", line):
                    found_main_shield = True
                if i == tb[0].lineno:
                    print(f"found_main_shield={found_main_shield}")
                    return found_main_shield
    except:
        print("Coulnd't inspect stack, let's pretend the code is OK...")
        return True

print(called_from_main_shield())

if __name__ == "__main__":
    print(called_from_main_shield())
    
    #