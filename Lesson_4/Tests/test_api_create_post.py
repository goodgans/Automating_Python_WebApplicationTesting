import pytest
import requests

def test_create_and_check_post(auth_token, config):
    url_posts = config['url_posts']
    headers = {"X-Auth-Token": auth_token}

    post_data = {
        "title": config['default'].get('title_name', 'Default Title'),
        "description": config['default'].get('description_name', 'Default Description'),
        "content": config['default'].get('content_name', 'Default Content')
    }

    create_resp = requests.post(url_posts, headers=headers, json=post_data)
    assert create_resp.status_code in [200, 201], f"Ошибка создания поста: {create_resp.status_code}, ответ: {create_resp.text}"

    get_resp = requests.get(url_posts, headers=headers, params={"owner": "me"})
    assert get_resp.status_code == 200, f"Ошибка получения постов: {get_resp.status_code}, ответ: {get_resp.text}"

    posts = get_resp.json().get("data", [])

    descriptions = [post.get('description') for post in posts]
    assert post_data["description"] in descriptions, "Созданный пост с описанием не найден в списке"
