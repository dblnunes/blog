#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Daniel Nunes'
SITENAME = u'Daniel Nunes'
SITESUBTITLE = u'Learning Data Science and Machine Learning'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('github', 'https://github.com/dblnunes'),
          ('twitter', 'https://twitter.com/dbl_nunes'))

DEFAULT_PAGINATION = 10

HIDE_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', '/Users/daninunes/blog/plugins/pelican-plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites']

OUTPUT_PATH = 'docs/'

THEME = 'themes/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'sandstone'
BOOTSTRAP_NAVBAR_INVERSE = False
BOOTSTRAP_FLUID = False

SHOW_ARTICLE_CATEGORY = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

STATIC_PATHS = ['images']

SITELOGO = None
SITELOGO_SIZE = None


##

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

##


AVATAR = None

BANNER = "images/kde3.png"
BANNER_SUBTITLE = 'Learning Data Science and Machine Learning'

DISPLAY_ARTICLE_INFO_ON_INDEX = False

SHOW_ARTICLE_CATEGORY = True
TAG_CLOUD_MAX_ITEMS = 8

PYGMENTS_STYLE = 'native'
