import pytest
from libpythonpro.spam.spam.db import Conexao
from libpythonpro.spam.spam.modelos import Usuario


@pytest.fixture()
def conexao():
    # setup
    conexao_obj =  Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()

@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Andre')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Andre'), Usuario(nome='Dani')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
