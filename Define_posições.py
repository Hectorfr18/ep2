def define_posicoes(linha,coluna,orientacao,tamanho):
    resultado = []
    for i in range(tamanho):
        if orientacao == "vertical":
            resultado.append([linha,coluna])
            linha+=1
        else:
            resultado.append([linha,coluna])
            coluna+=1
    return resultado