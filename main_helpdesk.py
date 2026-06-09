from modulo_helpdesk import inicializar_banco, abrir_chamado, listar_chamados, fechar_chamado

# Garante que a tabela do banco de dados seja criada ao iniciar o programa
inicializar_banco()

def exibir_menu():
    print("\n" + "="*40)
    print("      🤖 SISTEMA HELPDESK T.I. (SQL)      ")
    print("="*40)
    print("1. Abrir Novo Chamado")
    print("2. Listar Todos os Chamados")
    print("3. Resolver/Fechar Chamado")
    print("4. Sair do Sistema")
    print("="*40)

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        print("\n--- 📝 ABRIR CHAMADO ---")
        titulo = input("Título do problema: ")
        descricao = input("Descrição detalhada: ")
        prioridade = input("Prioridade (Baixa, Media, Alta): ")
        
        abrir_chamado(titulo, descricao, prioridade)
        print("✅ Chamado registrado com sucesso no banco de dados!")

    elif opcao == "2":
        print("\n--- 📋 LISTA DE CHAMADOS NO BANCO ---")
        chamados = listar_chamados()
        if not chamados:
            print("Nenhum chamado encontrado.")
        for c in chamados:
            # Estrutura vinda do SQL: 0=ID, 1=Título, 2=Descrição, 3=Prioridade, 4=Status
            print(f"[{c[4]}] ID: {c[0]} | {c[1]} (Prioridade: {c[3]})")
            print(f"    Descrição: {c[2]}")
            print("-" * 35)

    elif opcao == "3":
        print("\n--- 🔧 RESOLVER CHAMADO ---")
        try:
            id_busca = int(input("Digite o número (ID) do chamado que deseja fechar: "))
            sucesso = fechar_chamado(id_busca)
            if sucesso:
                print(f"✅ Chamado nº {id_busca} finalizado e atualizado no banco!")
            else:
                print("❌ Erro: ID de chamado não encontrado no sistema.")
        except ValueError:
            print("⚠️ Erro: Por favor, digite um número de ID válido.")

    elif opcao == "4":
        print("\n👋 Desconectando do sistema. Até logo, Anderson!")
        break
    else:
        print("⚠️ Opção inválida! Tente um número de 1 a 4.")