import csv

print("--- 🤖 CONSOLIDADOR DE RELATÓRIOS (CSV) ---")

total_folha = 0.0


with open("funcionarios.csv", "r", encoding="utf-8") as arquivo:
    
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        
        salario_texto = linha["Salario"]
        
        salario_limpo = float(salario_texto.strip())

        total_folha += salario_limpo
        
        print(f"Funcionário: {linha['Nome'].strip()} | Salário: R$ {salario_limpo:.2f}")

print("-" * 40)
print(f"💰 Gasto total com a folha de pagamento: R$ {total_folha:.2f}")
