#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2026  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damenltk; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import nltk
from nltk.corpus import cmudict
from src.syllable import Syllable

class TddInPythonExample(unittest.TestCase):

    def test_syllable_count_syllables(self):
        sy = Syllable()
        n1 = sy.count_syllables("David")
        self.assertEqual(n1, 2)
        n2 = sy.count_syllables("Maria")
        self.assertEqual(n2, 2)
        n3 = sy.count_syllables("Gerónimo")
        self.assertEqual(n3, 3)
