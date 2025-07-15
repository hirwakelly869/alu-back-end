mport requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers to a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "custom-user-agent-script/0.1"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If response is OK (status code 200), parse JSON
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception:
        return 0
