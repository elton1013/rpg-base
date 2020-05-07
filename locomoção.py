#a locomoção envolve possibilidade de ordem pratica, ordem politica, e progresso de campanha
#a locomoção pode vir a influenciar o tempo, onde se locomover de uma cidade a outra pode levar uma fração de dia ou dias
#uma dia é fracionado em 12 períodos
#	3 para noite
#	3 para madrugada
#	3 para dia
#	3 para tarde

#qualquer localidade respeita uma estrutura básica de dicionario, onde a chave é seguida por acessos possíveis no momento.

mansao = {
	'hall de entrada' : ('hall superior', 'salão de festas', 'sala de visitas'),
	'hall superior' : ('quarto 1', 'quarto 2', 'quarto 3', 'hall de entrada'),
	'salão de festas' : ('hall de entrada', 'cozinha'),
	'sala de visitas' : ('hall de entrada', 'cozinha'),
	'quarto 1' : ('hall superior',),
	'quarto 2' : ('hall superior',),
	'quarto 3' : ('hall superior',),
	'cozinha' : ('salão de festas', 'sala de visitas')
}


#localidade é um dicionario de chave:acesso para
#sala é a chave que define o ponto de entrada inicial na localidade
def explorar(localidade, sala):
    while 1:
        print(f'\nvoce esta aqui > {sala}')
        for pos, i in enumerate(localidade[sala]):
            print(pos, i)
        try:
            escolha = int(input('para onde? : '))
            sala = localidade[sala][escolha]
        except:
            break



if __name__ == '__main__':
    explorar(mansao, 'hall de entrada')
