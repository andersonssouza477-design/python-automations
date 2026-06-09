import sqlite3

def inicializar_banco():
    """Cria o banco de dados e a tabela de chamados se não existirem."""
    conexao = sqlite3.connect("chamados_ti.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

def abrir_chamado(titulo, descricao, prioridade):
    """Insere um novo chamado no banco SQL."""
    conexao = sqlite3.connect("chamados_ti.db")
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO chamados (titulo, descricao, prioridade, status)
    VALUES (?, ?, ?, 'ABERTO')
    """, (titulo, descricao, prioridade.upper()))
    conexao.commit()
    conexao.close()

def listar_chamados():
    """Busca e retorna todos os chamados salvos no banco."""
    conexao = sqlite3.connect("chamados_ti.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM chamados")
    todos_chamados = cursor.fetchall()
    conexao.close()
    return todos_chamados

def fechar_chamado(id_chamado):
    """Atualiza o status de um chamado para FECHADO com base no ID."""
    conexao = sqlite3.connect("chamados_ti.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE chamados SET status = 'FECHADO' WHERE id = ?", (id_chamado,))
    # rowcount nos diz quantas linhas foram alteradas no banco
    linhas_alteradas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_alteradas > 0