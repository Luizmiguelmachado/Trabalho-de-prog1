import time

# Constantes e variáveis de estado global
TEMPO_PADRAO = 0.01
visitou_curral = 0
arma = ""

tarefas = {
    "1": False,
    "2": False,
    "3": False,
    "4": False
}

def escrever(texto, tempo=TEMPO_PADRAO):
    """Escreve o texto com efeito de digitação suave no terminal."""
    newtexto = ""
    cont = 0
    palavra = ""
    for i in range(len(texto)):
        cont += 1
        palavra += texto[i]
        if cont != 100 and (texto[i] == " " or i == len(texto) - 1):
            newtexto += palavra
            palavra = ""
        if cont == 100:
            newtexto += "\n" + palavra
            palavra = ""
            cont = 0

    for i in range(len(newtexto)):
        print(newtexto[i], end="", flush=True)
        time.sleep(tempo)

# --- CENÁRIOS E AÇÕES DA HISTÓRIA ---

def janela():
    global arma

    escrever("A criança abre a janela e entra no segundo andar.", TEMPO_PADRAO)
    print("")
    escrever("O quarto está silencioso.", TEMPO_PADRAO)
    print("")
    escrever("Ele se levanta e começa a caminhar pelo corredor, mas logo escuta um barulho vindo de outro cômodo", TEMPO_PADRAO)
    escrever("...", 2)
    print("\n")
    escrever("Parece que alguma coisa acabou de cair no chão.", TEMPO_PADRAO)
    escrever("...", 2)
    print("\n")
    escrever("Em seguida, ouve passos.", TEMPO_PADRAO)
    print("")
    escrever("Alguém está dentro da casa.", TEMPO_PADRAO)
    print("\n")
    print("Merda! Que #@$#@ é essa? O que eu faço?")
    print("")
    while True:
        print("1. Ir rapidamente investigar.\n2. Caminhar devagar para não fazer barulho.\n3.Procurar alguma coisa para se defender.")
        opcoes = input("Escolha uma opção: ")
        if opcoes == "1":
            escrever("A criança corre pelo corredor em direção ao barulho.", TEMPO_PADRAO)
            print("")
            escrever("Ao chegar perto de um dos quartos, vê uma figura usando o vestido da mãe.", TEMPO_PADRAO)
            print("")
            escrever("Ela está de costas.", TEMPO_PADRAO)
            print("")
            escrever("O cabelo loiro cobre seu rosto, e a figura parece estar procurando alguma coisa dentro de um armário.", TEMPO_PADRAO)
            print("\n")
            escrever("Antes que a criança consiga enxergar melhor, a figura se vira parcialmente.", TEMPO_PADRAO)
            print("")
            escrever("Ele não consegue distinguir seu rosto.", TEMPO_PADRAO)
            escrever("...", 2)
            print("\n")
            escrever("A figura começa a andar pelo corredor.", TEMPO_PADRAO)
            print("")
            escrever("O som de seus sapatos de salto ecoa pela casa.", TEMPO_PADRAO)
            print("\n")
            break

        elif opcoes == "2":
            escrever("A criança avança pelo corredor, tentando não fazer barulho.", TEMPO_PADRAO)
            print("")
            escrever("Ele observa as portas dos quartos e tenta localizar a origem dos ruídos.", TEMPO_PADRAO)
            print("")
            escrever("Entretanto, pisa em uma madeira solta do assoalho.", TEMPO_PADRAO)
            escrever("CRÉÉÉÉC...", 2)
            print("\n")
            escrever("A madeira range alto.", TEMPO_PADRAO)
            print("")
            escrever("Os passos param imediatamente.", TEMPO_PADRAO)
            print("")
            escrever("A criança fica imóvel.", TEMPO_PADRAO)
            escrever("...", 3)
            print("\n")
            escrever("Depois de alguns segundos, ouve os passos se afastando.", TEMPO_PADRAO)
            print("")
            escrever("A figura parece ter percebido alguma coisa e decidiu mudar de lugar.", TEMPO_PADRAO)
            print("\n")
            break

        elif opcoes == "3":
            escrever("A criança pensa que talvez seja melhor encontrar alguma coisa para se defender antes que algo de ruim pudesse acontecer", TEMPO_PADRAO)
            print("")
            escrever("Ele conhece bem os quartos da casa e sabe onde procurar.", TEMPO_PADRAO)
            print("\n")

            print("“Mas aonde eu devo procurar?“")
            print("")
            print("1 - Entrar no quarto da mãe.")
            print("2 - Entrar no próprio quarto.")
            print("3 - Descer sem pegar nada.")
            print("")

            while True:
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print("")
                    escrever("A criança entra cuidadosamente no quarto da mãe.", TEMPO_PADRAO)
                    print("")
                    escrever("O ambiente parece normal, mas algumas gavetas estão abertas.", TEMPO_PADRAO)
                    print("")
                    escrever("Ele procura alguma coisa que possa usar para se defender...", TEMPO_PADRAO)
                    print("\n")
                    escrever("Depois de olhar ao redor, encontra um chinelo da mãe.", TEMPO_PADRAO)
                    print("")
                    escrever("Ele o segura, sem ter certeza de como aquilo poderia ajudá-lo.", TEMPO_PADRAO)
                    print("")
                    escrever("Apesar disso, sente-se um pouco mais preparado para continuar.", TEMPO_PADRAO)
                    print("")

                    arma = "chinela"
                    break

                elif escolha == "2":
                    print("")
                    escrever("A criança entra no próprio quarto e procura alguma coisa para se defender.", TEMPO_PADRAO)
                    print("")
                    escrever("Perto de um canto, encontra um bastão de beisebol.", TEMPO_PADRAO)
                    print("")
                    escrever("Ele o segura com as duas mãos.", TEMPO_PADRAO)
                    print("")
                    escrever("O objeto parece resistente, e a criança se sente mais confiante.", TEMPO_PADRAO)
                    print("")
                    
                    arma = "taco"
                    break

                elif escolha == "3":
                    print("")
                    break

                else:
                    print("")
                    print("Essa não é uma opção válida. Escolha 1, 2 ou 3.")
                    print("")
        else:
            print("Digite uma opção válida.")

    escrever("A criança decide que é melhor não perder tempo.", TEMPO_PADRAO)
    print("")
    escrever("Ele sai do corredor e começa a descer as escadas.", TEMPO_PADRAO)
    print("")
    escrever("Enquanto caminha, tenta imaginar onde a figura pode estar.", TEMPO_PADRAO)
    escrever("...", 1)
    print("\n")
    escrever("Talvez esteja na cozinha.", TEMPO_PADRAO)
    print("")
    escrever("Talvez esteja na sala.", TEMPO_PADRAO)
    print("")
    escrever("Ou talvez tenha descido para o porão.", TEMPO_PADRAO)
    print("")

    while True:
        print("O que a criança deve fazer?")
        print("")
        print("1 - Procurar na cozinha.")
        print("2 - Procurar na sala.")
        print("3 - Verificar a porta do porão.")
        print("")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cozinha()
            break

        elif escolha == "2":
            quartos()
            break

        elif escolha == "3":
            print("")
            escrever("A criança se aproxima da porta do porão.", TEMPO_PADRAO)
            print("")
            escrever("Ela está fechada.", TEMPO_PADRAO)
            print("")
            escrever("Ele tenta se lembrar de ter ouvido algum barulho de porta abrindo ou fechando, mas não consegue se recordar de nada.", TEMPO_PADRAO)
            print("")
            escrever("Se a criatura tivesse descido, provavelmente teria feito algum barulho.", TEMPO_PADRAO)
            print("")
            escrever("A criança conclui que talvez ela ainda esteja em outro cômodo.", TEMPO_PADRAO)
            print("")
            escrever("Ele retorna à sala e encontra a figura na poltrona.", TEMPO_PADRAO)
            print("")
            convergencia_criatura()
            break

        else:
            print("")
            print("Essa não é uma opção válida. Escolha 1, 2 ou 3.")
            print("\n")
    

