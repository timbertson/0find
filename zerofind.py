#!/usr/bin/env python

import sys
import zerofind

from zeroinstall import helpers
from zeroinstall import zerostore

def find(url):
	selections = helpers.ensure_cached(url)
	if not selections:
		return None
	selection = selections.selections[url]

	return zerostore.Stores().lookup(selection.id)

if __name__ == '__main__':
	url = sys.argv[1]
	cache_dir = find(url)
	if not cache_dir:
		print >> sys.stderr, "Cancelled."
		sys.exit(1)
	print cache_dir

