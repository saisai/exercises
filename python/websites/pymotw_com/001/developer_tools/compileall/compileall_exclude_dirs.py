import compileall
import re

compileall.compile_dir(
    '.',
    rx=re.compile(r'./')
)