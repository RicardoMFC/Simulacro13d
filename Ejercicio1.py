def palabras_clave(texto):
    lista_aux=[]
    for i in range (2,len(texto),1):
        if texto[i-1]=='#' and texto[i]=='#':
            j=i+1
            while texto[j]!='#':
                lista_aux.append(texto[j])
            i=j
    return lista_aux



def main():
    cadena=["#","#","#","g","o", "#","g","o","#","#","h","o","l","a"]
    resultado=palabras_clave(cadena)
    print(resultado)

if __name__=='__main__':
    main()