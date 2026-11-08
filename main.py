
compras = []
compras.append({
    "nome": "Maquina de Lavar",
    "preco": 1500.00,
    "Prioridade": "Alta",
    "parcelas": 10
})

compras.append({
    "nome": "Fogão",
    "preco": 1200.00,
    "Prioridade": "Média",
    "parcelas": 8
})


print("Organizador de Compras") 
print("-------------------------")

for compra in compras:
    print(f"Nome: {compra['nome']}")
    print(f"Preço: R${compra['preco']:.2f}")
    print(f"Prioridade: {compra['Prioridade']}")
    print(f"Parcelas: {compra['parcelas']}")
    print("-------------------------")


