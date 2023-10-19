#!/usr/bin/python3

"""
Reddit API Subreddit Subscriber Count
This module defines a function to query the Reddit API and
return the number of subscribers for a given subreddit.

Requirements:
- No authentication is necessary for most features of the Reddit API.
- If not a valid subreddit, the function returns 0.
- Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves number of subscribers from a given subreddit
    Args:
        subnreddit(str): subreddit to query
    Return:
        Number of subscribers or 0 if subreddit is invalid
    """
    # Define API endpoint url
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'Custom User-Agent'}
    # GET request to API
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        num = data['data']['subscribers']
        return num
    else:
        return 0
