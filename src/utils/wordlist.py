#!/usr/bin/env python3

"""
MIT License

Copyright (c) 2021 Ygor Simões

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from src.core.color import Color


class Wordlist:
    def __init__(self, args):
        self._wordlist = args.wordlist

    def run(self):
        """Opens the text files containing the wordlist."""

        if self._wordlist == "1":
            wordlist_text = open(os.path.realpath("extra/wordlists/small.txt"), 'r')
            Color.println("{+} Wordlist Small: 'extra/wordlists/small.txt'")

        elif self._wordlist == "2":
            wordlist_text = open(os.path.realpath("extra/wordlists/medium.txt"), 'r')
            Color.println("{+} Wordlist Medium: 'extra/wordlists/medium.txt'")

        elif self._wordlist == "3":
            wordlist_text = open(os.path.realpath("extra/wordlists/big.txt"), 'r')
            Color.println("{+} Wordlist Big: 'extra/wordlists/big.txt'")

        else:
            Color.println("{+} Wordlist Alternative: %s" % self.run())
            wordlist_text = open(self._wordlist, 'r')

        wordlist = wordlist_text.readlines()
        wordlist_text.close()

        # Returns the selected wordlist.
        return wordlist
