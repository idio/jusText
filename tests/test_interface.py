# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import unittest

from nose import tools
from lxml import html
from justext.core import ParagraphMaker, justext, get_stoplist, justitle
from justext.core import JustextMalformedInput
from justext.core import preprocessor, html_to_dom


content='text and some <em>other</em> words <span class="class">that I</span> have in my head now '
html_string = (
    '<html><body><title>Header | site.com</title>'
    '<h1>Header</h1>'
    '<p>{0}</p>'
    '<p>text and some <em>other</em> words <span class="class">that I</span> have in my head now</p>'
    '<h2>Smaller header</h2>'
    '<p>footer</p>'
    '</body></html>'
).format(content*5)

class TestTitle(unittest.TestCase):
    def test_accepts_string(self):
        try:
            justext(html_string, get_stoplist("English"))
        except JustextMalformedInput:
            self.fail("justext wasn't supposed to raise JustextMalformedInput exception on string")

    def test_accepts_html_tree(self):
        try:
            justext(html_to_dom(html_string), get_stoplist("English"))
        except JustextMalformedInput:
            self.fail("justext wasn't supposed to raise JustextMalformedInput exception on string")


    def test_raises_malformed_input(self):       
        self.assertRaises(JustextMalformedInput, justext, 80085, get_stoplist("English"))
