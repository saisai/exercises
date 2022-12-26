
def sum_of_global_int_vars():
    variables = vars(__builtins__).copy()
    variables.update(globals())
    #print(sum(v for v in variables.items() if type(v) == int))
    for v in variables.items():
        print(v)

sum_of_global_int_vars()

