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
    print('Space Route - Plataforma Inteligente de Monitoramento e Gerenciamento do Espaço Aéreo\n')
    print('============================================\n')

#funcao que exibe opçoes para o usuario
def exibir_opcoes():
    print('1- Proposta e Problema do Projeto\n')
    print('2- Descrição da Solução do Projeto\n')
    print('3- Suporte Tecnológico Coerente e Viabilidade\n')
    print('4- Simulação de Desvio de Rotas\n') 
    print('5- Simulação de Detrito Espacial para Desvio\n')
    print('6- Simulação de Classificação Simples de Lixo Espacial\n')
    print('7- Simulação de Monitoramento Dinâmico do Espaço Aéreo e Orbital\n')
    print('8- Sair\n')

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

#funçao que representa a opçao 4, onde o desvio de rotas é simulado de forma interativa, permitindo que o usuário escolha uma rota e veja se há necessidade de desviar para uma opção mais segura
def desvio_rotas():
    os.system('cls')
    print('Aeronaves e foguetes poderiam receber alertas automáticos de risco de colisão, permitindo que pilotos e controladores de voo tomem decisões informadas sobre desvios de rota ou ajustes de altitude para evitar áreas congestionadas ou perigosas\n')
    input('Pressione Enter para simular um alerta de risco de colisão...')
    os.system('cls')
    print('DESVIO DE ROTAS - SIMULAÇÃO INTERATIVA')
    print('Aqui você pode escolher a rota atual e ver se há necessidade de desviar para uma opção mais segura. (claro no projeto real isso sera automatico)\n')
    #apresenta rotas com varios status
    rotas = {
        1: {'nome': 'Rota 1', 'status': 'livre', 'descricao': 'Trajeto direto, sem problemas detectados.'},
        2: {'nome': 'Rota 2', 'status': 'congestionada', 'descricao': 'Tráfego aéreo intenso e risco de atraso.'},
        3: {'nome': 'Rota 3', 'status': 'perigosa', 'descricao': 'Área com risco de colisão por detritos ou tráfego espacial.'},
        4: {'nome': 'Rota 4', 'status': 'monitorada', 'descricao': 'Risco moderado, mas ainda aceitável com acompanhamento.'},
        5: {'nome': 'Rota 5', 'status': 'em_alerta', 'descricao': 'Sinais de colisão iminente e desvio recomendado.'},
        6: {'nome': 'Rota 6', 'status': 'manutencao', 'descricao': 'Rotina em revisão operacional, evite uso imediato.'}
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

    status = rota_atual['status']
    #desorganizado por enquanto, mas a ideia é mostrar o status da rota escolhida e recomendar ações com base nesse status
    if status == 'livre':
        print('Status: Sem necessidade de desvio. A rota está segura para prosseguir.')
    elif status in ('monitorada', 'congestionada'):
        alternativas = [
            rota for chave, rota in rotas.items()
            if chave != escolha and rota['status'] in ('livre', 'monitorada')
        ]
        print('Status: Rota com risco moderado ou tráfego intenso detectado.')
        print('Recomendação: mantenha monitoramento e considere desvio preventivo.')
        if alternativas:
            print('Sugestão de desvio para rotas mais seguras:')
            for rota in alternativas:
                print(f"- {rota['nome']}: {rota['descricao']}")
        else:
            print('Não há rotas adequadas disponíveis no momento. Ajuste manualmente a trajetória.')
    elif status in ('perigosa', 'em_alerta'):
        alternativas = [
            rota for chave, rota in rotas.items()
            if chave != escolha and rota['status'] in ('livre', 'monitorada')
        ]
        print('Status: Risco alto detectado. Desvio imediato recomendado.')
        if alternativas:
            print('Sugestões de desvio prioritárias:')
            for rota in alternativas:
                print(f"- {rota['nome']}: {rota['descricao']}")
        else:
            print('Nenhuma rota alternativa segura foi identificada. Avalie espera ou correção manual.')
    elif status == 'manutencao':
        print('Status: Rota em manutenção operacional. Evite uso até novo alinhamento da navegação.')
        alternativas = [
            rota for chave, rota in rotas.items()
            if chave != escolha and rota['status'] == 'livre'
        ]
        if alternativas:
            print('Rotas alternativas recomendadas:')
            for rota in alternativas:
                print(f"- {rota['nome']}: {rota['descricao']}")
        else:
            print('Não há rota livre disponível no momento.')
    else:
        print('Status: Situação não categorizada. Verifique a rota com o sistema de monitoramento.')

    voltar_app()
    
#funçao que representa a opçao 5, onde é feita uma simulaçao de detrito espacial para desvio,
def protocolo_desvio():
    os.system('cls')
    print('PROTOCOLO DE DESVIO - SIMULAÇÃO INTERATIVA')
    print('Este protótipo simples calcula a janela de desvio usando apenas a fórmula da distância entre os pontos.\n')

    continuar = 's'
    while continuar.lower() == 's':
        try:
            print('Informe as coordenadas da rota atual e do detrito para calcular a distância de desvio.')
            x1 = float(input('Digite a coordenada X da rota atual: '))
            y1 = float(input('Digite a coordenada Y da rota atual: '))
            x2 = float(input('Digite a coordenada X do detrito espacial: '))
            y2 = float(input('Digite a coordenada Y do detrito espacial: '))

            # cálculo da distância com a fórmula
            distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            distancia = round(distancia, 2)

            print(f'\nDistância calculada entre os pontos: {distancia} km')

            # desvio estimado usando apenas a distância calculada
            desvio_estimado = distancia
            desvio_estimado = round(desvio_estimado, 2)
            print(f'Desvio estimado: {desvio_estimado} km')
            #verificação do desvio estimado para recomendar ações, onde valores menores indicam necessidade de desvio mais urgente
            if desvio_estimado <= 5:
                print('Recomendação: desvio imediato para rota alternativa.')
            elif desvio_estimado <= 10:
                print('Recomendação: desvio precaucional com monitoramento contínuo.')
            else:
                print('Recomendação: manter a rota com monitoramento contínuo.')

        except ValueError:
            print('Entrada inválida. Digite apenas números.\n')

        continuar = input('\nDeseja realizar outra simulação? (s/n): ').strip().lower()
        os.system('cls')

    print('Retornando ao menu principal...')
    input('Pressione Enter para continuar...')
    main()

#função que representa a opção 6, onde é feita uma classificação simples de lixo espacial
def monitoramento_dinamico():
    os.system('cls')
    print('MONITORAMENTO DINÂMICO')
    print('Simulação simples de atualização automática do cenário aéreo e orbital.\n')

    try:
        att = int(input('Quantas atualizações você deseja observar? (máximo 7) '))
        if att <= 0:
            print('Digite um número maior que zero.')
            voltar_app()
            return
        if att > 7:
            print('Limite máximo de 7 atualizações atingido.')
            print('Exibindo apenas as primeiras 7 atualizações.')
            input('Pressione Enter para continuar...')
            att = 7

        for passo in range(1, att + 1):
            os.system('cls')
            print(f'ATUALIZAÇÃO {passo}/{att}')
            #pega valores aleatorios para simular o monitoramento
            rota = random.choice(['Rota Norte', 'Rota Sul', 'Rota Leste', 'Rota Oeste'])
            trafego = random.choice(['baixo', 'médio', 'alto']) #verifica se existem aeronaves,foguetes ou satélites próximos
            detrito = random.choice(['nenhum', 'leve', 'moderado'])

            print(f'Rota monitorada: {rota}')
            print(f'Tráfego aéreo: {trafego}')
            print(f'Detrito orbital detectado: {detrito}')
            #avaliaçao para recomendaçao de açao
            if trafego == 'alto' and detrito == 'moderado':
                print('Ação sugerida: aumentar o monitoramento e preparar desvio imediato.')
            elif detrito == 'moderado':
                print('Ação sugerida: monitoramento reforçado, possível ajuste de rota.')
            elif detrito == 'leve':
                print('Ação sugerida: manter atenção na área orbital próxima.')
            else:
                print('Ação sugerida: condição estável, acompanhamento normal.')

            if passo < att:
                input('\nPressione Enter para a próxima atualização...')
            else:
                input('\nPressione Enter para voltar ao menu...')

        main()

    except ValueError:
        print('Entrada inválida. Digite apenas números.')
        voltar_app()


def classificacao_lixo_espacial():
    os.system('cls')
    print('CLASSIFICAÇÃO DE LIXO ESPACIAL')
    print('A classificação será feita automaticamente para os 5 exemplos abaixo.\n')
    objetos = {
        1: {'nome': 'Fragmento de painel solar', 'tamanho': 8, 'tipo': 1},
        2: {'nome': 'Pedaço de estrutura metálica', 'tamanho': 15, 'tipo': 2},
        3: {'nome': 'Bloco de combustível vazio', 'tamanho': 30, 'tipo': 3},
        4: {'nome': 'Parte de antena danificada', 'tamanho': 12, 'tipo': 2},
        5: {'nome': 'Resíduo de satélite antigo', 'tamanho': 22, 'tipo': 3},
    }

    for codigo, item in objetos.items():
        print(f'{codigo} - {item["nome"]} (tamanho: {item["tamanho"]} cm)')
    
    input('Pressione Enter para continuar...')
    os.system('cls')

    print('\nClassificando todos os exemplos automaticamente...')

    for codigo, item in objetos.items():
        tamanho = float(item['tamanho'])
        tipo = int(item['tipo'])
        pesos_tipo = {1: 1.0, 2: 3.0, 3: 6.0}
        pontuacao = round((tamanho * 0.2) + pesos_tipo[tipo], 1)

        if pontuacao < 5:
            categoria = 'Classe Verde'
            descricao = 'Risco baixo: fragmento pequeno ou leve, monitoramento simples.'
        elif pontuacao < 10:
            categoria = 'Classe Amarela'
            descricao = 'Risco médio: objeto com tamanho ou massa suficiente para exigir atenção.'
        else:
            categoria = 'Classe Vermelha'
            descricao = 'Risco alto: objeto grande ou pesado, exige acompanhamento e desvio cauteloso.'

        print(f'\n{codigo} - {item["nome"]}')
        print(f'Tamanho: {tamanho} cm')
        print(f'Tipo de lixo espacial: {item["nome"]}')
        print(f'Pontuação de risco: {pontuacao}')
        print(f'Categoria: {categoria}')
        print(f'Descrição: {descricao}')
        print('---------------------------------------------')

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
            protocolo_desvio()
        elif opcao == 6:
            classificacao_lixo_espacial()
        elif opcao == 7:
            monitoramento_dinamico()
        elif opcao == 8:
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