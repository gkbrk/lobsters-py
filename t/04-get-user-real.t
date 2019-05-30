#!/usr/bin/env python3
import sys
sys.path.append('.')

import lobsters
from testsimple import *

plan(tests=6)

diag('This tests requires an internet connection')

c = lobsters.Client()
ok(c)

user = c.get_user('gkbrk')
ok(user, 'Got user')
ok(user.username == 'gkbrk', 'Username matches')
ok(not user.is_admin, 'Not an admin')
ok(not user.is_moderator, 'Not a moderator')
ok(user.karma > 0)