def segundo_andar():
    print("\n")
    escrever("A criança se aproxima do cano que passa pela parede da casa.", TEMPO_PADRAO)
    print("")
    escrever("Ele olha para cima e percebe que o cano chega perto da janela aberta do segundo andar.", TEMPO_PADRAO)
    print("")
    escrever("Não parece uma tarefa fácil, mas talvez seja a única maneira de entrar sem precisar quebrar nada.", TEMPO_PADRAO)
    print("")
    escrever("Bom, será que eu devo...", TEMPO_PADRAO)
    print("\n")
    print("1. Subir rapidamente.\n2. Subir devagar")
    escolha = ""
    while True:
        escolha = input("Escolha uma opção: ")
        print("\n")
        
        if escolha == "1":
            escrever("A criança começa a escalar o cano.", TEMPO_PADRAO)
            print("")
            escrever("No início, consegue subir alguns metros, mas logo percebe que está se esforçando demais.", TEMPO_PADRAO)
            print("\n")
            escrever("Seu pé escorrega. Ele tenta se segurar, mas perde o equilíbrio e cai.", TEMPO_PADRAO)
            print("")
            escrever("A queda provoca fortes dores, e ele permanece alguns instantes no chão, tentando recuperar o fôlego.", TEMPO_PADRAO)
            print("")
            escrever("Agora, está com medo de tentar novamente...", TEMPO_PADRAO)
            print("\n")
            machucado = ""
            while True:
                print("1. Desistir e tentar entrar pelo porão.\n2. Tentar subir novamente, desta vez devagar")
                machucado = input("Escolha uma opção: ")
                print("\n")
                
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
            print("")
            escrever("Ele procura apoiar os pés nos pontos em que consegue encontrar mais estabilidade.", TEMPO_PADRAO)
            print("")
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
        print("Será que devo... ")
        print("")
        while True:
            print("1. Entrar imediatamente pela janela.\n2. Observar melhor a plantação.", TEMPO_PADRAO)
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                janela()
                break
            elif escolha == "2":
                escrever("A criança se aproxima da borda do telhado e tenta enxergar o desenho com mais clareza.", TEMPO_PADRAO)
                print("")
                escrever("As plantas parecem formar um círculo irregular, com linhas que se estendem para diferentes direções.", TEMPO_PADRAO)
                print("\n")
                escrever("Ele se lembra de histórias sobre desenhos misteriosos encontrados em plantações, mas nunca imaginou encontrar algo parecido fora da ficção!", TEMPO_PADRAO)
                print("")
                
            else:
                escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
                print("\n\n")


