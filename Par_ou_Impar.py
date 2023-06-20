entrada = input(str('Digite um número inteiro: '))
try:
    conta = int(entrada) % int(2) == int(0)
    texto = str('impar')
    if conta is True:
        texto = str('par')
    print(str(f'O número {int(entrada)} é {str(texto)}.'))
except ValueError:
    if str(entrada) == str('NASA'):
        print(str('Código secreto ativado!'))
    else:
        print(str('Digite um número inteiro válido!'))

# Testando tipagem str, int, etc.