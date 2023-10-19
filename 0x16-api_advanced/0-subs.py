#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Define API endpoint url
    api_url = "https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'Custom User-Agent'}
    # GET request to API
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        num = data['data']['subscribers']
        return num
    else:
        return 0
