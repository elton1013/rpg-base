#comandos perminte acesso a menus e ações no geral

def invalido(*args, **kwargs):
    input('Comando ou opções invalidas.\nTecle ENTER...')
    return 0

def aviso(*args, **kwargs):
    input('Falta implementar.\nTecle ENTER...')

def main():
    #setup
    menu_principal = {
            'STATUS' : aviso,
            'MOVER' : aviso,
            'INSPECIONAR' : aviso,
            'USAR' : aviso,
            'EQUIPAR' : aviso,
            'PEGAR' : aviso,
            'CONVERSAR' : aviso,
            'SALVAR' : aviso,
            'QUIT' : exit,
            }

    #game
    while 1:
        print('\n', *menu_principal.keys())
        entrada = input('> ').upper().split()

        if len(entrada) > 1:
            comando, *opcoes = entrada

        elif entrada:
            comando = entrada[0]
            opcoes = None

        else:
            invalido()
            continue

        escolhido = menu_principal.get(comando, invalido)
        retorno = escolhido(opcoes)


if __name__ = '__main__':
    main()
