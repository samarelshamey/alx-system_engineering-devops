#!/usr/bin/python3
"""returns a list of the titles of all articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, params=params,
                                headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for post in children:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        return None
