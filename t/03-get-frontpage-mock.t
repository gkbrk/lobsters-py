#!/usr/bin/env python3
import sys
sys.path.append('.')

import lobsters
from testsimple import *

c = lobsters.Client()
ok(c)

def get_frontpage(url):
    return [
        {
            'url': 'http://example.com',
            'title': 'Example website',
            'submitter_user': {
                'username': 'leo',
                'is_admin': True
            }
        },
    ]

# Mock HTTP request
c._get_json = get_frontpage

frontpage = list(c.frontpage())
ok(frontpage, 'Got frontpage')

ok(len(frontpage) == 1, 'Story count')

item = frontpage[0]
ok('example.com' in item.url)
ok(item.title == 'Example website')

ok(item.user, 'Item has user')
ok(item.user.username == 'leo')
ok(item.user.is_admin)
ok(not item.user.is_moderator)

done_testing()
