"""
Character Sets
A character set is a group of characters, any one of which can match at that point in the pattern. For example, [ab] would match either a or b.
"""

from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('[ab]', 'either a or b'),
     ('a[ab]+', 'a followed by 1 or more a or b'),
     ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)