#biblioteca que limpa o terminal
import os #os.system('cls')

#funçao que passa o nome do app
def nome_app():
    print('Nome Generico')
    print('============================================\n')

#funcao que exibe opçoes para o usuario
def exibir_opcoes():
    print('1- ')
    print('2- ')
    print('3- ')
    print('4- ')
    print('5- Sair\n')

#funcao que finaliza o app
def finalizar_app():
    os.system('cls')
    print('finalizando o app...\n')

def voltar_app():
    input('Pressione Enter para voltar ao menu principal...')
    main()

#funçao de opçao invalida, quando a resposta nao é esperada
def opcao_invalida():
    os.system('cls')
    print('Opção inválida, tente novamente\n')
    voltar_app()


#funçao para escolher a opçao
def escolher_opcao():
    print('=============================================')
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        #cada opcao ativa uma funçao
        if opcao == 1:
            print('opção 1 selecionada')
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