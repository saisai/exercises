"""
To match the characters that are part of the regular expression syntax, escape the characters in the search pattern.
"""

from re_test_patterns import test_patterns

test_patterns(
    r'\d+ \D+ \s+',
    [(r'\\.\+', 'escape code')],
)