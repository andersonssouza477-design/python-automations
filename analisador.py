import csv

print("--- 🤖 CONSOLIDADOR DE RELATÓRIOS (CSV) ---")

total_folha = 0.0

# O comando abaixo abre o arquivo que você criou
with open("funcionarios.csv", "r", encoding="utf-8") as arquivo:
    # O DictReader lê o CSV transformando cada linha em um mini-dicionário
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        # 1. Pegamos o salário bruto (que vem como texto e com espaços)
        salario_texto = linha["Salario"]
        
        # 2. AGORA É COM VOCÊ!
        # DICA: Use o .strip() para tirar os espaços da variável 'salario_texto'
        # e converta o resultado para float(). Guarde isso numa variável 'salario_limpo'.
        salario_limpo = float(salario_texto.strip())

        # 3. Some o 'salario_limpo' ao seu 'total_folha'
        total_folha += salario_limpo
        # 4. Adicione um print para mostrar o nome do funcionário limpo e o salário
        # Ex: print(f"Funcionário: {linha['Nome'].strip()} | Salário: R$ {salario_limpo}")
        print(f"Funcionário: {linha['Nome'].strip()} | Salário: R$ {salario_limpo:.2f}")


# Fora do loop, mostre o total geral calculado
print("-" * 40)
print(f"💰 Gasto total com a folha de pagamento: R$ {total_folha:.2f}")