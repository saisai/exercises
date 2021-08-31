from scipy import constants

print(dir(constants))

for data in dir(constants):
    print(data, getattr(constants, data))
    print('\n')
