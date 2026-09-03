# main.py
import json
import os
from clientes import cadastrar_cliente, consultar_cliente, alterar_cliente
from servicos import cadastrar_servico, alterar_inativar_servico
from agendamentos import cadastrar_agendamento, listar_agendamentos, alterar_status_agendamento, historico_cliente
from historico_fila import exibir_fila_do_dia
from status_agenda import CONCLUIDO, CANCELADO

CAMINHO_DADOS = os.path.join('dados', 'dados.json')

def carregar_dados():
    """Carrega os dados de dados/dados.json ou inicializa a estrutura vazia."""
    estrutura_padrao = {
        "clientes": [],
        "servicos": [],
        "agendamentos": []
    }
    
    if os.path.exists(CAMINHO_DADOS):
        try:
            with open(CAMINHO_DADOS, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for chave in estrutura_padrao:
                    if chave not in dados:
                        dados[chave] = []
                return dados
        except Exception as e:
            print(f"Aviso ao ler {CAMINHO_DADOS}: {e}. Inicializando estrutura vazia.")
            return estrutura_padrao
    else:
        return estrutura_padrao

def salvar_dados(dados):
    """Salva todas as listas no arquivo dados/dados.json (RNF05)."""
    pasta = os.path.dirname(CAMINHO_DADOS)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
        
    with open(CAMINHO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def menu_principal():
    dados = carregar_dados()
    clientes = dados["clientes"]
    servicos = dados["servicos"]
    agendamentos = dados["agendamentos"]

    while True:
        print("\n" + "="*30)
        print("      SISTEMA AGENDABELA")
        print("="*30)
        print("1. Cadastrar Cliente")
        print("2. Consultar/Alterar Cliente")
        print("3. Cadastrar Serviço")
        print("4. Alterar/Inativar Serviço")
        print("5. Realizar Agendamento")
        print("6. Listar Agendamentos")
        print("7. Concluir Atendimento")
        print("8. Cancelar Agendamento")
        print("9. Ver Histórico de Cliente")
        print("10. Exibir Fila do Dia (Queue)")
        print("0. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == '1':
                cadastrar_cliente(clientes)
            elif opcao == '2':
                consultar_cliente(clientes)
                if input("Deseja alterar algum cliente? (S/N): ").strip().upper() == 'S':
                    alterar_cliente(clientes)
            elif opcao == '3':
                cadastrar_servico(servicos)
            elif opcao == '4':
                alterar_inativar_servico(servicos)
            elif opcao == '5':
                cadastrar_agendamento(agendamentos, clientes, servicos)
            elif opcao == '6':
                listar_agendamentos(agendamentos)
            elif opcao == '7':
                listar_agendamentos(agendamentos)
                alterar_status_agendamento(agendamentos, CONCLUIDO)
            elif opcao == '8':
                listar_agendamentos(agendamentos)
                alterar_status_agendamento(agendamentos, CANCELADO)
            elif opcao == '9':
                historico_cliente(agendamentos)
            elif opcao == '10':
                exibir_fila_do_dia(agendamentos)
            elif opcao == '0':
                print("Salvando dados em dados/dados.json e encerrando...")
                salvar_dados(dados)
                break
            else:
                print("Opção inválida.")
                
            # Grava automaticamente no dados.json a cada alteração
            salvar_dados(dados)

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    menu_principal()