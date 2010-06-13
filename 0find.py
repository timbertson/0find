#!/usr/bin/env python

import sys

from zeroinstall import helpers
from zeroinstall import zerostore

url = sys.argv[1]
selections = helpers.ensure_cached(url)
if not selections:
	print >> sys.stderr, "Cancelled."
	sys.exit(1)
selection = selections.selections[url]

cache_dir = zerostore.Stores().lookup(selection.id)
print cache_dir
