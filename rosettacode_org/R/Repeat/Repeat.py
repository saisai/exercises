
def repeat(f, n):
    for i in range(n):
        f()

def procedure():
    print("Example")

repeat(procedure, 5)