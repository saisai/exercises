def is_numeric(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False

print(is_numeric('123.0'))


print('123'.isdigit())