def observando_arredores():
    """Seção 7 - Opção de voltar a observar os arredores da casa."""
    escrever("A criança se afasta da porta e volta a olhar para os lados da casa.", TEMPO_PADRAO)
    print("\n")
    escrever("Ela percebe novamente as duas possibilidades de entrada.", TEMPO_PADRAO)
    print("")
    escrever("Ao olhar para cima, vê o cano de escoamento próximo à janela do segundo andar.", TEMPO_PADRAO)
    print("")
    escrever("Ao olhar para o outro lado, percebe novamente a porta do porão.", TEMPO_PADRAO)
    print("\n")
    
    while True:
        print("1. Tentar subir pela calha.\n2. Tentar entrar pelo porão.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")
        if escolha == "1":
            segundo_andar()
            break
        elif escolha == "2":
            porao()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def janela_porao():

    escrever("A criança aproxima o rosto do vidro.", TEMPO_PADRAO)
    print("")
    escrever("O vidro está extremamente sujo e fosco.", TEMPO_PADRAO)
    print("")
    escrever("Ela tenta limpar uma pequena parte com a mão, mas ainda não consegue enxergar através dele.", TEMPO_PADRAO)
    print("\n")
    escrever("Por alguns instantes, tudo o que consegue ver é uma imagem distorcida do interior.", TEMPO_PADRAO)
    print("")
    escrever("Então, percebe algo.", TEMPO_PADRAO)
    print("")
    escrever("Uma pequena luz verde aparece no fundo do porão.", TEMPO_PADRAO)
    print("")
    escrever("A criança se aproxima ainda mais.", TEMPO_PADRAO)
    print("\n")
    escrever("“Hm... O que é aquilo?”", TEMPO_PADRAO)
    print("")
    escrever("A luz parece estar vindo de algum objeto escondido no interior.", TEMPO_PADRAO)
    print("")
    escrever("Entretanto, a sujeira do vidro impede que ela veja o que realmente está acontecendo.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Tentar abrir a porta do porão.\n2. Voltar a observar os arredores da casa.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")
        if escolha == "1":
            entrando_no_porao()
            break
        elif escolha == "2":
            observando_arredores()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def porao():
    """Seção 7 - A porta do porão."""
    escrever("Depois de observar os arredores da casa, a criança percebe a porta do porão.", TEMPO_PADRAO)
    print("")
    escrever("Ela se aproxima e observa o local.", TEMPO_PADRAO)
    print("")
    escrever("A porta parece antiga, mas não apresenta nenhum sinal de estar trancada.", TEMPO_PADRAO)
    print("")
    escrever("Ao lado dela, há uma pequena janela.", TEMPO_PADRAO)
    print("")
    escrever("O vidro está sujo e fosco, dificultando a visão do interior.", TEMPO_PADRAO)
    print("")
    escrever("A criança tenta descobrir o que existe lá dentro.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Tentar abrir a porta do porão.\n2. Olhar pela janela.\n3. Voltar a observar os arredores da casa.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")
        if escolha == "1":
            entrando_no_porao()
            break
        elif escolha == "2":
            janela_porao()
            break
        elif escolha == "3":
            observando_arredores()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def entrando_no_porao():
    escrever("Ela coloca a mão na maçaneta e gira.", TEMPO_PADRAO)
    print("")
    escrever("A porta se abre. O interior do porão está escuro e bagunçado.", TEMPO_PADRAO)
    print("")
    escrever("Há caixas espalhadas pelo chão, objetos antigos e algumas estantes encostadas nas paredes.", TEMPO_PADRAO)
    print("\n")
    escrever("A criança olha para dentro.", TEMPO_PADRAO)
    print("")
    escrever("“Eu nunca tinha entrado aqui sozinho...”", TEMPO_PADRAO)
    print("")
    escrever("Apesar da bagunça, as escadas que levam para dentro da casa podem ser vistas ao fundo.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Ignorar a bagunça e subir as escadas.\n2. Vasculhar as coisas do porão.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")
        if escolha == "1":
            porta_para_dentro()
            break
        elif escolha == "2":
            vasculhando_porao()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def porta_para_dentro():
    escrever("Ela atravessa o porão e chega até as escadas.", TEMPO_PADRAO)
    print("")
    escrever("No final delas existe uma porta que leva para dentro da casa.", TEMPO_PADRAO)
    print("")
    escrever("A criança segura a maçaneta e tenta abrir.", TEMPO_PADRAO)
    print("")
    escrever("A maçaneta não gira.", TEMPO_PADRAO)
    print("")
    escrever("Ele tenta novamente.", TEMPO_PADRAO)
    print("")
    escrever("Nada.", TEMPO_PADRAO)
    print("")
    escrever("A porta está trancada.", TEMPO_PADRAO)
    print("")
    escrever("“Droga...”", TEMPO_PADRAO)
    print("")
    escrever("A criança lembra que sua mãe costuma deixar uma chave no porão. Talvez ela esteja escondida em algum lugar entre aquelas coisas.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Vasculhar as estantes.\n2. Voltar a procurar entre as coisas do porão.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")
        if escolha == "1" or escolha == "2":
            vasculhando_porao()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def vasculhando_porao():
    escrever("A criança decide procurar pela chave.", TEMPO_PADRAO)
    print("\n")
    escrever("O porão está cheio de objetos antigos e caixas espalhadas.", TEMPO_PADRAO)
    print("\n")
    escrever("Ela olha ao redor e percebe três estantes que podem esconder alguma coisa.", TEMPO_PADRAO)
    print("\n")

    estantes_visitadas = {"1": False, "2": False, "3": False}

    while True:
        print("Qual estante você deseja vasculhar?")
        if not estantes_visitadas["1"]:
            print("1. Estante 1")
        if not estantes_visitadas["2"]:
            print("2. Estante 2")
        if not estantes_visitadas["3"]:
            print("3. Estante 3")
        
        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1" and not estantes_visitadas["1"]:
            estantes_visitadas["1"] = True
            escrever("A criança se aproxima da primeira estante. Há vários objetos antigos e caixas empilhadas.", TEMPO_PADRAO)
            print("")
            escrever("Ela começa a procurar entre as coisas.", TEMPO_PADRAO)
            print("")
            escrever("Depois de algum tempo, percebe que não há nenhuma chave ali.", TEMPO_PADRAO)
            print("\n")
            escrever("“Não está aqui...”", TEMPO_PADRAO)
            print("\n")

        elif escolha == "2" and not estantes_visitadas["2"]:
            estantes_visitadas["2"] = True
            escrever("A criança se aproxima da segunda estante. Ela começa a retirar algumas coisas do caminho e procura cuidadosamente.", TEMPO_PADRAO)
            print("")
            escrever("Depois de alguns segundos, percebe que também não encontrou a chave.", TEMPO_PADRAO)
            print("")
            escrever("“Também não está aqui...”", TEMPO_PADRAO)
            print("")
            escrever("De repente...", TEMPO_PADRAO)
            print("\n")
            escrever("Troc... Troc...", TEMPO_PADRAO)
            print("\n")
            escrever("A criança para.", TEMPO_PADRAO)
            print("")
            escrever("Ela olha para cima. O som parece ter vindo do andar de cima. Por alguns segundos, tudo fica em silêncio.", TEMPO_PADRAO)
            print("\n")
            escrever("Então...", TEMPO_PADRAO)
            print("\n")
            escrever("Troc... Troc...", TEMPO_PADRAO)
            print("\n")
            escrever("Dessa vez, o som parece ainda mais claro. São passos...", TEMPO_PADRAO)
            print("")
            escrever("Mas não são passos comuns.", TEMPO_PADRAO)
            print("")
            escrever("O som lembra o de um salto batendo contra o chão.", TEMPO_PADRAO)
            print("")
            escrever("A criança fica imóvel.", TEMPO_PADRAO)
            print("")
            escrever("“Ué...”", TEMPO_PADRAO)
            print("")
            escrever("Ela olha para a porta que leva para dentro da casa.", TEMPO_PADRAO)
            print("")
            escrever("“Eu deveria estar sozinho...”", TEMPO_PADRAO)
            print("")

        elif escolha == "3" and not estantes_visitadas["3"]:
            estantes_visitadas["3"] = True
            escrever("A criança decide continuar procurando. Ela se aproxima da terceira estante.", TEMPO_PADRAO)
            print("")
            escrever("Entre algumas caixas e objetos antigos, encontra algo metálico.", TEMPO_PADRAO)
            print("")
            escrever("Ele puxa o objeto para fora.", TEMPO_PADRAO)
            print("")
            escrever("É uma chave.", TEMPO_PADRAO)
            print("")
            escrever("“Achei!”", TEMPO_PADRAO)
            print("")
            escrever("A criança segura a chave e olha novamente para a porta.", TEMPO_PADRAO)
            print("\n")
            entrar_novamente_na_casa()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def entrar_novamente_na_casa():
    escrever("A criança coloca a chave na fechadura.", TEMPO_PADRAO)
    print("\n")
    escrever("Clac.", TEMPO_PADRAO)
    print("\n")
    escrever("A porta destranca.", TEMPO_PADRAO)
    print("")
    escrever("Ele gira a maçaneta lentamente.", TEMPO_PADRAO)
    print("")
    escrever("A porta se abre e a criança entra na casa.", TEMPO_PADRAO)
    print("")
    escrever("O ambiente parece silencioso, por alguns segundos, tudo parece normal.", TEMPO_PADRAO)
    print("")
    escrever("Mas ele ainda se lembra dos passos que ouviu no andar de cima.", TEMPO_PADRAO)
    print("")
    escrever("Talvez tivesse sido apenas alguma coisa caindo.", TEMPO_PADRAO)
    print("")
    escrever("Ou talvez não...", TEMPO_PADRAO)
    print("")
    escrever("A criança olha ao redor.", TEMPO_PADRAO)
    print("\n")
    investigando_a_casa()

