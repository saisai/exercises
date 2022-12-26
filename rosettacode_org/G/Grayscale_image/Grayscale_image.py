# String masquerading as ppm file (version P3)
import io

from collections import namedtuple
from copy import copy

Colour = namedtuple('Colour', 'r,g,b')
Colour.copy = lambda self: copy(self)

black = Colour(0, 0, 0)
white = Colour(255, 255, 255)  # Colour ranges are not enforced.


class Bitmap():
    def __init__(self, width=40, height=40, background=white):
        assert width > 0 and height > 0 and type(background) == Colour
        self.width = width
        self.height = height
        self.background = background
        self.map = [[background.copy() for w in range(width)] for h in range(height)]

    def fillrect(self, x, y, width, height, colour=black):
        assert x >= 0 and y >= 0 and width > 0 and height > 0 and type(colour) == Colour
        for h in range(height):
            for w in range(width):
                self.map[y + h][x + w] = colour.copy()

    def chardisplay(self):
        txt = [''.join(' ' if bit == self.background else '@'
                       for bit in row)
               for row in self.map]
        # Boxing
        txt = ['|' + row + '|' for row in txt]
        txt.insert(0, '+' + '-' * self.width + '+')
        txt.append('+' + '-' * self.width + '+')
        print('\n'.join(reversed(txt)))

    def set(self, x, y, colour=black):
        assert type(colour) == Colour
        self.map[y][x] = colour

    def get(self, x, y):
        return self.map[y][x]

ppmfileout = io.StringIO('')


def togreyscale(self):
    for h in range(self.height):
        for w in range(self.width):
            r, g, b = self.get(w, h)
            l = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            self.set(w, h, Colour(l, l, l))


Bitmap.togreyscale = togreyscale


def writeppmp3(self, f):
    self.writeppm(f, ppmformat='P3')


def writeppm(self, f, ppmformat='P6'):
    assert ppmformat in ['P3', 'P6'], 'Format wrong'
    magic = ppmformat + '\n'
    comment = '# generated from Bitmap.writeppm\n'
    maxval = max(max(max(bit) for bit in row) for row in self.map)
    assert ppmformat == 'P3' or 0 <= maxval < 256, 'R,G,B must fit in a byte'
    if ppmformat == 'P6':
        fwrite = lambda s: f.write(bytes(s, 'UTF-8'))
        maxval = 255
    else:
        fwrite = f.write
        numsize = len(str(maxval))
    fwrite(magic)
    fwrite(comment)
    fwrite('%i %i\n%i\n' % (self.width, self.height, maxval))
    for h in range(self.height - 1, -1, -1):
        for w in range(self.width):
            r, g, b = self.get(w, h)
            if ppmformat == 'P3':
                fwrite('   %*i %*i %*i' % (numsize, r, numsize, g, numsize, b))
            else:
                fwrite('%c%c%c' % (r, g, b))
        if ppmformat == 'P3':
            fwrite('\n')


Bitmap.writeppmp3 = writeppmp3
Bitmap.writeppm = writeppm



# Draw something simple
bitmap = Bitmap(4, 4, white)
bitmap.fillrect(1, 0, 1, 2, Colour(127, 0, 63))
bitmap.set(3, 3, Colour(0, 127, 31))
print('Colour:')
# Write to the open 'file' handle

bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())
print('Grey:')
bitmap.togreyscale()
ppmfileout = io.StringIO('')
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())
