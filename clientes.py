# clientes.py - RF01, RF02, RF03
# Estrutura de dados: lista de dicionários (cada cliente = 1 dicionário)
# "clientes" é recebido como parâmetro em cada função (quem carrega e
# salva em dados/dados.json é o main.py, de forma centralizada).


def cadastrar_cliente(clientes):
    """RF01 - Cadastra um novo cliente na lista."""
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail (opcional): ").strip()

    if not nome or not telefone:
        print("Nome e telefone são obrigatórios. Cadastro não realizado.")
        return

    if len(nome) < 3:
        print("Nome deve ter pelo menos 3 caracteres. Cadastro não realizado.")
        return

    if not telefone.isdigit() or len(telefone) < 10 or len(telefone) > 11:
        print("Telefone deve conter só números, com DDD (10 ou 11 dígitos). Cadastro não realizado.")
        return

    maior_id = 0
    for c in clientes:
        if c["id"] > maior_id:
            maior_id = c["id"]
    novo_id = maior_id + 1

    clientes.append({"id": novo_id, "nome": nome, "telefone": telefone, "email": email})
    print(f"Cliente '{nome}' cadastrado com sucesso! (ID: {novo_id})")


def consultar_cliente(clientes):
    """RF02 - Busca clientes pelo nome ou telefone."""
    print("\n--- Consulta de Cliente ---")
    termo = input("Digite o nome ou telefone para buscar: ").strip().lower()

    encontrados = []
    for c in clientes:
        if termo in c["nome"].lower() or termo in c["telefone"]:
            encontrados.append(c)

    if not encontrados:
        print("Nenhum cliente encontrado.")
        return

    for c in encontrados:
        print(f"  ID: {c['id']} | {c['nome']} | {c['telefone']} | {c['email']}")


def alterar_cliente(clientes):
    """RF03 - Localiza um cliente pelo ID e atualiza seus dados."""
    print("\n--- Alteração de Cliente ---")
    try:
        id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
    except ValueError:
        print("ID inválido. Deve ser um número.")
        return

    cliente = None
    for c in clientes:
        if c["id"] == id_cliente:
            cliente = c
            break

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print(f"Cliente encontrado: {cliente['nome']} - {cliente['telefone']}")
    print("Deixe em branco para manter o valor atual.")

    novo_nome = input(f"Novo nome [{cliente['nome']}]: ").strip()
    novo_telefone = input(f"Novo telefone [{cliente['telefone']}]: ").strip()
    novo_email = input(f"Novo e-mail [{cliente['email']}]: ").strip()

    if novo_nome:
        cliente["nome"] = novo_nome
    if novo_telefone:
        cliente["telefone"] = novo_telefone
    if novo_email:
        cliente["email"] = novo_email

    print("Dados atualizados com sucesso!")
