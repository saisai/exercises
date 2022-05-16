
def fun(n):
    if n < 1:
        return
    fun(n - 1)
    fun(n - 3)
    print(n)

fun(5)

