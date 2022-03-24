from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/16453890?v=4'
    resp_mock.json.return_value = {
        'login': 'gelhen',
        'id': 16453890,
        'node_id': 'MDQ6VXNlcjE2NDUzODkw',
        'avatar_url': url
    }
    # guarda o get original para isolar o teste
    get_original = github_api.requests.get
    # pega o objeto original e mocka ele
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_busca_avatar(avatar_url):
    url = github_api.buscar_avatar('gelhen')
    assert avatar_url == url


def test_busca_avatar_integracao():
    url = github_api.buscar_avatar('gelhen')
    assert 'https://avatars.githubusercontent.com/u/16453890?v=4' == url
