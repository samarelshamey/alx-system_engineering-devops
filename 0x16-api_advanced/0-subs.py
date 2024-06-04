#!/usr/bin/python3
"""return reddit subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        return data['data']['subscribers']
    except (requests.RequestException, KeyError):
        return 0
