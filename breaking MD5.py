import string
import secrets
def gerar_senha(comprimento=12):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    return senha
senha_segura = gerar_senha(16)
print(f'Senha gerada: {senha_segura}')
