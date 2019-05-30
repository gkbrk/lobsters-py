#!/usr/bin/env python3
import sys
sys.path.append('.')

import lobsters
from testsimple import *

plan(tests=4)

ok(lobsters.Client, 'Found Client class')

c = lobsters.Client()

ok(c, 'Constructor')
ok(c.frontpage, 'Frontpage exists')
ok(c.get_user, 'get_user exists')
