#biblioteca que limpa o terminal
import os #os.system('cls')
#biblioteca para calculos
import math 
#biblioteca para gerar tempo
import time
#biblioteca para gerar numeros aleatorios
import random

#funçao que passa o nome do app
def nome_app():
    print('Nome Generico')
    print('============================================\n')

#funcao que exibe opçoes para o usuario
def exibir_opcoes():
    print('1- Proposta e Problema do Projeto\n')
    print('2- Descrição da Solução do Projeto\n')
    print('3- Suporte Tecnológico Coerente e Viabilidade\n')
    print('4- Protipo e Demonstração de Viabilidade\n') #desvio de rotas, monitoramento de tráfego aéreo e espacial, previsão de riscos de colisão, categorizaçao
    print('5- Sair\n')

#funcao que finaliza o app
def finalizar_app():
    os.system('cls')
    print('finalizando o app...\n')

#funcao que volta para o menu principal, usada em varias partes do app
def voltar_app():
    input('Pressione Enter para voltar ao menu principal...')
    main()

#funçao de opçao invalida, quando a resposta nao é esperada
def opcao_invalida():
    os.system('cls')
    print('Opção inválida, tente novamente\n')
    voltar_app()

#funcao que representa a opcao 1, onde o projeto é apresentado e o problema é explicado
def proposta_problema_projeto():
    #primeira parte da funçao, onde o projeto é apresentado
    os.system('cls')
    print('O projeto se trata do desenvolvimento de uma plataforma inteligente de monitoramento e gerenciamento do espaço aéreo baseada em dados satelitais e orbitais em tempo real.\n')
    print('Se encaixa nem três possiveis ODS:\n')
    #ods relacionados ao projeto
    ods = ['ODS 9 (Indústria, Inovação e Infraestrutura)', 'ODS 11 (Cidades e Comunidades Sustentáveis)', 'ODS 13 (Ação pelo Clima)'] #lista de ODS que se encaixam no projeto
    for i, item in enumerate(ods, start=1): #enumeraçao dos ODS para exibir na tela
        print(f' {i}- {item}\n')

    input('Pressione Enter para continuar...')
    os.system('cls')
    #segunda parte da funçao, onde o problema é apresentado
    print('O problema está no aumento do tráfego aéreo e espacial derivado de iniciativas como turismo espacial e maior quantidade de missões para o espaço gera riscos cada vez maiores como:\n')
    #riscos relacionados ao projeto
    riscos = ['colisões entre aeronaves;','conflitos de rota;','acidentes envolvendo foguetes e satélites;','impactos causados por lixo espacial;','falhas de comunicação entre sistemas separados de monitoramento.'] #lista de riscos relacionados ao projeto
    for risco in riscos: #em vez de enumerar os riscos apenas foram listados
        print(f"• {risco}")
    print('\nPois hoje, muitos dados ficam descentralizados, dificultando respostas rápidas e decisões mais seguras em termos de definição de rota.\n')

    voltar_app()

#funçao que representa a opçao 2, onde a soluçao do projeto é explicada
def solucao_projeto():
    os.system('cls')
    print('A solução funcionará como uma forma de integrar informações de companhias aéreas, sistemas de navegação de aeronaves pessoais e operações espaciais, reunindo dados de aviões, helicópteros, foguetes e objetos orbitais como lixo espacial\n')
    print('Uma única infraestrutura com o propósito de aumentar a segurança e a eficiência do tráfego aéreo, utilizando análise contínua de dados para prever riscos de colisão, calcular rotas mais seguras e gerar desvios automáticos de rota de maneira precisa e dinâmica\n')
    print('Além disso, a solução auxiliará operações aeroespaciais críticas, permitindo que lançamentos e retornos de foguetes ocorram de forma mais segura através do monitoramento simultâneo do tráfego aéreo e de possíveis riscos orbitais como detritos espaciais e satélites proximos\n')
    voltar_app()

