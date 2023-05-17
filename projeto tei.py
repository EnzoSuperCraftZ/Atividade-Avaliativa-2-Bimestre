player = str(input('Diga o seu nome: '))
print('Um grupo de amigos (Alice, Pietro, Carmen, Júlio, Lucas e {}) vão a uma floresta para acampar por uma semana. Eles preparam suas malas e organizam as coisas.'.format(player))
roupa = input('Você prefere levar uma camisa vermelha ou uma azul? 1 - Vermelha 2 - Azul: ')
if roupa == '1':
    print('Você escolheu levar uma camisa vermelha.')
elif roupa == '2':
    print('Você escolheu levar uma camisa azul.')
else:
    print('Resposta inválida')
    exit()
print('Chegando lá os amigos se separaram para montar as coisas no local. Você ficou encarregado pelas barracas.')
barraca = input('Escolha alguém para te ajudar: ')
print('Você e {} então montam a barraca. Todos vão dormir e de madrugada se ouve um grito.')
investigar = input('Você quer ir investigar?')
if investigar == 'sim' or investigar == 's':
    print('Vocês decidem descobrir de onde veio o grito.')
    print('Descobre-se, então, que o grito veio da cabana do Júlio.')
    print('Entrando na cabana, o grupo encontra o corpo de Júlio com marcas de facadas nas regiões do pescoço, abdômen e coração.')
elif investigar == 'não' or investigar == 'n':
    print('Você decide não investigar, e o grupo vai sem você.')
    print('Na volta, o grupo está horrorizado com a visão que tiveram.')
    print('Alice tenta explicar o que aconteceu, mas começa a chorar. Pietro toma a palavra e explica a você.')
    print('Pietro: A gente encontrou de Júlio com marcas de facadas nas regiões do pescoço, abdômen e coração.')
fugir = input('Você prefere fugir ou investigar? 1 - Fugir 2 - Investigar: ')
if fugir == '1':
    print('Você, então, foge do acampamento.')
    print('Dias depois, chega a você a notícia de que todos os seus amigos foram mortos e você é o principal suspeito.')
    print('Você foi preso. (Final ruim)')
    quit()