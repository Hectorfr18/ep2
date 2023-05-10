def posicao_valida(dicionario,linha,coluna,orientacao,tamanho):
    resultado = []
    for i in range(tamanho):
        if orientacao == "vertical":
            resultado.append([linha,coluna])
            if linha>9 or linha<0:
                return False
            linha+=1
            
        else:
            resultado.append([linha,coluna])
            if coluna>9 or coluna<0:
                return False
            coluna+=1
            

    
    for nome_navio, lista in dicionario.items():
        for posicao in lista:
            for pos_especifica in posicao:
                if pos_especifica in resultado:
                    return False
    return True