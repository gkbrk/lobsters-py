#!/usr/bin/env python3
import sys
sys.path.append('.')

import lobsters
from testsimple import *

plan(tests=7)

c = lobsters.Client()
ok(c)

def get_user(url):
    return {
        'username': 'gkbrk',
        'twitter_username': '0xGKBRK',
        'is_moderator': True,
        'karma': 1234,
    }

# Mock HTTP request
c._get_json = get_user

user = c.get_user('gkbrk')
ok(user, 'Got user')
ok(user.username == 'gkbrk', 'Username matches')
ok(user.twitter_username == '0xGKBRK', 'Twitter username matches')
ok(user.is_moderator, 'Moderator')
ok(not user.is_admin, 'Not admin')
ok(user.karma == 1234, 'Karma matches')
