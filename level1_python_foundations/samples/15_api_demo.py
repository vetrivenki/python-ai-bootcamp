# 15_api_demo.py
# Level 1 — Topic 15: requests and REST APIs

import requests


def get_github_user(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        print(f"Error {response.status_code}: {response.text[:200]}")
        return {}
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {}


if __name__ == "__main__":
    user = get_github_user("octocat")
    if user:
        print(f"Name         : {user.get('name')}")
        print(f"Public repos : {user.get('public_repos')}")
        print(f"Followers    : {user.get('followers')}")
        print(f"Profile URL  : {user.get('html_url')}")
    else:
        print("Could not fetch user.")

    print("\n# pip install requests")
