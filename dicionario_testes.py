# Criando um dicionário
meu_dicionario = {
    "nome": "Ana",
    "idade": 28,
    "profissão": "Engenheira",
    "cidade": "São Paulo"
}

# Acessando valores no dicionário
print(meu_dicionario["nome"])       # Saída: Ana
print(meu_dicionario["idade"])      # Saída: 28

# Adicionando um novo par chave-valor
meu_dicionario["país"] = "Brasil"

# Atualizando um valor existente
meu_dicionario["idade"] = 29

# Removendo um par chave-valor
del meu_dicionario["cidade"]

# Iterando sobre chaves e valores
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

# Verificando se uma chave existe no dicionário
if "profissão" in meu_dicionario:
    print("A chave 'profissão' está no dicionário.")

# Obtendo um valor com um valor padrão caso a chave não exista
altura = meu_dicionario.get("altura", "Chave não encontrada")
print(altura)   # Saída: Chave não encontrada