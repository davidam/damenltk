#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

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
# along with damenltk; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from nltk.corpus import cmudict
import string


class Syllable(object):
    
    def count_syllables(self, word):
        vowels = "aeiouy"
        numVowels = 0
        lastWasVowel = False
        for wc in word:
            foundVowel = False
            for v in vowels:
                if v == wc:
                    if not lastWasVowel: numVowels+=1 #don't count diphthongs
                    foundVowel = lastWasVowel = True
                if not foundVowel: #If full cycle and no vowel found, set lastWasVowel to false
                    lastWasVowel = False
        if len(word) > 2 and word[-2:] == "es": #Remove es - it's "usually" silent (?)
            numVowels-=1
        elif len(word) > 1 and word[-1:] == "e": #remove silent e
            numVowels-=1
        return numVowels

    
