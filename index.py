def verificarCondicoes():
    opcaoUsuario = int(input("Qual ação desejada? se desejar sair, digite o numeral 8! "))
    return opcaoUsuario

listaDeUsuario = []

def verificar ():
    while True:
        print("""********************* 

 1- Cadastrar novo usuário(nome completo e email)
 2- Exibir todos us usuários, listando por ordem de cadastro
 3- Exibir todos os usuários cadastrados listando por ordem alfabética
 4- Verificar se o usuário faz parte da lista, buscando-o pelo seu nome
 5- Remover um usuário cadastrado, buscando-o por seu e-mail
 6- Alterar o nome de um usuário, buscando-o por seu e-mail
 
 *************************

""" 
)

        opcaoUsuario = verificarCondicoes()

        if opcaoUsuario == 1:
            cadastreUsuario()
        elif opcaoUsuario == 2:
            usuarioCadastrado()
        elif opcaoUsuario == 3:
            ordemAlfabetica()
