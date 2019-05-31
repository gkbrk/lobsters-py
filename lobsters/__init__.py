import json
import requests
import typing

class User:
    about: str
    avatar_url: str
    created_at: str
    github_username: str
    invited_by_user: str
    is_admin: bool
    is_moderator: bool
    karma: int
    twitter_username: str
    username: str

    def from_dict(data):
        user = User()

        user.about = data.get('about', '')
        user.avatar_url = data.get('avatar_url', '')
        user.created_at = data.get('created_at', '')
        user.github_username = data.get('github_username', '')
        user.invited_by_user = data.get('invited_by_user', '')
        user.is_admin = data.get('is_admin', False)
        user.is_moderator = data.get('is_moderator', False)
        user.karma = data.get('karma', 0)
        user.twitter_username = data.get('twitter_username', '')
        user.username = data.get('username', '')

        return user


class Story:
    comment_count: int
    created_at: str
    downvotes: int
    score: int
    short_id: str
    short_id_url: str
    title: str
    upvotes: int
    url: str
    user: User
    description: str

    def from_dict(data):
        story = Story()

        story.comment_count = data.get('comment_count')
        story.created_at = data.get('created_at')
        story.downvotes = data.get('downvotes')
        story.score = data.get('score')
        story.short_id = data.get('short_id')
        story.short_id_url = data.get('short_id_url')
        story.title = data.get('title')
        story.upvotes = data.get('upvotes')
        story.url = data.get('url')
        story.user = User.from_dict(data.get('submitter_user', {}))
        story.description = data.get('description')

        return story

class Client:
    def __init__(self, base='https://lobste.rs'):
        self.__base = base
        self.__s = requests.Session()

    def frontpage(self):
        url = self._url('/hottest.json')
        data = self._get_json(url)

        return map(Story.from_dict, data)

    def get_user(self, username) -> User:
        url = self._url(f'/u/{username}.json')
        data = self._get_json(url)

        return User.from_dict(data)

    def _get_json(self, url):
        return self.__s.get(url).json()

    def _url(self, path):
        return f'{self.__base}{path}'
