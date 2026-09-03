# servicos.py
from status_agenda import SERVICO_ATIVO, SERVICO_INATIVO

def cadastrar_servico(servicos):
    print("\n--- Cadastro de Serviço ---")
    nome = input("Nome do serviço (ex: Corte, Manicure): ").strip()
    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return

    try:
        preco = float(input("Preço (R$): "))
    except ValueError:
        print("Erro: Preço inválido. (RNF03)")
        return

    if preco <= 0:
        print("Erro: Preço deve ser maior que zero. (RNF03)")
        return

    novo_id = max([s['id'] for s in servicos], default=0) + 1
    servico = {
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "status": SERVICO_ATIVO
    }
    servicos.append(servico)
    print(f"Serviço '{nome}' cadastrado com sucesso!")


def alterar_inativar_servico(servicos):
    print("\n--- Alterar/Inativar Serviço ---")
    if not servicos:
        print("Nenhum serviço cadastrado.")
        return

    for s in servicos:
        print(f"ID: {s['id']} | Nome: {s['nome']} | Preço: R${s['preco']:.2f} | Status: {s['status']}")

    try:
        id_servico = int(input("Digite o ID do serviço: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    servico = next((s for s in servicos if s['id'] == id_servico), None)
    if not servico:
        print("Serviço não localizado.")
        return

    opcao = input("Deseja [A]lterar dados ou [I]nativar/Ativar status? ").strip().upper()

    if opcao == 'A':
        novo_nome = input("Novo nome (Enter para pular): ").strip()
        novo_preco_str = input("Novo preço (Enter para pular): ").strip()

        # Valida o preço ANTES de aplicar qualquer alteração,
        # evitando atualização parcial (nome muda mas preço não).
        novo_preco = None
        if novo_preco_str:
            try:
                novo_preco = float(novo_preco_str)
            except ValueError:
                print("Erro: Preço inválido. (RNF03)")
                return
            if novo_preco <= 0:
                print("Erro: Preço deve ser maior que zero. (RNF03)")
                return

        if novo_nome:
            servico['nome'] = novo_nome
        if novo_preco is not None:
            servico['preco'] = novo_preco

        print("Serviço atualizado!")

    elif opcao == 'I':
        servico['status'] = SERVICO_INATIVO if servico['status'] == SERVICO_ATIVO else SERVICO_ATIVO
        print(f"Status alterado para: {servico['status']}.")

    else:
        print("Opção inválida.")