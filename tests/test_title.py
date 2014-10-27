# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import unittest

from nose import tools
from lxml import html
from justext.core import ParagraphMaker, justext, get_stoplist, justitle


class TestTitle(unittest.TestCase):
    def test_basic(self):
        s='text and some <em>other</em> words <span class="class">that I</span> have in my head now '
        html_string = (
            '<html><body><title>Header | site.com</title>'
            '<h1>Header</h1>'
            '<p>{0}</p>'
            '<p>text and some <em>other</em> words <span class="class">that I</span> have in my head now</p>'
            '<h2>Smaller header</h2>'
            '<p>footer</p>'
            '</body></html>'
        ).format(s*5)

        pars = justext(html_string, get_stoplist("English"))
        title = justitle(html_string, pars)
        assert title == "Header"

    def test_no_title_tag(self):
        s='text and some <em>other</em> words <span class="class">that I</span> have in my head now '
        html_string = (
            '<html><body>'
            '<h1>Header</h1>'
            '<p>{0}</p>'
            '<p>text and some <em>other</em> words <span class="class">that I</span> have in my head now</p>'
            '<h2>Smaller header</h2>'
            '<p>footer</p>'
            '</body></html>'
        ).format(s*5)
        
        pars = justext(html_string, get_stoplist("English"))
        title = justitle(html_string, pars)
        assert title == "Header"

    def test_no_heading(self):
        html_string = '<html><body><title>Header | site.com</title></body></html>'
        
        pars = justext(html_string, get_stoplist("English"))
        title = justitle(html_string, pars)
        assert title == "Header | site.com"

    def test_no_titles(self):
        s='text and some <em>other</em> words <span class="class">that I</span> have in my head now '
        html_string = (
            '<html><body>'
            '<p>{0}</p>'
            '<p>text and some <em>other</em> words <span class="class">that I</span> have in my head now</p>'
            '<h2>Smaller header</h2>'
            '<p>footer</p>'
            '</body></html>'
        ).format(s*5)

        pars = justext(html_string, get_stoplist("English"))
        title = justitle(html_string, pars)
        assert title == None
