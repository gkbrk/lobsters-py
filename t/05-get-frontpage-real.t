#!/usr/bin/env python3
import sys
sys.path.append('.')

import lobsters
from testsimple import *

plan(tests=6)

diag('This tests requires an internet connection')

c = lobsters.Client()
ok(c)

frontpage = c.frontpage()
ok(frontpage)

frontpage = list(frontpage)

ok(len(frontpage) > 0)

first = frontpage[0]
ok(first)
ok(first.title)
ok(first.url)
