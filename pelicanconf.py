#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Nunes'
SITENAME = 'Daniel Nunes'
SITESUBTITLE = 'Learning Data Science and Machine Learning'
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

PLUGIN_PATHS = ['./plugins', '/Users/daninunes/blog/plugins/pelican-plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites']

OUTPUT_PATH = 'docs/'

THEME = 'themes/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'
SHOW_ARTICLE_CATEGORY = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

STATIC_PATHS = ['images']

SITELOGO = 'content/images/310logo.png'
SITELOGO_SIZE = 32


##

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

##

ABOUT_ME = "I'm a programmer and engineer with a love for Python. I enjoy testing odd hypotheses, investigating datasets, and creating rad graphs.\
<p>Find out more about me at <strong><a href=\"http://tylerhartley.com\" title=\"Professional Website\">tylerhartley.com</a></strong></p>\
<p>You can also contact me " + """<a href="http://www.google.com/recaptcha/mailhide/d?k=01viQ7or9YI4gJ8hto_vDniA==&amp;c=PFSG4q4HL4celXjwzCtAo6YzW_WP9gWcjNfpI6f3Gxw=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\07501viQ7or9YI4gJ8hto_vDniA\75\75\46c\75PFSG4q4HL4celXjwzCtAo6YzW_WP9gWcjNfpI6f3Gxw\075', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address"><strong>here</strong></a></p>"""
AVATAR = "/images/headshot.png"

BANNER = "/images/banner.png"

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

PYGMENTS_STYLE = 'monokai'

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'