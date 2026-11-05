import requests

usernames = ["LaibaMir1", "Faraz-oop", "mobeen0"]

for username in usernames:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    # Only read the data if the request succeeded
    if response.status_code == 200:
        data = response.json()
        print(f"{data['login']}: {data['public_repos']} public repos")
    else:
        print(f"Could not fetch {username} (status code {response.status_code})")