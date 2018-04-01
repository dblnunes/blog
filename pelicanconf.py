#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Nunes'
SITENAME = 'Daniel Nunes'
SITEURL = 'https://dblnunes.github.io/blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Publico', 'https://www.publico.pt/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('github', 'https://github.com/dblnunes'),
          ('twitter', 'https://twitter.com/dbl_nunes'),('mailto', 'mailto:dblnunes@outlook.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', '/Users/daninunes/blog/themes/voce/plugins/assets']
PLUGINS = ['ipynb.markup', 'assets']

OUTPUT_PATH = 'docs/'

THEME = 'themes/voce'

USER_LOGO_URL = '/Users/daninunes/blog/content/images/310logo.png'

STATIC_PATHS = ['/Users/daninunes/blog/content/images']