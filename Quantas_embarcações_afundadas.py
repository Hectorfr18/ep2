def afundados(dic_navios_tabuleiro, tabuleiro):
    afundado = True
    qtd_afundados = 0
    for nome_navio, lista in dic_navios_tabuleiro.items():
        for posicao in lista:
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] != "X":
                    afundado = False
                
            if afundado:
                qtd_afundados+=1
            afundado = True
    return qtd_afundados
                