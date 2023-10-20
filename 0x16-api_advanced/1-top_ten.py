#!/usr/bin/python3

"""
This module defines a function to query the Reddit API and
return the first 10 hot posts

Requirements:
- No authentication is necessary for most features of the Reddit API.
- If not a valid subreddit, the function returns 0.
- Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""

import requests


def top_ten(subreddit):
    """
    Retrieves top ten hot posts for a given subreddit
    Args:
        subnreddit(str): subreddit to query
    Return:
        Titles of first 10 hot posts
    """

    # Define API endpoint url
    api_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {'User-Agent': 'Custom User-Agent'}
    # GET request to API
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
