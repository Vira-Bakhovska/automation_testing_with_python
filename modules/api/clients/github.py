import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"http://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def search_users_followers(self, username):
        r = requests.get(f"https://api.github.com/users/{username}/followers")
        body = r.json()

        return body

    def search_lable(self, repository_id, lable):
        r = requests.get(
            "https://api.github.com/search/labels",
            params={"repository_id": repository_id, "q": lable},
        )
        body = r.json()

        return body
