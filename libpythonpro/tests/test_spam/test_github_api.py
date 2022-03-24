from unittest.mock import Mock

from libpythonpro import github_api


def test_busca_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'gelhen',
        'id': 16453890,
        'node_id': 'MDQ6VXNlcjE2NDUzODkw',
        'avatar_url': 'https://avatars.githubusercontent.com/u/16453890?v=4'
    }
    #pega o objeto original e mocka ele
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('gelhen')
    assert 'https://avatars.githubusercontent.com/u/16453890?v=4' == url
