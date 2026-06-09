import sqlite3

print("--- 🤖 AWS CLOUD MONITOR & INVENTORY (SQL) ---")

# 1. Conecta ao banco de dados local do seu portfólio
conexao = sqlite3.connect("infraestrutura_aws.db")
cursor = conexao.cursor()

# 2. Cria a tabela simulando servidores EC2 da AWS se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS servidores_ec2 (
    id TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    custo_hora REAL NOT NULL,
    status TEXT NOT NULL
)
""")

# 3. Dados simulados da AWS que vamos inserir (Lista de Dicionários!)
servidores_provedor = [
    {"id": "i-0abcd1234efgh5678", "nome": "Web-Production-01", "custo_hora": 0.0464, "status": "running"},
    {"id": "i-09876fedcba43210", "nome": "DB-Replica-Postgres", "custo_hora": 0.0928, "status": "stopped"},
    {"id": "i-0112233445566778", "nome": "API-Gateway-Core", "custo_hora": 0.0232, "status": "running"}
]

# 4. Inserindo os dados no banco usando loops e segurança
for servidor in servidores_provedor:
    try:
        cursor.execute("""
        INSERT OR REPLACE INTO servidores_ec2 (id, nome, custo_hora, status)
        VALUES (?, ?, ?, ?)
        """, (servidor["id"], servidor["nome"], servidor["custo_hora"], servidor["status"]))
    except sqlite3.Error as e:
        print(f"⚠️ Erro ao inserir servidor {servidor['nome']}: {e}")

conexao.commit()
print("💾 Inventário de servidores AWS sincronizado com o Banco SQL!")


# Escreva o comando SQL de filtro aqui dentro das aspas:
comando_busca = "SELECT * FROM servidores_ec2 WHERE status = 'running'"

cursor.execute(comando_busca)
servidores_ativos = cursor.fetchall()

print("\n📊 --- SERVIDORES AWS ATIVOS NO MOMENTO ---")
custo_total_hora = 0.0

for s in servidores_ativos:
    # No SQL, as colunas vêm por ordem: 0=id, 1=nome, 2=custo, 3=status
    print(f"🖥️ Instância: {s[1]} | ID: {s[0]} | Custo/Hora: ${s[2]}")
    custo_total_hora += s[2]

print("-" * 50)
print(f"💰 Custo de Infraestrutura Ativa: ${custo_total_hora:.4f} por hora")

conexao.close()