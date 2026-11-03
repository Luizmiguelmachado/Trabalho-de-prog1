import time

# Constantes e variáveis de estado global
TEMPO_PADRAO = 0.07
visitou_curral = 0

tarefas = {
    "1": False,
    "2": False,
    "3": False,
    "4": False
}

# --- FUNÇÕES UTILITÁRIAS ---

def escrever(texto, tempo=TEMPO_PADRAO):
    """Escreve o texto com efeito de digitação suave no terminal."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(tempo)

# --- CENÁRIOS E AÇÕES DA HISTÓRIA ---

def segundo_andar():
    print("\n")
    escrever("A criança se aproxima do cano que passa pela parede da casa.", TEMPO_PADRAO)
    print("\n")
    escrever("Ele olha para cima e percebe que o cano chega perto da janela aberta do segundo andar.", TEMPO_PADRAO)
    print("")
    escrever("Não parece uma tarefa fácil, mas talvez seja a única maneira de entrar sem precisar quebrar nada.", TEMPO_PADRAO)
    print("\n")
    escrever("Bom, será que eu devo...", TEMPO_PADRAO)
    print("")
    print("1. Subir rapidamente.\n2. Subir devagar")
    escolha = ""
    while True:
        escolha = input("Escolha uma opção: ")
        print("\n")
        
        if escolha == "1":
            escrever("A criança começa a escalar o cano.", TEMPO_PADRAO)
            print("\n")
            escrever("No início, consegue subir alguns metros, mas logo percebe que está se esforçando demais.", TEMPO_PADRAO)
            print("\n")
            escrever("Seu pé escorrega. Ele tenta se segurar, mas perde o equilíbrio e cai.", TEMPO_PADRAO)
            print("\n")
            escrever("A queda provoca fortes dores, e ele permanece alguns instantes no chão, tentando recuperar o fôlego.", TEMPO_PADRAO)
            print("\n")
            escrever("Agora, está com medo de tentar novamente...", TEMPO_PADRAO)
            print("\n")
            machucado = ""
            while True:
                machucado = input("1. Desistir e tentar entrar pelo porão.\n2. Tentar subir novamente, desta vez devagar")
                
                if machucado == "1":
                    porao()
                    break
                elif machucado == "2":
                    escolha = "2"
                    break
                else:
                    escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
                    print("\n\n")
            if machucado == "1":
                break
            
        if escolha == "2":
            escrever("A criança segura o cano com firmeza e começa a subir cuidadosamente.", TEMPO_PADRAO)
            print("\n")
            escrever("Ele procura apoiar os pés nos pontos em que consegue encontrar mais estabilidade.", TEMPO_PADRAO)
            print("\n")
            escrever("A subida é demorada, mas, depois de algum esforço, consegue alcançar o telhado.", TEMPO_PADRAO)
            print("")
            escrever("Ele se senta por alguns instantes para recuperar o fôlego. Enfim, com um ultimo suspiro de força, ele chega até a janela aberta do segundo andar.", TEMPO_PADRAO)
            break
    
        if escolha not in ["1", "2"]:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")
    if escolha == "2":
        print("\n")
        escrever("Do telhado, a criança consegue observar parte da propriedade.", TEMPO_PADRAO)
        print("")
        escrever("O milharal se estende até onde sua visão alcança.", TEMPO_PADRAO)
        print("\n")
        escrever("Por alguns instantes, tudo parece normal.", TEMPO_PADRAO)
        print("\n")
        escrever("Então, ele percebe algo estranho na plantação...", TEMPO_PADRAO)
        print("")
        escrever("As plantas estão organizadas de uma maneira diferente em determinada área, formando um desenho que não parece ter sido feito naturalmente.", TEMPO_PADRAO)
        print("\n")
        escrever("Ele tenta entender o que está vendo, mas a distância dificulta a identificação.", TEMPO_PADRAO)
        print("\n")

        #Continuar daquiii: Entrar imediatamente pela janela. Observar melhor a plantação. Tentar subir ainda mais para enxergar melhor.


#tem que terminar essa parte
def porao():
    print("\n")
    escrever("Você se aproxima da porta do porão e segura a maçaneta gelada de metal...", TEMPO_PADRAO)
    print("\n")
    escrever("[Conteúdo do porão em desenvolvimento...]", TEMPO_PADRAO)
    print("\n")

def voltando_para_casa_opcoes():
    escrever("“Será que devo...“\n", TEMPO_PADRAO)
    
    while True:
        print("1. “Tentar arrombar a porta.“\n2. “Olhar ao redor em busca de outra entrada.“\n")
        opcao = input("Escolha uma opção: ").strip()
        print("\n")
        
        if opcao == "1":
            escrever("A criança empurra a porta com força.", TEMPO_PADRAO)
            print("")
            escrever("Ela não se move.", TEMPO_PADRAO)
            print("")
            escrever("Ele tenta novamente, usando o ombro, mas acaba sentindo dor.", TEMPO_PADRAO)
            print("\n")
            escrever("A porta é resistente demais para que uma criança de 10 anos consiga arrombá-la.", TEMPO_PADRAO)
            print("")
            escrever("Frustrado, ele desiste.", TEMPO_PADRAO)
            print("")
            escrever("“Acho que o que me resta é procurar uma entrada ao redor...“", TEMPO_PADRAO)
            print("\n")
            break
        elif opcao == "2":
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

    # Sequência após descurbrir que precisa procurar outra entrada
    escrever("A criança se afasta alguns passos para observar a casa.", TEMPO_PADRAO)
    print("\n")
    escrever("Ao olhar para cima, percebe que uma janela do segundo andar está aberta.", TEMPO_PADRAO)
    print("")
    escrever("Ele também nota o cano de escoamento que passa pela parede, próximo à janela.", TEMPO_PADRAO)
    print("")
    escrever("Talvez consiga subir por ele...", TEMPO_PADRAO)
    print("\n")
    escrever("Ao olhar para o outro lado da casa, percebe a porta do porão.", TEMPO_PADRAO)
    print("\n")

    while True:
        caminhos = input("1. “Acho que devo tentar entrar pelo segundo andar.“\n2. “Devo tentar abrir a porta do porão.“\nEscolha: ").strip()
        if caminhos == "1":
            segundo_andar()
            break
        elif caminhos == "2":
            porao()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def voltando_para_casa():
    escrever("Ao se aproximar da entrada, tenta abrir a porta, mas a maçaneta não gira.", TEMPO_PADRAO)
    print("\n")
    escrever("Ele tenta novamente.", TEMPO_PADRAO)
    print("\n")
    escrever("A porta está trancada.", TEMPO_PADRAO)
    print("\n")
    escrever("A criança estranha a situação. Sua mãe levou a chave consigo, mas deveria voltar apenas mais tarde.", TEMPO_PADRAO)
    print("\n")
    escrever("Ele se vê em uma posição difícil e pensa: ", TEMPO_PADRAO)
    print("\n")
    voltando_para_casa_opcoes()

def lavar_louca():
    global visitou_curral
    if visitou_curral >= 2:
        print("O menino retorna para casa.")
        voltando_para_casa()
    else:
        escrever("A criança vai até a cozinha.", TEMPO_PADRAO)
        print("")
        escrever("Na pia, encontra os pratos, copos e talheres que precisam ser lavados.", TEMPO_PADRAO)
        print("")
        escrever("Ele abre a torneira e começa a limpar a louça.", TEMPO_PADRAO)
        print("")
        escrever("Depois de terminar, guarda os utensílios e volta para consultar a lista.", TEMPO_PADRAO)
        print("\n")
        lista_tarefas()

def varrer_casa():
    global visitou_curral
    if visitou_curral >= 2:
        print("O menino retorna para casa.")
        voltando_para_casa()
    else:
        escrever("A criança pega a vassoura, mas percebe que ela não está no lugar habitual.", TEMPO_PADRAO)
        print("\n")
        escrever("“Acho que deixei essa vassoura no curral, aquele lugar anda sempre sujo...”", TEMPO_PADRAO)
        print("\n")
        escrever("Sem outra alternativa, sai de casa e caminha até lá.", TEMPO_PADRAO)
        print("\n")
        escrever("Ao chegar ao curral, a criança observa as vacas.", TEMPO_PADRAO)
        
        if visitou_curral != 0:
            visitou_curral += 1
            print("\n")
            escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", TEMPO_PADRAO)
            print("\n") 
            escrever("Depois de pegar a vassoura, retorna para casa.", TEMPO_PADRAO)
            print("\n")
            voltando_para_casa()  
        else:
            visitou_curral += 1
            print("\n")
            escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", TEMPO_PADRAO)
            print("\n") 
            escrever("Depois de pegar a vassoura, retorna para casa.", TEMPO_PADRAO)
            print("\n")
            escrever("Ele começa a varrer os cômodos, recolhendo a sujeira acumulada no chão. Enfim, tarefa concluída com sucesso!", TEMPO_PADRAO)
            print("\n")
            lista_tarefas()

def colher_milho():
    global visitou_curral
    escrever("A criança vai até o milharal para recolher o milho.", TEMPO_PADRAO)
    print("\n")
    escrever("A plantação é extensa, e as folhas altas dificultam a visão do que está ao redor. O vento passa pelas fileiras de plantas, produzindo um ruído constante.", TEMPO_PADRAO)
    print("\n")
    escrever("Ao chegar: “Ó, acho que ainda não acordei completamente, o cesto para pegar as espigas está no curral.”", TEMPO_PADRAO)
    print("\n")
    escrever("A criança caminha até o curral.", TEMPO_PADRAO)
    print("")
    escrever("Ao chegar, observa os animais.", TEMPO_PADRAO)

    if visitou_curral != 0:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", TEMPO_PADRAO)
        print("\n") 
        escrever("Ele pega o cesto e retorna ao milharal.", TEMPO_PADRAO)
        print("\n")
        escrever("Com o cesto em mãos, começa a recolher as espigas, tarefa concluída com sucesso!", TEMPO_PADRAO)
    else:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", TEMPO_PADRAO)
        print("\n") 
        escrever("Tudo parece normal, embora uma delas esteja um pouco afastada das outras.", TEMPO_PADRAO)
        print("\n")
        escrever("Ele pega o cesto e retorna ao milharal.", TEMPO_PADRAO)
        print("\n")
        escrever("Com o cesto em mãos, começa a recolher as espigas, tarefa concluída com sucesso!", TEMPO_PADRAO)
        
    print("\n")
    lista_tarefas()

def buscar_leite():
    global visitou_curral
    escrever("A criança caminha até o curral, onde as vacas costumam ficar durante a manhã.", TEMPO_PADRAO)
    print("\n")
    escrever("Ao chegar, percebe que os animais estão inquietos. Eles se movimentam de um lado para o outro, como se alguma coisa os estivesse incomodando.", TEMPO_PADRAO)
    print("\n")
    escrever("A criança se aproxima para contar os animais.", TEMPO_PADRAO)

    if visitou_curral != 0:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cin... Uai, estranho... Pensei ter contado cinco vacas na última vez. Bom, devo ter me confundido, minhas notas em matemática não andam muito boas...”", TEMPO_PADRAO)
        print("\n") 
        escrever("Ainda assim a criança começa a tirar o leite e voilà, tarefa concluída com sucesso!", TEMPO_PADRAO)
    else:
        visitou_curral += 1
        print("\n")
        escrever("“Um, dois, três, quatro, cinco... Isso aí, são cinco vacas!”", TEMPO_PADRAO)
        print("\n") 
        escrever("Tudo parece normal, embora uma delas esteja um pouco afastada das outras.", TEMPO_PADRAO)
        print("\n")
        escrever("A criança começa a tirar o leite e voilà, tarefa concluída com sucesso!", TEMPO_PADRAO)
        
    print("\n")
    lista_tarefas()

def lista_tarefas():
    global tarefas

    if all(tarefas.values()):
        escrever("Parabéns! Você concluiu todas as tarefas do dia!", TEMPO_PADRAO)
        print("\n")
        escrever("Agora você pode relaxar e aproveitar o resto do dia na fazenda.", TEMPO_PADRAO)
        print("")
        escrever("Mas espera aí", TEMPO_PADRAO)
        escrever("... ", 2)
        print("")
        escrever("Ele caminha até a sua casa. ")
        voltando_para_casa()
    else:
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
        
        while True:
            tarefa = input("“Por onde devo começar?...”(Digite o número da tarefa): ").strip()

            if tarefa == "1" and not tarefas["1"]:
                tarefas["1"] = True
                print("\n")
                buscar_leite()
                break
            elif tarefa == "2" and not tarefas["2"]:
                tarefas["2"] = True
                print("\n")
                colher_milho()
                break
            elif tarefa == "3" and not tarefas["3"]:
                tarefas["3"] = True
                print("\n")
                varrer_casa()
                break
            elif tarefa == "4" and not tarefas["4"]:
                tarefas["4"] = True
                print("\n")
                lavar_louca()
                break
            else:
                escrever("Tarefa inválida ou já concluída. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
                print("\n\n")

# --- FLUXO PRINCIPAL DO JOGO ---

def main():
    # O despertar
    escrever("É uma tarde comum em uma fazenda isolada no interior.", TEMPO_PADRAO)
    print("\n")
    escrever("Uma criança de 10 anos acorda dormindo na sala de sua casa. A televisão está ligada passando jornal, o horário dos desenhos já havia passado faz tempo. O apresentador parece estar histérico com alguma notícia alarmante, mas não é do seu interesse prestar atenção.", TEMPO_PADRAO)
    print("\n")
    escrever("Sua boca está seca, o controle está jogado no chão, mas ainda nauseado, começa a lembrar de alguma coisa que sua mãe havia pedido a ele", TEMPO_PADRAO)
    escrever("...", 2)
    escrever(" AH! É isso mesmo! Precisava fazer algumas tarefas de casa. Sua mãe precisou ir à cidade e deixou uma lista de afazeres para que ele terminasse antes de sua volta.", TEMPO_PADRAO)
    print("\n")
    escrever("A casa está silenciosa. Do lado de fora, é possível ouvir o vento passando pela plantação e alguns animais se movimentando ao longe.", TEMPO_PADRAO)
    lista_tarefas()

def fazenda():
    while True:
        texto = "A FAZENDA\n"
        jogar = "[(A) JOGAR]"
        sair = "[(S) SAIR ]"
        print(texto.center(50))
        print(jogar.center(50))
        print(sair.center(50))
        escolha = input("Escolha uma opção: ").strip().upper()

        if escolha == "A":
            escrever("Você escolheu jogar! Seja muito bem-vindo!", TEMPO_PADRAO)
            print("\n\n")
            main()
            break
        elif escolha == "S":
            escrever("Você escolheu sair!", TEMPO_PADRAO)
            print("\n")
            break
        else:
            escrever("Opção inválida!", TEMPO_PADRAO)
            print("\n\n")


fazenda()
