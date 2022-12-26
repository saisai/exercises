for i in range(1, 101):
    root = i ** 0.5
    print("Door %d:" % i, 'open' if root == int(root) else 'close')


print("\n".join(['Door %s is %s' % (i, ('closed', 'open')[(i**0.5).is_integer()]) for i in range(1, 101)  ]))


print("\n".join("Door %s is %s" % (i, 'closed' if i**0.5 % 1 else 'open') for i in range(1, 101)))
