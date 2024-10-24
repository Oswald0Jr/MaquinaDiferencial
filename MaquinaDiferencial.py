
# funcao recursiva para calcular as diferencas finitas
def diferencas_finitas_recursivo(valores, ordem=1):
    """Calcula a diferença de ordem 'ordem' de forma recursiva."""
    if ordem == 1:
        return [valores[i+1] - valores[i] for i in range(len(valores) - 1)]
    else:
        return diferencas_finitas_recursivo(diferencas_finitas_recursivo(valores, ordem - 1), 1)

# funcao para montar a tabela de diferencas recursivamente
def montar_tabela_diferencas(valores):
    """Monta a tabela de diferenças completa recursivamente"""
    tabela = [valores]
    for ordem in range(1, len(valores)):
        tabela.append(diferencas_finitas_recursivo(tabela[ordem - 1]))
    return tabela

# funcao recursiva para interpolacao
def interpolar_recursivo(tabela_dif, x_valores, x, s=None, grau=None, ordem=0):
    """Interpolação recursiva para polinomios de qualquer grau"""
    if ordem == 0:
        h = x_valores[1] - x_valores[0]  # espacamento entre valores de x
        s = (x - x_valores[0]) / h  # fator de interpolacao
        if grau is None or grau >= len(x_valores):
            grau = len(x_valores) - 1  # grau maximo permitido
        return tabela_dif[0][0] + interpolar_recursivo(tabela_dif, x_valores, x, s, grau, 1)
    
    if ordem > grau:
        return 0
    
    # calculando o termo recursivo
    termo = tabela_dif[ordem][0]
    for i in range(ordem):
        termo *= (s - i) / (i + 1)
    
    return termo + interpolar_recursivo(tabela_dif, x_valores, x, s, grau, ordem + 1)

# exemplo de uso para polinomio de qualquer grau
x_valores = [1, 2, 3, 4, 5]
y_valores = [5, 9, 15, 23, 33]


# montando a tabela de diferenças de forma recursiva
tabela_dif = montar_tabela_diferencas(y_valores)

# alculando valor de x para polinomio de grau 2 (ou qualquer grau que deseja)
x_novo = 6
grau_2= 2
resultado_grau_2 = interpolar_recursivo(tabela_dif, x_valores, x_novo, grau_2)
print(f"Valor interpolado recursivamente para x = {x_novo} com grau 2: {resultado_grau_2:.4f}")

# calculando valor de x para polinomio de qualquer grau
x_novo_geral = 9
resultado_geral = interpolar_recursivo(tabela_dif, x_valores, x_novo_geral)
print(f"Valor interpolado recursivamente para x = {x_novo_geral} (grau máximo): {resultado_geral:.4f}")