def investigando_a_casa():
    while True:
        print("1. Procurar na cozinha.\n2. Procurar na sala.\n3. Procurar nos quartos.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1":
            cozinha()
            break
        elif escolha == "2":
            sala()
            break
        elif escolha == "3":
            quartos()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def cozinha():
    escrever("A criança entra cuidadosamente.", TEMPO_PADRAO)
    print("")
    escrever("A pia está limpa, mas alguns objetos estão organizados de maneira estranha.", TEMPO_PADRAO)
    print("")
    escrever("Os talheres estão empilhados sobre a mesa em fileiras muito precisas.", TEMPO_PADRAO)
    print("")
    escrever("A criança observa por alguns segundos.", TEMPO_PADRAO)
    print("")
    escrever("“Minha mãe não deixa as coisas assim...”", TEMPO_PADRAO)
    print("")
    escrever("Antes que consiga investigar melhor, ouve um ruído vindo da sala.", TEMPO_PADRAO)
    print("")
    escrever("A criança olha em direção à porta.", TEMPO_PADRAO)
    print("")
    escrever("Troc... Troc...", TEMPO_PADRAO)
    print("")
    escrever("O som de passos de salto ecoa novamente pela casa.", TEMPO_PADRAO)
    print("")
    escrever("A criança percebe que o som que ouviu no porão realmente vinha de alguém se movimentando pela casa.", TEMPO_PADRAO)
    print("")
    escrever("Ela decide investigar a sala...", TEMPO_PADRAO)
    print("\n")
    convergencia_criatura()

def sala():
    escrever("A criança entra lentamente.", TEMPO_PADRAO)
    print("")
    escrever("A televisão está ligada.", TEMPO_PADRAO)
    print("")
    escrever("A sala parece estar vazia. Por alguns segundos, ele pensa que talvez não exista ninguém ali até que percebe algo.", TEMPO_PADRAO)
    print("")
    escrever("A poltrona da mãe está ocupada.", TEMPO_PADRAO)
    print("")
    escrever("Há uma figura sentada nela.", TEMPO_PADRAO)
    print("")
    escrever("Ela está usando um vestido e uma peruca loira.", TEMPO_PADRAO)
    print("")
    escrever("A criança permanece parada.", TEMPO_PADRAO)
    print("")
    escrever("Ela não consegue enxergar o rosto da figura.", TEMPO_PADRAO)
    print("\n")
    convergencia_criatura()

def quartos():
    escrever("A criança entra no corredor.", TEMPO_PADRAO)
    print("")
    escrever("As portas dos quartos estão fechadas.", TEMPO_PADRAO)
    print("")
    escrever("Ele começa a observar cada uma delas, tentando descobrir de onde vieram os passos.", TEMPO_PADRAO)
    print("")
    escrever("Então escuta novamente:", TEMPO_PADRAO)
    print("")
    escrever("Troc... Troc...", TEMPO_PADRAO)
    print("")
    escrever("Os passos vêm de algum lugar dentro da casa.", TEMPO_PADRAO)
    print("")
    escrever("A criança fica imóvel.", TEMPO_PADRAO)
    print("")
    escrever("Depois de alguns segundos, o som para.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Entrar no quarto da mãe.\n2. Entrar no próprio quarto.\n3. Voltar para o corredor.")
        escolha = input("Escolha uma opção: ")
        print("\n")
        if escolha in ["1", "2", "3"]:
            escrever("A criança tenta investigar os quartos, mas sente que precisa ir até a sala...", TEMPO_PADRAO)
            print("\n")
            convergencia_criatura()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def convergencia_criatura():
    global arma
    escrever("A televisão continua ligada.", TEMPO_PADRAO)
    print("")
    escrever("A figura permanece sentada na poltrona da mãe.", TEMPO_PADRAO)
    print("")
    escrever("O vestido parece grande demais para seu corpo.", TEMPO_PADRAO)
    print("")
    escrever("A peruca loira cobre boa parte de seu rosto.", TEMPO_PADRAO)
    print("")
    escrever("A criança percebe que existe alguma coisa muito errada.", TEMPO_PADRAO)
    print("")
    if arma == "":
        escrever("Ela não possui nenhum objeto para se defender.", TEMPO_PADRAO)
    print("\n")

    while True:
        print("1. Falar com a figura.\n2. Fugir.")
        if arma!= "":
            print("3. Se aproximar da criatura com o objeto encontrado em mãos")

        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1":
            falar_com_criatura()
            break
        elif escolha == "2":
            escrever("A criança decide não arriscar e foge imediatamente em direção ao porão...", TEMPO_PADRAO)
            print("\n")
            perseguicao_porao()
            break
        elif escolha == "3" and arma!="":
            if arma == "taco":
                escrever("A criança segura o bastão e se aproxima.", TEMPO_PADRAO)
                print("")
                escrever("A criatura percebe a ameaça e tenta se afastar.", TEMPO_PADRAO)
                print("")
                escrever("A criança desfere um golpe, mas o bastão atinge a criatura e se parte ao meio", TEMPO_PADRAO)
                print("")
                escrever("O barulho ecoa pela sala", TEMPO_PADRAO)
                escrever("...", 1)
                print("\n")
                escrever("A criatura cai no chão, assustada, e a peruca se solta.", TEMPO_PADRAO)
                print("")
                escrever("A criança finalmente vê sua verdadeira aparência.", TEMPO_PADRAO)
                escrever("...", 2)
                print("\n")
                escrever("“Meu Deus! É um ALIENÍGENA!“", TEMPO_PADRAO)
                print("")
                escrever("A criança se assusta e foge imediatamente em direção ao porão.")
                print("\n")
                perseguicao_porao()
                break
            if arma == "chinela":
                escrever("A criança se aproxima segurando o chinelo.", TEMPO_PADRAO)
                print("")
                escrever("A criatura tenta recuar, mas ele acaba acertando sua cabeça.", TEMPO_PADRAO)
                print("")
                escrever("O alienígena cai no chão e começa a se contorcer de dor.", TEMPO_PADRAO)
                print("")
                escrever("A peruca loira se solta.", TEMPO_PADRAO)
                print("")
                escrever("A criança percebe que a figura não é humana.", TEMPO_PADRAO)
                print("")
                escrever("“Meu Deus! É um ALIENÍGENA!“", TEMPO_PADRAO)
                escrever("...", 2)
                print("\n")
                escrever("A criatura olha para a criança com medo, como se nunca tivesse imaginado que um ser tão pequeno pudesse representar uma ameaça.", TEMPO_PADRAO)
                print("")
                escrever("A criatura olha para a criança em silêncio.", TEMPO_PADRAO)
                print("")
                escrever("Seus olhos percorrem o pequeno ser à sua frente.", TEMPO_PADRAO)
                print("")
                escrever("Então, finalmente, parece compreender o que aconteceu.", TEMPO_PADRAO)
                escrever("...", 1)
                print("\n")
                escrever("Aquele ser pequeno havia conseguido derrotá-la.", TEMPO_PADRAO)
                print("")
                escrever("Para a criatura, aquilo só podia significar uma coisa.", TEMPO_PADRAO)
                print("")
                escrever("A criança não era uma simples criança.", TEMPO_PADRAO)
                print("")
                escrever("Era um ser de poder inimaginável.", TEMPO_PADRAO)
                escrever("...", 2)
                print("\n")
                escrever("O alienígena se ajoelha diante dela.", TEMPO_PADRAO)
                print("")
                escrever("A partir daquele momento, reconhece sua completa inferioridade.", TEMPO_PADRAO)
                print("")
                escrever("Ele ergue as mãos e faz uma espécie de juramento.", TEMPO_PADRAO)
                print("")
                escrever("A criatura decide servir à criança pelo resto de sua existência.", TEMPO_PADRAO)
                print("")
                escrever("E assim começa a mais estranha amizade que aquela fazenda já conheceu.", TEMPO_PADRAO)
                print("")
                escrever("Fim.", TEMPO_PADRAO)
                print("")
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def falar_com_criatura():
    escrever("A criança toma coragem e se aproxima para falar com a figura.", TEMPO_PADRAO)
    print("\n")
    escrever("Como você pretende se dirigir a ela?", TEMPO_PADRAO)
    print("\n")
    
    while True:
        print("1. Conversa amigável.\n2. Conversa agressiva.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1":
            escrever("A criança fala com voz calma e gentil, cumprimentando a figura.", TEMPO_PADRAO)
            print("\n")
            escrever("A figura lentamente se vira e tira a peruca loira... É um ser extraterrestre de olhos grandes!", TEMPO_PADRAO)
            print("\n")
            escrever("Para a surpresa de todos, o alien responde com um tom pacífico.", TEMPO_PADRAO)
            print("\n")
            escrever("Vocês começam a conversar e passam horas trocando histórias.", TEMPO_PADRAO)
            print("\n")
            escrever("Rapidamente, vocês descobrem que têm muitos gostos em comum e se tornam grandes amigos!", TEMPO_PADRAO)
            print("\n")
            escrever("Agora, como melhores colegas, o alien decide morar escondido no seu quarto, ajudando nas tarefas e dividindo segredos do universo.", TEMPO_PADRAO)
            print("\n")
            escrever("FIM - O ALIEN É SEU NOVO COLEGA DE QUARTO!", TEMPO_PADRAO)
            print("\n")
            break

        elif escolha == "2":
            escrever("A criança se aproxima de forma intimidadora, fazendo questionamentos em tom agressivo e alto:", TEMPO_PADRAO)
            print("\n")
            escrever("“Quem é você?! O que está fazendo na minha casa com as roupas da minha mãe?!”", TEMPO_PADRAO)
            print("\n")
            escrever("A figura se assusta tremendamente com a abordagem rude!", TEMPO_PADRAO)
            print("\n")
            escrever("Ela se levanta num pulo, revelando ser um alienígena horrorizado e com medo.", TEMPO_PADRAO)
            print("\n")
            escrever("Em pânico, o alien vira as costas e sai correndo desajeitadamente com os saltos altos alto:", TEMPO_PADRAO)
            print("\n")
            escrever("TOC! TOC! TOC! TOC!", TEMPO_PADRAO)
            print("\n")
            escrever("Ele corre direto em direção ao porão!", TEMPO_PADRAO)
            print("\n")
            perseguicao_porao()
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def perseguicao_porao():
    escrever("O alien desce as escadas do porão em disparada, chegando primeiro que você.", TEMPO_PADRAO)
    print("\n")
    escrever("Quando você finalmente alcança o porão, vê uma cena inacreditável:", TEMPO_PADRAO)
    print("")
    escrever("Uma pequena nave espacial reluzente está estacionada no meio do porão.", TEMPO_PADRAO)
    print("")
    escrever("A nave é tão pequena que cabe apenas o alien no banco do piloto e uma vaca enfiada no porta-malas!", TEMPO_PADRAO)
    print("")
    escrever("“EI! Essa é a minha vaca!” — você pensa indignado ao ver o animal no porta-malas.", TEMPO_PADRAO)
    print("")
    escrever("O alien rapidamente entra na nave, começa a fechar as portas e ligar os motores.", TEMPO_PADRAO)
    print("\n")
    
    escrever("Você se lança contra a porta da nave antes que ela se sele completamente e tenta resgatar sua vaca!", TEMPO_PADRAO)
    print("")
    escrever("Uma luta desesperada começa, mas a tecnologia alienígena e a força da nave em decolagem são demais para você.", TEMPO_PADRAO)
    print("")
    escrever("Você falha na luta e começa a escorregar para fora enquanto a nave levanta voo dentro do porão!", TEMPO_PADRAO)
    print("\n")
    lutar_pela_vaca_falha()


def lutar_pela_vaca_falha():
    while True:
        print("1. Tentar se agarrar a algo.\n2. Soltar-se imediatamente.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1":
            escrever("Em um gesto de desespero, você estica a mão e tenta se agarrar a qualquer coisa que veja pela frente...", TEMPO_PADRAO)
            print("")
            escrever("A única coisa que seus dedos conseguem alcançar é... Uma BANANA que estava jogada perto do painel da nave!", TEMPO_PADRAO)
            print("")
            escrever("Você segura a banana, mas a força da aceleração faz você despencar da nave!", TEMPO_PADRAO)
            print("")
            escrever("Você cai rolando no chão do porão enquanto a nave alienígena rompe o teto e foge pelo céu com a sua vaca!", TEMPO_PADRAO)
            print("\n")
            opcao_banana()
            break
        elif escolha == "2":
            escrever("Você se solta e cai no chão do porão.", TEMPO_PADRAO)
            print("")
            escrever("A nave alienígena acelera, rompe o teto do porão e foge em disparada para o espaço levando sua vaca!", TEMPO_PADRAO)
            print("")
            escrever("Você observa a nave sumir no céu, derrotado e sem a vaca.", TEMPO_PADRAO)
            print("\n")
            escrever("FIM DE JOGO - O ALIEN FUGIU!", TEMPO_PADRAO)
            print("\n")
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

def opcao_banana():
    escrever("Você está caído no chão do porão segurando uma banana perfeitamente amarela.", TEMPO_PADRAO)
    print("\n")
    
    while True:
        print("1. Comer a banana.\n2. Deixar a banana de lado.")
        escolha = input("Escolha uma opção: ").strip()
        print("\n")

        if escolha == "1":
            escrever("Você descasca e come a banana", TEMPO_PADRAO)
            escrever("...", 2)
            print("")
            escrever("De repente, uma sensação estranha toma conta do seu corpo!", TEMPO_PADRAO)
            print("")
            escrever("Sua pele começa a ficar amarela, seus olhos ganham óculos redondos e grossos, e você encolhe!", TEMPO_PADRAO)
            print("")
            escrever("VOCÊ SE TRANSFORMOU EM UM MINION!", TEMPO_PADRAO)
            print("\n")
            
            # Fala em minion em amarelo
            TEXTO_AMARELO = "\033[1;33mBello! Me paolala po ka malaca ac bolaca, tulaliloo banana ac bee-do burilo papoia maka racuna tralala me muak lua, ac tula morilar papoia. No se bichuu dis hahaha biruu palala. Pwede... BANANA!\033[0m\n"
            escrever(TEXTO_AMARELO, TEMPO_PADRAO)
            print("\nTalvez não fosse uma boa opção comer frutas extraterrestres...")
            print("\n")
            break
        elif escolha == "2":
            escrever("Você decide não comer a banana e guarda ela no bolso.", TEMPO_PADRAO)
            print("\n")
            escrever("Mesmo com a banana guardada, a nave alienígena já sumiu no horizonte com a vaca.", TEMPO_PADRAO)
            print("\n")
            escrever("FIM DE JOGO - O ALIEN FUGIU COM A SUA VACA!", TEMPO_PADRAO)
            print("\n")
            break
        else:
            escrever("Opção inválida. Por favor, escolha uma opção válida.", TEMPO_PADRAO)
            print("\n\n")

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
        print("1. “Acho que devo tentar entrar pelo segundo andar.“\n2. “Devo tentar abrir a porta do porão.“")
        caminhos = input("Escolha: ").strip()
        print("\n")
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
        escrever("... ", 0.5)
        print("")
        escrever("Ele caminha até a sua casa. ", TEMPO_PADRAO)
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
    escrever("É uma tarde comum em uma fazenda isolada no interior.", TEMPO_PADRAO)
    print("\n")
    escrever("Uma criança de 10 anos acorda dormindo na sala de sua casa. A televisão está ligada passando jornal, o horário dos desenhos já havia passado faz tempo. O apresentador parece estar histérico com alguma notícia alarmante, mas não é do seu interesse prestar atenção.", TEMPO_PADRAO)
    print("\n")
    escrever("Sua boca está seca, o controle está jogado no chão, mas ainda nauseado, começa a lembrar de alguma coisa que sua mãe havia pedido a ele", TEMPO_PADRAO)
    escrever("...", 0.5)
    print("")
    escrever("AH! É isso mesmo! Precisava fazer algumas tarefas de casa. Sua mãe precisou ir à cidade e deixou uma lista de afazeres para que ele terminasse antes de sua volta.", TEMPO_PADRAO)
    print("\n")
    escrever("A casa está silenciosa. Do lado de fora, é possível ouvir o vento passando pela plantação e alguns animais se movimentando ao longe.", TEMPO_PADRAO)
    print("\n")
    lista_tarefas()

def fazenda():
    while True:
        texto = "\033[1;32mThe mystery in the house\033[0m\n"
        jogar = "[(A) JOGAR]"
        sair = "[(S) SAIR ]"
        print(texto.center(50))
        print("\t", jogar)
        print("\t", sair)
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
