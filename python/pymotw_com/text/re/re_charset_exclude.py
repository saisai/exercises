"""
A character set can also be used to exclude specific characters. The carat (^) means to look for characters that are not in the set following the carat.
"""

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+', 'sequences without -, ., or space')],
)