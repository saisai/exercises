"""
As character sets grow larger, typing every character that should (or should not) match becomes tedious. A more compact format using character ranges can be used to define a character set to include all of the contiguous characters between the specified start and stop points.
"""

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[a-z]+', 'sequences of lowercase letters'),
     ('[A-Z]+', 'sequences of uppercase letters'),
     ('[a-zA-Z]+', 'sequences of letters of either case'),
     ('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
)