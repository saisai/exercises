import compileall
import glob

def show(title):
    print(title)
    for filename in glob.glob("./**",
                               recursive=True):
        print('  {}'.format(filename))
    print()

show('Before')

compileall.compile_dir('.')
show('\nAfter')