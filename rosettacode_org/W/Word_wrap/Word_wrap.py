import textwrap
print(help(textwrap.fill))

txt = '''\
Reformat the single paragraph in 'text' to fit in lines of no more
than 'width' columns, and return a new string containing the entire
wrapped paragraph.  As with wrap(), tabs are expanded and other
whitespace characters converted to space.  See TextWrapper class for
available keyword args to customize wrapping behaviour.'''
print(textwrap.fill(txt, width=75))

print()
print(textwrap.fill(txt, width=45))

print()
print(textwrap.fill(txt, width=85))