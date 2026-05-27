#biblioteca que limpa o terminal
import os #os.system('cls')

#funçao que passa o nome do app
def nome_app():
    print('Nome Generico')
    print('============================================\n')

#funcao que exibe opçoes para o usuario
def exibir_opcoes():
    print('1- Proposta e Problema do Projeto\n')
    print('2- Solução do Projeto\n')
    print('3- ')
    print('4- ')
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


#funçao para escolher a opçao
def escolher_opcao():
    print('=============================================')
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        #cada opcao ativa uma funçao
        if opcao == 1:
            proposta_problema_projeto()
        elif opcao == 2:
            print('opção 2 selecionada')
        elif opcao == 3:
            print('opção 3 selecionada')
        elif opcao == 4:
            print('opção 4 selecionada')
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