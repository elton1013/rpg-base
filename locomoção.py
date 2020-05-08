#A locomoção envolve possibilidade de ordem pratica, ordem politica, e progresso 
#de campanha.
#A locomoção pode vir a influenciar o tempo, onde se locomover de uma cidade a 
#outra pode levar uma fração de dia ou dias.

#um dia é fracionado em 12 períodos
#	3 para noite
#	3 para madrugada
#	3 para dia
#	3 para tarde

#Qualquer localidade é representada por um dicionario.
#A chave é uma string representando um local especifico. O valor correspondente
#é uma tupla ou lista com strings representando os acessos possiveis.

#Ex:
# casa = {'sala1' : ['sala2'],
#         'sala2' : ['sala1', 'sala3']}

#No exemplo acima se tem passagem da 'sala1' para 'sala2'.
#Passagem da 'sala2' para 'sala1' ou 'sala3'.
#A 'sala3' não tem o conjunto de chave e valor, logo se o jogar passar da 'sala2'
#para 'sala3' ficara trancado sem poder progredir no game.

mansao = {
	'hall de entrada' : ('hall superior', 'salão de festas', 'sala de visitas'),
	'hall superior' : ('quarto 1', 'quarto 2', 'quarto 3', 'hall de entrada'),
	'salão de festas' : ('hall de entrada', 'cozinha'),
	'sala de visitas' : ('hall de entrada', 'cozinha'),
	'quarto 1' : ('hall superior',),
	'quarto 2' : ('hall superior',),
	'quarto 3' : ('hall superior',),
	'cozinha' : ('salão de festas', 'sala de visitas'),
}


#localidade é um dicionario de chave:acesso a
#sala é uma string que define a localização atual na localidade
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
