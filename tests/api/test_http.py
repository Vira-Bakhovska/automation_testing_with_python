import pytest
import requests
import json


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get("http://api.github.com/users/defunkt")
    ascii_content = r.text.encode("ascii", "ignore").decode("ascii")
    body = r.json()
    heders = r.headers

    assert body["name"] == "Chris Wanstrath"
    assert r.status_code == 200
    assert heders["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    r = requests.get("http://api.github.com/users/sergii_butenko")

    assert r.status_code == 404
