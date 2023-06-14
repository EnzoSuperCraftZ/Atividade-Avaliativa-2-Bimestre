#INSTITUTO FEDERAL - CAMPUS PORTO VELHO CALAMA 

#INTEGRANTES DO GRUPO:
#ANA CLARA
#ENZO KAIL
#KEREN HAPUC
#PAULO GABRIEL 

#parte do enzo

player = str(input('Diga o seu nome: '))
from ast import Delete
from pickle import POP
import time
from winreg import DeleteKey
print('Um grupo de amigos (Alice, Pietro, Carmen, Júlio, Lucas e {}) vão a uma floresta para acampar por uma semana. Eles preparam suas malas e organizam as coisas.'.format(player))
time.sleep(3)
roupa = 0
while roupa != 0:
    roupa = input('Você prefere levar uma camisa vermelha ou uma azul? 1 - Vermelha 2 - Azul: ')
    if roupa == '1':
        print('Você escolheu levar uma camisa vermelha.')
        break
    elif roupa == '2':
        print('Você escolheu levar uma camisa azul.')
        break
    else:
        print('Resposta inválida')
        
time.sleep(3)
print('Chegando lá os amigos se separaram para montar as coisas no local. Você ficou encarregado pelas barracas.')
time.sleep(3)
barraca = input('Escolha alguém para te ajudar: ')
print('Você e {} então montam a barraca. Todos vão dormir e de madrugada se ouve um grito.'.format(barraca))

#parte do paulo

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
    elif investigar == 'NÃO' or investigar == 'N' or investigar == 'NAO':
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

#parte da keren

fugir = 1
while fugir != 0:
    fugir = input('Você prefere fugir ou ir mais afundo? 1 - Fugir 2 - Investigar: ')
    if fugir == '1':
        print('Você, então, foge do acampamento.')
        time.sleep(3)
        print('Dias depois, chega a você a notícia de que todos os seus amigos foram mortos e você é o principal suspeito.')
        time.sleep(5)
        print('Você foi preso.\nFINAL ALTERNATIVO')
        quit()
    elif fugir == '2':
        print('Você então começa a suspeitar de seus amigos, e decide questioná-los.')
        time.sleep(3)
        lista = ['alice','lucas','carmen','pietro']
        suspeito = str.upper(input('Para quem você se dirige primeiro? '))
        break
    else:
        print('Resposta inválida')

#parte do enzo

def escolher():
    while suspeito != 0:
        if suspeito == 'ALICE':
            print('Você interroga Alice.') 
            time.sleep(3)
            print('Ela começa a chorar, te questionando o porquê de você suspeitar dela, e diz que só queria um final de semana em paz com os amigos.')
            break
        elif suspeito == 'LUCAS':
            print('Você interroga Lucas.')
            time.sleep(3)
            print('Ele começa a te xingar de tudo que é nome, e diz que você é um idiota por achar que ele é o assasino.')
            break
        elif suspeito == 'CARMEN':
            print('Você interroga Carmen.')
            time.sleep(3)
            print('Ela diz que seria impossível, porque ela possui uma grande intimidade com todo o grupo.')
            break
        elif suspeito == 'PIETRO':
            time.sleep(3)
            print('Pietro se desespera mais ainda, com medo de ser o próximo, e afirma à você que não foi ele.')
            time.sleep(3) 
            break
        else:
            print('Resposta inválida')
            escolher()
            
escolher()
suspeito = str.upper(input('Qual será o próximo a ser interrogado? '))
escolher()
suspeito = str.upper(input('Qual será o próximo a ser interrogado? '))
escolher()
suspeito = str.upper(input('E por último: '))
escolher()
print('Você se reconcilia, e se lembra que não tem como o grupo sair dalí, já que foram deixados no acampamento pela mãe de Pietro, que só volta em uma semana.')
time.sleep(3)
print('De noite, enquanto você está se preparando para dormir, alguém bate na porta.')
time.sleep(3)
print('Era Alice que, desesperada, veio pedir para dormir com você.')
time.sleep(3)
print('No dia seguinte, o grupo acorda com uma grave notícia.')
time.sleep(3)
print('Carmen foi enforcada em uma das árvores do acampamento.')
time.sleep(3)

#parte da ana 

