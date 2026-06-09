import json

print("--- 🤖 MANIPULADOR DE CONFIGURAÇÕES (JSON) ---")

# 1. O comando abaixo lê o arquivo JSON e transforma numa estrutura do Python
with open("config.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Se você der um print(dados), vai ver que ele virou um Dicionário Python!
print(f"Status Atual do Servidor: {dados['status']}")


# ==========================================================
# 🛠️ AGORA É COM VOCÊ!
# LÓGICA: Altere o valor da chave "status" dentro do dicionário 'dados' para "ativo".
# DICA: Lembra como altera uma caixinha/variável? dados["status"] = ...
# ==========================================================
#2
dados["status"] = "ativo"

# 3. O comando abaixo pega o dicionário atualizado e salva de volta no arquivo
with open("config.json", "w", encoding="utf-8") as arquivo:
    # O indent=4 deixa o arquivo JSON bonitinho e organizado
    json.dump(dados, arquivo, indent=4)

print("✅ Configuração atualizada e salva com sucesso no config.json!")