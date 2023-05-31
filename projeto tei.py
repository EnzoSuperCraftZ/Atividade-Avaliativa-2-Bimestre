player = str(input('Diga o seu nome: '))
from pickle import POP
import time
print('Um grupo de amigos (Alice, Pietro, Carmen, Júlio, Lucas e {}) vão a uma floresta para acampar por uma semana. Eles preparam suas malas e organizam as coisas.'.format(player))
time.sleep(3)
roupa = 0
while roupa == 0:
    roupa = input('Você prefere levar uma camisa vermelha ou uma azul? 1 - Vermelha 2 - Azul: ')
    if roupa == '1':
        print('Você escolheu levar uma camisa vermelha.')
        break
    elif roupa == '2':
        print('Você escolheu levar uma camisa azul.')
        break
    else:
        print('Resposta inválida (Responda "sim" ou "não")')
time.sleep(3)
print('Chegando lá os amigos se separaram para montar as coisas no local. Você ficou encarregado pelas barracas.')
time.sleep(3)
barraca = input('Escolha alguém para te ajudar: ')
print('Você e {} então montam a barraca. Todos vão dormir e de madrugada se ouve um grito.'.format(barraca))
investigar = 1
while investigar != 0:
    investigar = str.upper(input('Você quer ir investigar? '))
    if investigar == 'SIM' or investigar == 'S':
        print('Vocês decidem descobrir de onde veio o grito.')
        time.sleep(3)
        print('Descobre-se, então, que o grito veio da cabana do Júlio.')
        time.sleep(3)
        print('Entrando na cabana, o grupo encontra o corpo de Júlio com marcas de facadas nas regiões do pescoço, abdômen e coração.')
        time.sleep(5)
        break
    elif investigar == 'não' or investigar == 'n':
        print('Você decide não investigar, e o grupo vai sem você.')
        time.sleep(3)
        print('Na volta, o grupo está horrorizado com a visão que tiveram.')
        time.sleep(3)
        print('Alice tenta explicar o que aconteceu, mas começa a chorar. Pietro toma a palavra e explica a você.')
        time.sleep(3)
        print('Pietro: A gente encontrou de Júlio com marcas de facadas nas regiões do pescoço, abdômen e coração.')
        time.sleep(3)
        break
    else:
        print('Resposta inválida')
fugir = input('Você prefere fugir ou ir mais afundo? 1 - Fugir 2 - Investigar: ')
if fugir == '1':
    print('Você, então, foge do acampamento.')
    time.sleep(3)
    print('Dias depois, chega a você a notícia de que todos os seus amigos foram mortos e você é o principal suspeito.')
    time.sleep(5)
    print('Você foi preso. (Final ruim)')
    quit()
elif fugir == '2':
    print('Você então começa a suspeitar de seus amigos, e decide questioná-los.')
    time.sleep(3)
    suspeito = str.upper(input('Para quem você se dirige primeiro? '))
    def escolher ():
        suspeito = 1
        while suspeito != 0:
            if suspeito == 'ALICE':
                print('Você interroga Alice.') 
                time.sleep(3)
                print('Ela começa a chorar, te questionando o porquê de você suspeitar dela, e diz que só queria um final de semana em paz com os amigos.')
                time.sleep(3)
                break
            elif suspeito == 'LUCAS':
                print('Você interroga Lucas.')
                time.sleep(3)
                print('Ele começa a te xingar de tudo que é nome, e diz que você é um idiota por achar que ele é o assasino.')
                time.sleep(3)
                break
            elif suspeito == 'CARMEN':
                print('Você interroga Carmen.')
                time.sleep(3)
                print('Ela diz que seria impossível, porque ela possui uma grande intimidade com todo o grupo.')
                time.sleep(3)
                break
            elif suspeito == 'PIETRO':
                print('Você interroga Pietro.')
                time.sleep(3)
                print('Pietro se desespera mais ainda, com medo de ser o próximo, e afirma à você que não foi ele.')
                time.sleep(3)
                break
            else:
                print('Resposta inválida')
    escolher()
suspeito = input('Qual será o próximo a ser interrogado? ')
escolher()
suspeito = input('Qual será o próximo a ser interrogado? ')
escolher()
suspeito = input('E por último: ')
escolher()
    