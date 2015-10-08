#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://matthewvance.github.io'
RELATIVE_URLS = False

### Feed settings ###
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
AUTHOR_FEED_RSS = None

# Delete the output directory, and all of its contents, before generating new
# files. This can be useful in preventing older, unnecessary files from
# persisting in your output. However, this is a destructive setting and should
# be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True
