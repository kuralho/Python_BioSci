def maiuscula(s):
    y = {}
    if len(s) <= 10000:
        palavras = s.split()  
        for palavra in palavras: 
            if palavra in y:
                y[palavra] += 1  
            else:
                y[palavra] = 1
        
        tupla = list(y.items())          
        for chave, valor in tupla:
            print(chave, valor)
    return chave