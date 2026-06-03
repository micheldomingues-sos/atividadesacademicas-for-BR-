def calcular_total(produtos):
    """Retorna a soma de todos os preços no dicionário."""
    return sum(produtos.values())

def produto_mais_caro(produtos):
    """Retorna o nome e o preço do produto com o maior valor."""
    if not produtos:
        return None, 0
    nome = max(produtos, key=produtos.get)
    return nome, produtos[nome]

def produto_mais_barato(produtos):
    """Retorna o nome e o preço do produto com o menor valor."""
    if not produtos:
        return None, 0
    nome = min(produtos, key=produtos.get)
    return nome, produtos[nome]

def principal():
    produtos = {}
    total_cadastros = 5

    print(f"--- Cadastro de {total_cadastros} Produtos ---")
    
    # Parte 3: Utilizando estrutura de repetição 'for'
    for i in range(1, total_cadastros + 1):
        nome = input(f"Informe o nome do {i}º produto: ").strip()
        
        # Parte 3: Utilizando 'while' para validar entrada numérica (Tratamento de Erros)
        while True:
            try:
                preco = float(input(f"Informe o preço de '{nome}': "))
                if preco < 0:
                    print("O preço não pode ser negativo. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número para o preço.")
        
        # Parte 1: Organizando dados em um dicionário
        produtos[nome] = preco

    # Parte 4: Relatório Final
    print("\n" + "="*30)
    print("       RELATÓRIO FINAL")
    print("="*30)
    
    print("Produtos cadastrados:")
    for nome, preco in produtos.items():
        print(f" - {nome}: R$ {preco:.2f}")
    
    # Cálculos utilizando as funções da Parte 2
    total = calcular_total(produtos)
    nome_caro, preco_caro = produto_mais_caro(produtos)
    nome_barato, preco_barato = produto_mais_barato(produtos)
    
    # Média de preços
    media = total / len(produtos) if produtos else 0

    print("-" * 30)
    print(f"Valor Total: R$ {total:.2f}")
    print(f"Média de Preços: R$ {media:.2f}")
    print(f"Produto mais caro: {nome_caro} (R$ {preco_caro:.2f})")
    print(f"Produto mais barato: {nome_barato} (R$ {preco_barato:.2f})")
    print("="*30)

if __name__ == "__main__":
    principal()
