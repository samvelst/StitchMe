# Samvel Stepanyan
# Testing stitchme functions

import unittest
import Image
from .. import __main__

class TestEval(unittest.TestCase):
    def test_get_horizontal_scanlines(self):
        im = Image.open('test.png')
        scans = __main__.get_horizontal_scanlines(im)
        self.assertEquals(im.size[1], len(scans[0]))
        self.assertEquals(im.size[0], len(scans))

