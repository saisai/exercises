def identity(size):
    return {(x, y):int(x== y) for x in range(size) for y in range(size)}

size = 4
matrix = identity(4)
print('\n'.join(' '.join(str(matrix[(x,y)]) for x in range(size)) for y in range(size)))