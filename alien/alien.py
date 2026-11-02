import time

tempo_padrao = 0.07
visitou_curral = 0
tarefas = {
    "1": False,
    "2": False,
    "3": False,
    "4": False
}

def main():
    #O despertar
    escrever("É uma tarde comum em uma fazenda isolada no interior.", tempo_padrao)
    print("\n")
    escrever("Uma criança de 10 anos acorda dormindo na sala de sua casa. A televisão está ligada passando jornal, o horário dos desenhos já havia passado faz tempo. O apresentador parece estar estérico com alguma notícia alarmante, mas não é do seu interesse prestar atenção.", tempo_padrao)
    print("\n")
    escrever("Sua boca está seca, o controle está jogado no chão, mas ainda nauseado, começa a lembrar de alguma coisa que sua mãe havia pedido a ele", tempo_padrao)
    escrever("...", 2)
    escrever(" AH! É isso mesmo! Precisava fazer algumas tarefas de casa. Sua mãe precisou ir à cidade e deixou uma lista de afazeres para que ele terminasse antes de sua volta.", tempo_padrao)
    print("\n")
    escrever("A casa está silenciosa. Do lado de fora, é possível ouvir o vento passando pela plantação e alguns animais se movimentando ao longe.", tempo_padrao)
    lista_tarefas()

def lista_tarefas():
    global tarefas
    global visitou_curral
    print("\n\033[1mTarefas do dia:\033[0m")
    if not tarefas["1"]:
        print("1. Ir buscar leite das vacas.")
    if not tarefas["2"]:
        print("2. Colher o milho.")
    if not tarefas["3"]:
        print("3. Varrer a casa.")
    if not tarefas["4"]:
        print("4. Lavar a louça.")
    print("Ass.: mamãe\n")
    tarefa = input("“Por onde devo começar?...”(Digite o número da tarefa): ")

    if tarefa == "1" and not tarefas["1"]:
        tarefas["1"] = True
        print("\n")
        buscar_leite()
    elif tarefa == "2" and not tarefas["2"]:
        tarefas["2"] = True
        print("\n")
        colher_milho()
    elif tarefa == "3" and not tarefas["3"]:
        tarefas["3"] = True
        print("\n")
        varrer_casa()
    elif tarefa == "4" and not tarefas["4"]:
        tarefas["4"] = True
        print("\n")
        lavar_louca()
    else:
        escrever("Tarefa inválida. Por favor, escolha uma tarefa válida.", tempo_padrao)
        print("\n")
        lista_tarefas()
    

def voltando_para_casa():
    escrever("Ao se aproximar da entrada, tenta abrir a porta, mas a maçaneta não gira.", tempo_padrao)

def lavar_louca():
    #Se ele já passou no curral 2 vezes antes e ainda tem que lavar a louça significa que ele está do lado de fora
    global visitou_curral
    if visitou_curral==2:
        print("O menino retorna para casa")
        voltando_para_casa()
    else:
        escrever("A criança vai até a cozinha.", tempo_padrao)
        escrever("Na pia, encontra os pratos, copos e talheres que precisam ser lavados.", tempo_padrao)
        escrever("Ele abre a torneira e começa a limpar a louça.", tempo_padrao)
        escrever("Depois de terminar, guarda os utensílios e volta para consultar a lista.", tempo_padrao)
        print("\n")
        lista_tarefas()