print ("Alice desaba de chorar pois Carmen era sua melhor amiga.")
time.sleep(3)
print ("Lucas fica agressivo e começa a gritar com todos, chegando a dar um tapa na cara de Alice.")
time.sleep(3)
pergunta6 = 1
while pergunta6 != 0:
    pergunta6=input ("1 - Segurar Lucas? 2 - Deixar ele extravazar de raiva? ")
    if pergunta6 == '1':
        print ("Lucas se acalma e começa a chorar.")
        break
    elif pergunta6 == '2':
        print ("Lucas vai para o mato o pra se acalmar.")
        time.sleep(3)
        print ("Depois de um tempo, Lucas volta mais calmo.")
        time.sleep(3)
        break
    else:
        print("Resposta inválida")
print ("Passou um certo tempo sem nada de diferente acontecer.")
time.sleep(3)
print ("Depois de um tempo você encontra Alice escrevendo em seu diário com cadeado e escondendo a chave em baixo de sua mala.")
time.sleep(3)
print ("Mais uma noite se passou, e pela manhã, quando os colegas se levantaram, Pietro que sempre era o primeiro a acordar não estava aparecendo em lugar nenhum,")
time.sleep(3)
print ("até que você foi para o banheiro e ali se depara com a cabeça de Pietro decepada ao lado de seus membros.")
time.sleep(3)
print ("As coisas fica bem sinistras naquele momento.")
time.sleep(3)
print ("Lucas acusa Alice com todas as suas forças, mas Alice revida com válidos argumentos.")
time.sleep(3)
print ("você pede para os dois se acalmarem e diz que vai investigar mais a fundo.")
time.sleep(3)
print ("enquanto Alice estava caçando lenha para a fogueira, Lucas estava pescando.")
time.sleep(3)
print ("você pega a chave e começa a ler o diário de Alice, algumas folhas estavam rasgadas e não havia nada de diferente além do romance que ela sentia por você.")
time.sleep(3)
print ("Mas vasculhando a tenda de Alice, ela aparece e pergunta com a voz bem serena e calma:")
time.sleep(3)
print ('"o que você está fazendo?"')
time.sleep(3)
print ("você responde que estava colhendo informações.")
time.sleep(3)
print ("Alice vê o seu diário aberto e expulsa você da tenda vermelha de vergonha e raiva.")
time.sleep(3)
print ("Você vasculha a tenda do Lucas e não encontra nada de interessante.")
time.sleep(3)
print ("No dia seguinte, você procura em volta da tenda de cada um e na tenda de Alice havia um terreno mexido.")
time.sleep(3)
print ("Você esperou um momento em que Alice saísse dali e começou a cavar, encontrou as folhas que faltavam no diário da Alice que falavam detalhamente sobre os assassinatos.")
time.sleep(3)
print ("o que você não sabia era que Alice estava observando tudo.")
time.sleep(3)
pergunta7 = 1
while pergunta7 != 0:
    pergunta7=input("1 - Falar à Lucas e prender a Alice? 2 - Deixar para falar com o Lucas depois para não levantar suspeitas? 3 - Não falar nada? ")
    if pergunta7 == '1':
        print ("\nVocê chega até a localização do Lucas e mostra as provas para ele. Os dois prendem a Alice e esperam até o dia de ir embora para poder chamar a policia.\nFINAL BOM")
        quit()
    elif pergunta7 == '2':
        print ('\nSe passa uma noite e no dia seguinte você acorda com a Alice na porta da sua tenda toda ensanguentada com uma faca na mão')
        time.sleep(3)
        print('Ela lhe diz que apenas queria passar uma semana com você, e sabia que você gosta de brincar de investigação então fez aquilo para te deixar feliz.')
        time.sleep(3)
        print('Ela entra na tenda e mata o jogador.\nFINAL RUIM')
        quit()
    elif pergunta7 == '3':
        print('Você irá conversar com a Alice.')
        time.sleep(3)
        print('Ele a explica o porquê fez aquilo,')
        time.sleep(3)
        print('E então ela te da um beijo e os dois fogem de moto para bem longe daquele lugar.') 
        time.sleep(3)
        print('Lucas por ser o único encontrado no local é preso, e os dois são taxados de desaparecidos.\nFINAL CAÓTICO')
        quit()
    else:
        print('Resposta inválida')