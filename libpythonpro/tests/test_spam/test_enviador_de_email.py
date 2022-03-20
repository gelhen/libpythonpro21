import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['ti@tozzoalimentos.com.br', 'gelhen@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    destinatario = 'gelhen@gmail.com'
    resultado = enviador.enviar(
        remetente,
        destinatario,
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'gelhen']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    destinatario = 'gelhen@gmail.com'
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            destinatario,
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
