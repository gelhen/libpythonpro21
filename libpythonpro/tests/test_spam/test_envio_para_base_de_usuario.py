from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    
    enviador_de_spam.enviar_emails(
        'gelhen@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )