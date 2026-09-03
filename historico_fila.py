# historico_fila.py
from status_agenda import AGENDADO

def exibir_fila_do_dia(agendamentos):
    print("\n--- Fila de Atendimentos do Dia ---")
    data_hoje = input("Digite a data (DD/MM/AAAA) para ver a fila: ").strip()
    
    # Filtra apenas os agendados para a data específica
    fila = [a for a in agendamentos if a['data'] == data_hoje and a['status'] == AGENDADO]
    
    # Ordena pelo horário (Fila em ordem cronológica)
    fila_ordenada = sorted(fila, key=lambda k: k['hora'])
    
    if fila_ordenada:
        print(f"Total na fila: {len(fila_ordenada)}")
        for i, a in enumerate(fila_ordenada, 1):
            print(f"{i}º da Fila -> {a['hora']} | Cliente: {a['cliente_nome']} ({a['servico_nome']})")
    else:
        print("A fila está vazia para esta data.")