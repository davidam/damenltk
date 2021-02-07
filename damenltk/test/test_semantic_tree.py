#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2021  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with damenltk; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import nltk
from nltk import CFG

class TddInPythonExample(unittest.TestCase):

    def test_semantic_tree_returns_correct_result(self):
        grammar = CFG.fromstring("""
        S -> NP VP
        PP -> P NP
        NP -> Det N | NP PP
        VP -> V NP | VP PP
        Det -> 'a' | 'the'
        N -> 'dog' | 'cat'
        V -> 'chased' | 'sat'
        P -> 'on' | 'in'
        """)
        self.assertEqual(str(grammar.start()), 'S')
        self.assertEqual("[S -> NP VP, PP -> P NP, NP -> Det N, NP -> NP PP, VP -> V NP, VP -> VP PP, Det -> 'a', Det -> 'the', N -> 'dog', N -> 'cat', V -> 'chased', V -> 'sat', P -> 'on', P -> 'in']", str(grammar.productions()))
    
    
