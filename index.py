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
        elif opcaoUsuario == 4:
            verificarNome()
        elif opcaoUsuario == 5:
            remover()
        elif opcaoUsuario == 6:
            alteraNome()
        else:
            break

def continuar():

    desejaContinuar = int(input("Deseja continuar? 1= sim 2= não  "))
    if desejaContinuar == 1:
        verificar()
    else:
        exit

def cadastreUsuario():

    qtdDeUsuario = int(input("Quantos usuários voce deseja criar? "))
    aux = 0
    while (aux < qtdDeUsuario):
        listaDeUsuario.append (input("Qual o nome do usuario: "))
        listaDeUsuario.append (input("Qual o email do usuario:  "))
        print("Usuario criado")
        aux = aux+1



def usuarioCadastrado ():
    s = " - "
    print(s.join(listaDeUsuario))

def ordemAlfabetica():
    listaDeUsuario.sort()
    print(listaDeUsuario)

def verificarNome():
    verificarNome = input("Qual o nome do usuario que deseja verificar ?")
    verificarNome = listaDeUsuario
    for Verifique in verificarNome:
        print (Verifique)


def remover():
    removerUsuario = input("Qual usuario voce deseja remover, informe o email")
    listaDeUsuario.remove (removerUsuario)
    print(removerUsuario)

def alteraNome():
    email = input("digite o e-mail  do usuário a ser alterado: ")
    for i in listaDeUsuario:
     if i["email"] == email:
        i["nome"] = input("digite o novo nome: ")

def main():
    verificar()

if __name__ == "__main__":
    main()
