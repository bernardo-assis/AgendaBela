# agendamentos.py
from status_agenda import AGENDADO, CONCLUIDO, CANCELADO, SERVICO_ATIVO

def cadastrar_agendamento(agendamentos, clientes, servicos):
    print("\n--- Novo Agendamento ---")
    if not clientes or not servicos:
        print("Erro: Cadastre clientes e serviços antes de agendar.")
        return

    try:
        id_cliente = int(input("ID do Cliente: "))
        id_servico = int(input("ID do Serviço: "))
        data = input("Data (DD/MM/AAAA): ").strip()
        hora = input("Horário (HH:MM): ").strip()

        cliente = next((c for c in clientes if c['id'] == id_cliente), None)
        servico = next((s for s in servicos if s['id'] == id_servico and s['status'] == SERVICO_ATIVO), None)

        if cliente and servico:
            novo_id = max([a['id'] for a in agendamentos], default=0) + 1
            novo_agendamento = {
                "id": novo_id,
                "cliente_nome": cliente['nome'],
                "servico_nome": servico['nome'],
                "data": data,
                "hora": hora,
                "status": AGENDADO
            }
            agendamentos.append(novo_agendamento)
            print("Agendamento realizado com sucesso!")
        else:
            print("Cliente não encontrado ou Serviço inativo/inexistente.")
    except ValueError:
        print("Erro: IDs devem ser numéricos.")

def listar_agendamentos(agendamentos):
    print("\n--- Lista de Agendamentos ---")
    if not agendamentos:
        print("Nenhum agendamento registrado.")
        return
    for a in agendamentos:
        print(f"ID: {a['id']} | Data/Hora: {a['data']} {a['hora']} | Cliente: {a['cliente_nome']} | Serviço: {a['servico_nome']} | Status: {a['status']}")

def alterar_status_agendamento(agendamentos, novo_status):
    try:
        id_agendamento = int(input("Digite o ID do agendamento: "))
        agendamento = next((a for a in agendamentos if a['id'] == id_agendamento), None)
        
        if agendamento:
            agendamento['status'] = novo_status
            print(f"Agendamento alterado para: {novo_status}. (Histórico preservado - RNF04)")
        else:
            print("Agendamento não encontrado.")
    except ValueError:
        print("Erro: ID inválido.")

def historico_cliente(agendamentos):
    print("\n--- Histórico do Cliente ---")
    nome = input("Digite o nome exato do cliente: ").strip().lower()
    
    encontrados = [a for a in agendamentos if a['cliente_nome'].lower() == nome]
    if encontrados:
        for a in encontrados:
            print(f"Data: {a['data']} {a['hora']} | Serviço: {a['servico_nome']} | Status: {a['status']}")
    else:
        print("Nenhum histórico encontrado para este cliente.")