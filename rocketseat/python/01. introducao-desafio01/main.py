def adicionar_contato(contatos, novo_contato):
    contato = {"nome": novo_contato["nome"], "telefone": novo_contato["telefone"], "email": novo_contato["email"], "favorito": False}
    contatos.append(contato)
    print("\nNovo Contato adicionado com sucesso.")
    return

def visualizar_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✓" if contato["favorito"] else " "
        print(f"{indice}. FAV: [{favorito}] - NOME: {contato["nome"]} | TELEFONE: {contato["telefone"]} | E-MAIL: {contato["email"]}")
    return

def visualizar_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. NOME: {contato["nome"]} | TELEFONE: {contato["telefone"]} | E-MAIL: {contato["email"]}")
    return

def editar_contato(contatos, cod_contato, contato_editado):
    indice_contato = int(cod_contato) - 1 if cod_contato.isdigit() else -1
    
    if indice_contato >= 0 and indice_contato < len(contatos):
        contatos[indice_contato]["nome"] = contato_editado["nome"]
        contatos[indice_contato]["telefone"] = contato_editado["telefone"]
        contatos[indice_contato]["email"] = contato_editado["email"]
        print("Contato editado com sucesso.")
    else:
        print("Código de contato inválido.")
    return

def alternar_favorito(contatos, cod_contato):
    indice_contato = int(cod_contato) - 1 if cod_contato.isdigit() else -1
    
    if indice_contato >= 0 and indice_contato < len(contatos):
        if contatos[indice_contato]["favorito"]:
            contatos[indice_contato]["favorito"] = False
            print(f"Contato {indice_contato} desmarcado como favorito.")
        else:
            contatos[indice_contato]["favorito"] = True
            print(f"Contato {indice_contato} marcado como favorito.")
    else:
        print("Código de contato inválido.")
    return

def apagar_contato(contatos, cod_contato):
    indice_contato = int(cod_contato) - 1 if cod_contato.isdigit() else -1
    
    if indice_contato >= 0 and indice_contato < len(contatos):
        del contatos[indice_contato]
        print("Contato removido com sucesso.")
    else:
        print("Código de contato inválido.")
    return

contatos = []

print("\n----AGENDA----")
while True:
    print("\nMenu da Agenda:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Alternar favorito")
    print("5. Visualizar favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        print("\nAdicionar Contato:")
        nome_contato = input("Digite o Nome: ")
        telefone_contato = input("Digite o Telefone: ")
        email_contato = input("Digite o E-mail: ")
        novo_contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato}
        adicionar_contato(contatos, novo_contato)
    elif opcao == "2":
        visualizar_contatos(contatos)
    elif opcao == "3":
        visualizar_contatos(contatos)
        cod_contato = input("Digite o código do contato que deseja editar: ")
        nome_editado = input("Digite o novo nome: ")
        telefone_editado = input("Digite o novo telefone: ")
        email_editado = input("Digite o novo e-mail: ")
        contato_editado = {"nome": nome_editado, "telefone": telefone_editado, "email": email_editado}
        editar_contato(contatos, cod_contato, contato_editado)
    elif opcao == "4":
        visualizar_contatos(contatos)
        cod_contato = input("Digite o código do contato que deseja marcar/desmarcar como favorito: ")
        alternar_favorito(contatos, cod_contato)
        print("Lista atualizada:")
        visualizar_contatos(contatos)
    elif opcao == "5":
        visualizar_contatos_favoritos(contatos)
    elif opcao == "6":
        visualizar_contatos(contatos)
        cod_contato = input("Digite o código do contato que deseja apagar: ")
        apagar_contato(contatos, cod_contato)
    else:
        break