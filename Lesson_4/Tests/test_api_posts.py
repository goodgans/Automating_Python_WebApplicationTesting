import requests

def test_get_posts(auth_token):
    url = "https://test-stand.gb.ru/api/posts"
    headers = {"X-Auth-Token": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200