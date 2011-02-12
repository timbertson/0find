#!/usr/bin/env python

import sys
import os

from zeroinstall import helpers
from zeroinstall import zerostore

def find(url):
	del os.environ['DISPLAY']
	selections = helpers.ensure_cached(url, command=None)
	if not selections:
		return None
	selection = selections.selections[url]

	if selection.id.startswith("package:"):
		print >> sys.stderr, "Package implementation: %s" % (selection.id,)
		return None
	if os.path.exists(selection.id):
		return selection.id
	return zerostore.Stores().lookup_any(selection.digests)

if __name__ == '__main__':
	url = sys.argv[1]
	cache_dir = find(url)
	if not cache_dir:
		print >> sys.stderr, "Failed."
		sys.exit(1)
	print cache_dir

