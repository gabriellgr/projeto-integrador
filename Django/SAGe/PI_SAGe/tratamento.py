def tratar_palavra(palavra:str):
    palavra=list(palavra.lower())
    counter = 0
    
    for i in palavra:
        
        #vogais
        if i == "é" or i=='è'or i=='ê':
            palavra[counter]='e'
            
        if i == "á" or i=='à'or i=='â':
            palavra[counter]='a'
        
        if i == "í" or i=='ì'or i=='î':
            palavra[counter]='i'
            
        if i == "ó" or i=='ò'or i=='ô':
            palavra[counter]='o'
            
        if i == "ú" or i=='ù'or i=='û':
            palavra[counter]='u'
        #ponto
        if i =='.':
            palavra[counter]=''
        if i=="." or i=='-':
            palavra[counter]=''
            
        counter+=1
            
    print(''.join(palavra))
    
    return ''.join(palavra)

if __name__=='__main__':
    tratar_palavra('É um teste à palavras que contêm acentos (à,è,ì,ò,ù ).-----')
    #saida: e um teste a palavras que contem acentos (a,e,i,o,u )