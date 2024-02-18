import inspect 


curframe = inspect.currentframe()
calframe = inspect.getouterframes(curframe)
#with open('check.txt', 'a') as f:
with open('check.txt', 'a') as f:
    f.write("test\n")
    for obj in calframe:
        f.write(str(obj))
        f.write('\n')
print('caller name:', calframe[1][3], calframe[1][2], calframe)
print("aa ", calframe[1][1])
print("aa ", calframe[1][2])
print("aa ", calframe[1][3])
        
def print_location(active=True, offset=0, levels=1, end="\n"):
    import inspect
	if not active:
		return

	for level in range(levels):
		caller_frame_record = inspect.stack()[level + offset + 1]
		frame = caller_frame_record[0]
		info = inspect.getframeinfo(frame)
		file = info.filename
		print('[{}:{} {}()]'.format(file, info.lineno, info.function), end=end)

print_location(levels=3)

def caller_info(skip=2):
    """Get the name of a caller in the format module.class.method.
    Copied from: https://gist.github.com/techtonik/2151727
    :arguments:
        - skip (integer): Specifies how many levels of stack
                          to skip while getting caller name.
                          skip=1 means "who calls me",
                          skip=2 "who calls my caller" etc.
    :returns:
        - package (string): caller package.
        - module (string): caller module.
        - klass (string): caller classname if one otherwise None.
        - caller (string): caller function or method (if a class exist).
        - line (int): the line of the call.
        - An empty string is returned if skipped levels exceed stack height.
    """
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
        return ''
    parentframe = stack[start][0]

    # module and packagename.
    module_info = inspect.getmodule(parentframe)
    if module_info:
        mod = module_info.__name__.split('.')
        package = mod[0]
        module = mod[1]

    # class name.
    klass = None
    if 'self' in parentframe.f_locals:
        klass = parentframe.f_locals['self'].__class__.__name__

    # method or function name.
    caller = None
    if parentframe.f_code.co_name != '<module>':  # top level usually
        caller = parentframe.f_code.co_name

    # call line.
    line = parentframe.f_lineno

    # Remove reference to frame
    # See: https://docs.python.org/3/library/inspect.html#the-interpreter-stack
    del parentframe

    return package, module, klass, caller, line

print(caller_info())

# https://gist.github.com/lee-pai-long/d3004225e1847b84acb4fbba0c2aea91
# https://terokarvinen.com/2015/logging-in-python-with-function-names-line-numbers-command-line-v-d-and-aliases-v-d/
# https://medium.com/@neeraj.online/python-show-file-name-and-line-number-when-calling-print-like-javascript-console-log-eb240d757f9a