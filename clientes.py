# clientes.py

def cadastrar_cliente(clientes):
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome do cliente: ").strip()
    telefone = input("Telefone: ").strip()
    
    if not nome or not telefone:
        print("Erro: Nome e telefone são obrigatórios! (RNF03)")
        return

    novo_id = max([c['id'] for c in clientes], default=0) + 1
    novo_cliente = {"id": novo_id, "nome": nome, "telefone": telefone}
    clientes.append(novo_cliente)
    print(f"Cliente '{nome}' cadastrado com sucesso!")

def consultar_cliente(clientes):
    print("\n--- Consulta de Clientes ---")
    termo = input("Digite o nome ou telefone para busca: ").strip().lower()
    
    encontrados = [c for c in clientes if termo in c['nome'].lower() or termo in c['telefone']]
    
    if encontrados:
        for c in encontrados:
            print(f"ID: {c['id']} | Nome: {c['nome']} | Telefone: {c['telefone']}")
    else:
        print("Nenhum cliente encontrado.")

def alterar_cliente(clientes):
    print("\n--- Alteração de Cliente ---")
    try:
        id_cliente = int(input("Digite o ID do cliente que deseja alterar: "))
        cliente = next((c for c in clientes if c['id'] == id_cliente), None)
        
        if cliente:
            print(f"Dados atuais -> Nome: {cliente['nome']} | Telefone: {cliente['telefone']}")
            novo_nome = input("Novo nome (pressione Enter para manter): ").strip()
            novo_telefone = input("Novo telefone (pressione Enter para manter): ").strip()
            
            if novo_nome:
                cliente['nome'] = novo_nome
            if novo_telefone:
                cliente['telefone'] = novo_telefone
            
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")
    except ValueError:
        print("Erro: ID deve ser um número inteiro. (RNF06)")