#funçao que representa a opçao 3, onde a viabilidade técnica do projeto é explicada
def viabilidade_tecnica():
    os.system('cls')
    print('A viabilidade técnica do projeto é suportada por avanços recentes em diversas áreas tecnológicas, incluindo:\n')
    lista_variabilidades = ['satélites e sistemas GNSS/GPS','inteligência artificial e machine learning','sensores orbitais e radares','APIs de tráfego aéreo e espacial','redes de comunicação aeronáutica' 'entre outros.']
    for variabilidade in lista_variabilidades:
        print(f"• {variabilidade}")

    print('\nA proposta é plausível porque combina em grande parte tecnologias já existentes em uma só plataforma integrada.Empresas e organizações espaciais e de aviação já utilizam monitoramento em tempo real, previsão de rotas e rastreamento orbital, então o diferencial seria centralizar e automatizar essas informações em um único sistema inteligente incluindo a rastreabilidade e classificação de lixo espacial junto ao restante do tráfego aéreo e orbital\n')
    voltar_app()

def desvio_rotas():
    os.system('cls')
    print('Aeronaves e foguetes poderiam receber alertas automáticos de risco de colisão, permitindo que pilotos e controladores de voo tomem decisões informadas sobre desvios de rota ou ajustes de altitude para evitar áreas congestionadas ou perigosas\n')
    input('Pressione Enter para simular um alerta de risco de colisão...')
    os.system('cls')
    print('DESVIO DE ROTAS - SIMULAÇÃO INTERATIVA')
    print('Aqui você pode escolher a rota atual e ver se há necessidade de desviar para uma opção mais segura.\n')

    rotas = {
        1: {'nome': 'Rota 1', 'status': 'livre', 'descricao': 'Trajeto direto, sem problemas detectados.'},
        2: {'nome': 'Rota 2', 'status': 'congestionada', 'descricao': 'Tráfego aéreo intenso e risco de atraso.'},
        3: {'nome': 'Rota 3', 'status': 'perigosa', 'descricao': 'Área com risco de colisão por detritos ou tráfego espacial.'}
    }
    for chave, rota in rotas.items():
        print(f"{chave} - {rota['nome']} ({rota['status']}) - {rota['descricao']}")

    try:
        escolha = int(input('\nDigite o número da rota atual: '))
        if escolha not in rotas:
            raise ValueError #verifica se a escolha é válida, caso contrário levanta um erro para ser tratado
    except ValueError:
        print('\nOpção inválida. Voltando ao menu principal...')
        input('Pressione Enter para continuar...')
        main()
        return

    rota_atual = rotas[escolha]
    print(f"\nVocê selecionou: {rota_atual['nome']} ({rota_atual['status']})")

    if rota_atual['status'] == 'livre':
        print('Status: Sem necessidade de desvio. A rota está segura para prosseguir.')
    else:
        alternativas = [rota for rota in rotas.values() if rota['status'] == 'livre']
        print('Status: Rota com risco detectado.')
        if alternativas:
            print('Sugestão de desvio para rotas mais seguras:')
            for rota in alternativas:
                print(f"- {rota['nome']}: {rota['descricao']}")
        else:
            print('Não há rotas livres disponíveis no momento. Avalie aguardar ou ajustar rota manualmente.')

    voltar_app()

#funçao para escolher a opçao
def escolher_opcao():
    print('=============================================')
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        #cada opcao ativa uma funçao
        if opcao == 1:
            proposta_problema_projeto()
        elif opcao == 2:
            solucao_projeto()
        elif opcao == 3:
            viabilidade_tecnica()
        elif opcao == 4:
            desvio_rotas()
        elif opcao == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#criei a ordem
def main():
    os.system('cls')
    nome_app()
    exibir_opcoes()
    escolher_opcao()

#chamei a ordem
if __name__ == "__main__":
    main()