def varrer_casa():
    #Se ele já passou no curral 2 vezes antes e ainda tem que varrer a casa significa que ele está do lado de fora
    global visitou_curral
    if visitou_curral==2:
        print("O menino retorna para casa")
        voltando_para_casa()
    else:
        escrever("A criança pega a vassoura, mas percebe que ela não está no lugar habitual.", tempo_padrao)
        print("\n")
        escrever("“Acho que deixei essa vassoura no curral, aquele lugar anda sempre sujo...”", tempo_padrao)
        print("\n")
        escrever("Sem outra alternativa, sai de casa e caminha até lá.", tempo_padrao)
        print("\n")
        escrever("Ao chegar ao curral, a criança observa as vacas.", tempo_padrao)
        
        if visitou_curral!=0:
            visitou_curral+=1
            print("\n")
            escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", tempo_padrao)
            print("\n") 
            escrever("Depois de pegar a vassoura, retorna para casa.", tempo_padrao)
            print("\n")
            voltando_para_casa()
            
        else:
            visitou_curral+=1
            print("\n")
            escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", tempo_padrao)
            print("\n") 
            escrever("Depois de pegar a vassoura, retorna para casa.", tempo_padrao)
            print("\n")
            escrever("Ele começa a varrer os cômodos, recolhendo a sujeira acumulada no chão. Enfim, tarefa concluída com sucesso!", tempo_padrao)
            print("\n")
            lista_tarefas()


def colher_milho():
    escrever("A criança vai até o milharal para recolher o milho.", tempo_padrao)
    print("\n")
    escrever("A plantação é extensa, e as folhas altas dificultam a visão do que está ao redor. O vento passa pelas fileiras de plantas, produzindo um ruído constante.", tempo_padrao)
    print("\n")
    escrever("Ao chegar: “Ó, acho que ainda não acordei completamente, o cesto para pegar as espigas está no curral.”", tempo_padrao)
    print("\n")
    escrever("A criança caminha até o curral.", tempo_padrao)
    escrever("Ao chegar, observa os animais.", tempo_padrao)

    global visitou_curral

    if visitou_curral!=0:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", tempo_padrao)
        print("\n") 
        escrever("Ele pega o cesto e retorna ao milharal.", tempo_padrao)
        print("\n")
        escrever("Com o cesto em mãos, começa a recolher as espigas, tarefa concluída com sucesso!", tempo_padrao)
    
    else:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", tempo_padrao)
        print("\n") 
        escrever("Tudo parece normal, embora uma delas esteja um pouco afastada das outras.", tempo_padrao)
        print("\n")
        escrever("Ele pega o cesto e retorna ao milharal.", tempo_padrao)
        print("\n")
        escrever("Com o cesto em mãos, começa a recolher as espigas, tarefa concluída com sucesso!", tempo_padrao)
    print("\n")
    lista_tarefas()

def buscar_leite():
    escrever("A criança caminha até o curral, onde as vacas costumam ficar durante a manhã.", tempo_padrao)
    print("\n")
    escrever("Ao chegar, percebe que os animais estão inquietos. Eles se movimentam de um lado para o outro, como se alguma coisa os estivesse incomodando.", tempo_padrao)
    print("\n")
    escrever("A criança se aproxima para contar os animais.", tempo_padrao)

    global visitou_curral

    if visitou_curral!=0:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", tempo_padrao)
        print("\n") 
        escrever("Ainda sim a criança começa a tirar o leite e voilà, tarefa concluída com sucesso!", tempo_padrao)

    else:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", tempo_padrao)
        print("\n") 
        escrever("Tudo parece normal, embora uma delas esteja um pouco afastada das outras.", tempo_padrao)
        print("\n")
        escrever("A criança começa a tirar o leite e voilà, tarefa concluída com sucesso!", tempo_padrao)
    print("\n")
    lista_tarefas()

#função para escrever o texto com efeito de digitação
def escrever(texto, tempo2):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(tempo2)

#função para exibir o menu da fazenda
def fazenda():
    texto = "A FAZENDA\n"
    #Mudar para um nome melhor quando for decidido
    jogar = "[(A) JOGAR]"
    sair = "[(S) SAIR ]"
    print(texto.center(50))
    print(jogar.center(50))
    print(sair.center(50))
    escolha = input("Escolha uma opção: ")

    if(escolha == "A" or escolha == "a"):
        escrever("Você escolheu jogar! Seja muito bem-vindo!", tempo_padrao)
        print("\n")
        main()
    elif(escolha == "S" or escolha == "s"):
        escrever("Você escolheu sair!", tempo_padrao)
        print("\n")
    else:
        escrever("Opção inválida!", tempo_padrao)
        print("\n")
        fazenda()

fazenda()