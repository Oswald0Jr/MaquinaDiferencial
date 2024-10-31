# Função recursiva para calcular as diferenças finitas
def babbage(valores, ordem=1):
    if ordem == 1:
        return [valores[i] - valores[i + 1] for i in range(len(valores) - 1)]
    else:
        return babbage(babbage(valores, ordem - 1), 1)

# Função para montar a tabela de diferenças recursivamente
def montar_tabela(valores):
    tabela = [valores]
    for ordem in range(1, len(valores)):
        tabela.append(babbage(tabela[ordem - 1]))
    return tabela

# Função recursiva para calcular o valor de um polinômio
def polinomio(x, coeficientes, grau):
    if grau < 0:
        return 0
    return coeficientes[0] * (x ** grau) + polinomio(x, coeficientes[1:], grau - 1)

# Exemplo de uso com valores
coeficientes = [2, -2, 3, 2]  # Coeficientes do polinômio
grau = len(coeficientes) - 1
eixo_x = list(range(10))
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]

# Montando a tabela de diferenças
tabela_dif = montar_tabela(eixo_y)

# Exibindo a tabela no terminal
print("Valores de x:", eixo_x)
print("Valores de y:", eixo_y)
print("\nTabela de Diferenças Finitas:")
for c, linha in enumerate(tabela_dif):
    print(f"Nível {c}: {linha}")