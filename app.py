import os

restaurantes = [{'nome':'Outback', 'categoria':'Carnes', 'ativo':True},
                {'nome':'Madero', 'categoria':'Lanche', 'ativo':True},
                {'nome':'Si senhor', 'categoria':'Mexicana', 'ativo':False}]

def exibir_nome_do_programa():
    print('𝔹𝕖𝕞 𝕧𝕚𝕟𝕕𝕠 𝕒𝕠 ℕ𝕒𝕣𝕚𝕕')

def exibir_opcoes():
    try:
        opcao_escolhida = int (input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1: 
                cadastrar_novo_restaurante() 
            case 2: 
                listar_restaurante()
            case 3:
                alternar_estado_do_restaurante()
            case 4:
                finalzar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante} que deseja cadastrar: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurente {nome_do_restaurante} foi cadastrado com sucesso!\n')
    retorno_menu_principal()

def listar_restaurante():
    exibir_subtitulos('Lista de Restaurantes\n')

    print(f'{'Nome'.ljust(11)} | {'Categoria'.ljust(10)} | Estado')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-{nome_restaurante.ljust(10)} | {categoria.ljust(10)} | {ativo}')

    retorno_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulos('Alternando o estado do seu restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')   

    retorno_menu_principal()

def opcoes():
    print ('escolha uma opção: \n')
    print('1 Cadastrar o seu restaurante')
    print('2 Listar restaurantes cadastrados')
    print('3 Alterar o estado do seu restaurante')
    print('4 Sair \n')

def finalzar_app():
    exibir_subtitulos('Até mais, volte sempre!')

def opcao_invalida():
    print('opção invalida\n')
    retorno_menu_principal()

def exibir_subtitulos(texto):
    os.system('clear')
    print(texto)

def retorno_menu_principal():
    input('\nPrecione uma tecla para voltar ao menu principal. ')
    main()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    opcoes()
    exibir_opcoes()
    
if __name__ == '__main__':
    main() 