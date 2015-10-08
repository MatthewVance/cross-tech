#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matthew Vance'
SITENAME = u'Cross Tech'
SITEURL = ''

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'miscellaneous'
# If disabled, content with dates in the future will get a default status of
# draft.
WITH_FUTURE_DATES = True
#If fs, Pelican will use the file system timestamp information (mtime) if it
# can’t get date information from the metadata.
DEFAULT_DATE = 'fs'


### Apperance ###
ARTICLE_ORDER_BY = 'reversed-date'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
NEWEST_FIRST_ARCHIVES = True
PAGE_ORDER_BY = 'basename'
REVERSE_CATEGORY_ORDER = False
SUMMARY_MAX_LENGTH = 50
TYPOGRIFY = True


## Themes ##
# pelican-svbhack #
THEME = "/home/matt/dev/repos/github.com/MatthewVance/pelican-svbhack"
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']


### Feed Settings ###
# Feed generation is usually not desired when developing
# override for published version in publishconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


### Local Settings ###
DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'
TIMEZONE = 'America/Chicago'
#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'


### Pagination Settings ###
DEFAULT_PAGINATION = 5
# the first page will just be /, and
# the second (and subsequent) pages will be /page/2/, etc.
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


### Path settings ###
# static paths will be copied without parsing their contents
OUTPUT_PATH = 'output/'
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = [
    'downloads',
    'extra/favicon.ico',
    'extra/robots.txt',
    'images',
    ]
# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    }


### Social Settings ###
# Social widget
#SOCIAL = (('GitHub', 'https://github.com/MatthewVance'),
#          ('LinkedIn', 'https://www.linkedin.com/in/mattvance'),
#          ('Twitter', 'https://twitter.com/vancematthew'),)

#It will use this information to create a GitHub ribbon.
GITHUB_URL = 'https://github.com/matthewvance/'

# Allows supporting themes to add a tweet button to articles
TWITTER_USERNAME = 'VanceMatthew'


### URL Settings ###
# the slug, use the article's file name when creating the slug
SLUGIFY_SOURCE = 'basename'
# Uncomment following line if you want document-relative
# URLs when developing #RELATIVE_URLS = True # When automatically generating
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives.html'
# If you do not want one or more of the default pages to be created (e.g., you
# are the only author on your site and thus do not need an Authors page), set
# the corresponding *_SAVE_AS setting to '' to prevent the relevant page from
# being generated.
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
