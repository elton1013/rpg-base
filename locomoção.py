#a locomoção envolve possibilidade de ordem pratica, ordem politica, e progresso de campanha
#a locomoção pode vir a influenciar o tempo, onde se locomover de uma cidade a outra pode levar uma fração de dia ou dias
#uma dia é fracionado em 12 períodos
#	3 para noite
#	3 para madrugada
#	3 para dia
#	3 para tarde

#qual localidade respeita uma estrutura básica de dicionario, onde a chave é seguida por acessos possíveis no momento.

mansao = {
	'hall de entrada' : ('hall superior', 'salão de festas', 'sala de visitas'),
	'hall superior' : ('quarto 1', 'quarto 2', 'quarto 3', 'hall superior'),
	'quarto 1' : ('hall superior',),
	'quarto 2' : ('hall superior',),
	'quarto 3' : ('hall superior',),
	'salão de festas' : ('hall de entrada', 'cozinha'),
	'sala de visitas' : ('hall de entrada', 'cozinha'),
	'cozinha' : ('hall de festas', 'sala de visitas')
}
